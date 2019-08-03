//  ***   set slider size equal to viewport   ***
$(document).ready(function() {
    function setHeight() {
      windowHeight = $(window).innerHeight() -56;
      $('.carousel-inner,.img-full,.full-view').css('height', windowHeight);
      $('.carousel-inner,.img-full,.full-view').width(window.innerWidth);
    };
    setHeight();
  
    $(window).resize(function() {
      setHeight();
    });
  });


//    *** BS4 tooltip
$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});