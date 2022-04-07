$('.product-items').imagesLoaded( function() {

    // Add isotope click function
   $('.food-menu-filter li').on( 'click', function(){
       $(".food-menu-filter li").removeClass("active");
       $(this).addClass("active");

       var selector = $(this).attr('data-filter');
       $(".product-items").isotope({
           filter: selector,
           animationOptions: {
               duration: 750,
               easing: 'linear',
               queue: false,
           }
       });
       return false;
   });

   $(".product-items").isotope({
       itemSelector: '.isotop-grid',
       layoutMode: 'masonry',
   });
});


// Wow JS Active
new WOW().init();