def main_context(request):
    cartLength = ''
    try:
        cartLength = len(request.session['cartdata'])
    except:
        pass    
   
    return {
        'domain' : request.META['HTTP_HOST'],
        'cartLength' : cartLength
        
    }