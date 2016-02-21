var scrollToID = function(id){
  $('html, body').animate({
      scrollTop: $(id).offset().top
  }, 2000);
};
