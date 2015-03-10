


// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});


$(function(){
   $('.form .mylink').click(function(){
      $(".form .mylink").hide();
      $('.form .second').show();
      $('.form .third').show();
      $('.form .fourth').show();
      $('.form .fifth').show();
      $('.form .mylink2').show();

      return false;
   });
});

$(function(){
   $('.form .mylink2').click(function(){
      $('.form .mylink2').hide();
      $('.form .second').hide();
      $('.form .third').hide();
      $('.form .fourth').hide();
      $('.form .fifth').hide();
      $(".form .mylink").show();
      

      return false;
   });
});


$(function(){
   $('.up').click(function(){
      $(".up").hide();
      $(".down").show();

      return false;
   });
});

$(function(){
   $('.down').click(function(){
      $(".down").hide();
      $(".up").show();
      
      return false;
   });
});

