from importlib.resources import contents
from django.shortcuts import render, get_object_or_404
from web.models import Category, Offer, Product, Banner, Gallery,Vat
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import operator

# Create your views here.

def index(request):
    vat =Vat.objects.all()[:1]
    banner = Banner.objects.all()
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.all()[:6]
    offers = Offer.objects.all()
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    context = {
        "is_index" : True,
        'banner': banner,
        'categories': categories,
        'products': products,
        'offers': offers,
        "cartLength": cartLength,
        "vat" : vat,
    }
    return render(request,'web/index.html',context)

def menu(request):
    vat =Vat.objects.all()[:1]
    categories = Category.objects.all()
    products = Product.objects.all()
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass
    context = {
        "is_about" : True,
        'categories': categories,
        'products': products,
        'cartLength': cartLength,
        'vat' : vat,
    }
    return render(request, 'web/menu.html', context)


def gallery(request):
    galleries = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        'galleries': galleries
    }
    return render(request, 'web/gallery.html', context)


def shopDetails(request,name,address):
    cartLength =''
    messagestring = ''
    grandtotal=0
    data = []
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
        messagestring = 'https://wa.me/966555021109?text=Name :'+name+'%0aExpected Time :'+address+\
                "%0a-----Order Details------"
        for i in request.session['cartdata']:
            cart =request.session['cartdata'][i]
            data1 = {
                'id':cart['id'],
                'name':cart['Product_name'],
                'image':cart['Product_image'],
                'quantity':cart['quantity'],
                'price':cart['product_price'],
                'sub_total':int(cart['quantity']) * int(cart['product_price'])               
            }
            data.append(data1)
            grandtotal+=int(cart['quantity']) * int(cart['product_price'])   
        for i in data:
            messagestring +="%0aProduct-Id:"+str(i['id'])+"%0aName:"+str(i['name'])+"%0aQty:"+str(i['quantity'])+"%0aPrice:"+str(i['price'])+"%0aTotal :"+str(i['sub_total'])+"%0a-----------------------------"
        messagestring+="%0a-----------------------------%0a\
        Grand Total :"+str(grandtotal)+"%0a--------------------------------"
    except Exception as e:
        pass
    context = {
        'link':messagestring
    }
    return render(request,'web/shop-details.html',context)


def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact": True,
            "forms": forms,

        }
        return render(request, 'web/contact.html', context)


# =============cart system

def cart(request):
    cartLength = ''
    subTotal = ''
    data = []
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
        for i in request.session['cartdata']:
            selectfgf = request.session['cartdata'][i]
            data1 = {
                'id': selectfgf['id'],
                'name': selectfgf['Product_name'],
                'image': selectfgf['Product_image'],
                'quantity': selectfgf['quantity'],
                'price': selectfgf['product_price'],
                'sub_total': int(selectfgf['quantity']) * int(selectfgf['product_price'])
            }
            data.append(data1)
        subTotal = sum(map(operator.itemgetter('sub_total'), data))
        
        if request.method == "POST":
            name = request.POST.get('name')
            address = request.POST.get('time')
            return HttpResponseRedirect('/check-out/'+name+'/'+address+'/') 
    except Exception as e:
        pass
    context = {
            'cart_length':cartLength,
            'cart_data':data,
            'total':subTotal
        }
    return render(request, 'web/cart.html', context)


def add_cart(request):
    msg = ''
    price = ''
    # del request.session['cartdata']
    productId = request.POST['product_id']
    productDetails = Product.objects.get(id=productId)
    if productDetails.price != None:
        price = productDetails.price
    else:
        price = productDetails.price

    cart_p = {}
    cart_p[str(productId)] = {
        'id': productId,
        'Product_name': productDetails.title,
        'Product_image': productDetails.image.url,
        'product_price': price,
        'quantity': 1,
    }
    if 'cartdata' in request.session:  # session check

        if productId in request.session['cartdata']:
            if(str(productId in request.session['cartdata'])):
                msg = '1'
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata'] = cart_data
            msg = '0'

    else:
        request.session['cartdata'] = cart_p
        msg = '0'
    return JsonResponse({'data': request.session['cartdata'], 'length': len(request.session['cartdata']), 'msg': msg})



def cart_delete(request):
    length = ''
    id = request.POST['product_id']
    pr = request.session['cartdata'][id]
    price = pr['product_price']
    try:
        length = len(request.session['cartdata'])
        del request.session['cartdata'][id]
        request.session.modified = True
        length = len(request.session['cartdata'])
        if length > 0:
            pass
        else:
            del request.session['cartdata']

    except Exception as e:
        print(e)
    return JsonResponse({'length':length,'price':price})


def update_cart(request):

    id = request.POST['id']
    productId = request.POST['product_id']
    quantity = request.POST['quantity']
    qty = ''
    price = ''
    qty1 = ''
    data = []
    subTotal = ''
    try:
        if id == '1':
            updateCart = request.session['cartdata'][productId]
            updateCart['quantity'] = quantity
            request.session.modified = True
            price = updateCart['product_price']
            for i in request.session['cartdata']:
                cart =request.session['cartdata'][i]
                data1 = {
                    'id':cart['id'],
                    'name':cart['Product_name'],
                    'image':cart['Product_image'],
                    'quantity':cart['quantity'],
                    'price':cart['product_price'],
                    'sub_total':int(cart['quantity']) * int(cart['product_price'])
                }
                data.append(data1)
            subTotal = sum(map(operator.itemgetter('sub_total'),data))
        else:
            updateCart = request.session['cartdata'][productId]
            updateCart['quantity'] = quantity
            request.session.modified = True
            price = updateCart['product_price']
            for i in request.session['cartdata']:
                cart =request.session['cartdata'][i]
                data1 = {
                    'id':cart['id'],
                    'name':cart['Product_name'],
                    'image':cart['Product_image'],
                    'quantity':cart['quantity'],
                    'price':cart['product_price'],
                    'sub_total':int(cart['quantity']) * int(cart['product_price'])
                }
                data.append(data1)
            subTotal = sum(map(operator.itemgetter('sub_total'),data))

    except Exception as e:
        pass
    return JsonResponse({'quantity':quantity,'price':price,'sub_total':subTotal})
















def shopDetails(request,):
    
    context = {
        
    }
    return render(request, 'web/shop-details.html', context)

def menudemo(request,):
    context = {
        
    }
    return render(request, 'web/menu-demo.html', context)

def productshow(request):
    a = []
    categoryId  = request.POST['category_id']
    obj = Product.objects.filter(category_id = categoryId)
    for i in obj:

        data = {
            'image':i.image.url,
            'title':i.title,
            'cal':i.cal,
            'price':i.price
        }
        a.append(data)

    return JsonResponse({'data':a})