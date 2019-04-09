$(document).ready(function(){
   $('form > div:nth-child(4) > div > input').focusout(function(){$('form > div:nth-child(4) > div > input').val("")});
   $('form > div:nth-child(5)').hide();
});
