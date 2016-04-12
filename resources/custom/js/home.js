function scrollToID(id){
  $('html, body').animate({
      scrollTop: $(id).offset().top
  }, 2000);
};

setTimeout(scrollToID.bind(null, '#profile'), 3000);
