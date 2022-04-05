
function addCart(productId,thisProp){
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    data = {
        'product_id':productId,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: '/add-cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        beforeSend: function() {
            $(thisProp).prop('disabled', true); // disable button
          },
        success: function(response){
            $("[id=cartCount]").html(response['length'])
            $(thisProp).prop('disabled', false);

            if(response['msg'] == '1'){
                $('#icon'+productId).toggleClass('fa-light fa-cart-arrow-down');
            }
            else{
                $('#icon'+productId).toggleClass('fa-light fa-cart-arrow-down');
            }
        }
    });
};


function updateQuantity(productId,b){
    quantity = $("#quantityId"+productId).val()
   
    // $(quantity).val(qty)
    // var $qty = $(b).closest('.quantity').find(".qty");
   
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    data = {
        'id':'1',
        'product_id':productId,
        'quantity':quantity,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: '/update-cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        success: function(response){ 
            updateTotal = response['quantity'] * response['price']
            $("#subTotalPrice"+productId).html('ر.س.'+updateTotal+'.00')
            $("#subTotal").html('ر.س.'+response['sub_total']+'.00')

        }
    });
}






function deleteProduct (productId,df){
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    data = {
        // 'id':'81456',
        'product_id':productId,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: '/delete-cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        success: function(response){
            console.log(response['length']) 
            $("[id=cartCount]").html(response['length'])
            var subTotal = $("#subTotalInputId").val();
            finalSubTotal = parseInt(subTotal) - parseInt(response['price'])
            $("#subTotal").html('SAR.'+finalSubTotal+'.00')
            $("#product-box"+productId).hide()

            if(response['length'] == '0'){
                $("#subTotal").html('SAR.'+'0'+'.00')

            }
        }
    });

};