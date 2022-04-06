def main_context(request):
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
        print(cartLength)
    except:
        pass    
   
    return {
        'domain' : request.META['HTTP_HOST'],
        'cartLength' : cartLength
    }