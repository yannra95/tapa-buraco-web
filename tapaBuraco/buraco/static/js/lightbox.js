$(function() {

  $(".clickable-row").click(function() {
    $('.lb-background').animate({'opacity':'0.60'}, 500, 'linear');
    $('.lb-background, .lightbox, .close').css('display', 'block');
    $(this).addClass("row-selected");

    var text = $(this).children('td:nth-of-type(1)').text();
    $('#lb-id').val(text);

    text = $(this).children('td:nth-of-type(2)').text();
    $('#lb-agente').val(text);

    text = $(this).children('td:nth-of-type(3)').text();
    $('#lb-lati').val(text);

    text = $(this).children('td:nth-of-type(4)').text();
    $('#lb-longi').val(text);
    
    text = $(this).children('td:nth-of-type(5)').text();
    $('#lb-acc').val(text);
    
    console.log("td: ",text);



  });

  $('.close').click(function(){
    $('.lb-background, .lightbox').css('display','none');
    /*$('.lb img').css('opacity','0');*/
  });
});