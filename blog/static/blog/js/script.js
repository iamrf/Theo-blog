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
  //  ***   set slider size equal to viewport   ***
  


  function myFunction(imgs) {
    // Get the expanded image
    var expandImg = document.getElementById("expandedImg");
    // Get the image text
    var imgText = document.getElementById("album-imgtext");
    // Use the same src in the expanded image as the image being clicked on from the grid
    expandImg.src = imgs.src;
    // Use the value of the alt attribute of the clickable image as text inside the expanded image
    imgText.innerHTML = imgs.alt;
    // Show the container element (hidden with CSS)
    expandImg.parentElement.style.display = "block";
  } 


  //  ***   detail page's image slider  ***