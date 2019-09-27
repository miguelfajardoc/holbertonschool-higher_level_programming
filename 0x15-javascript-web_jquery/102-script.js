window.addEventListener("load", function(){
  data = {'lang': 'es'}
  $.getJSON('https://fourtonfish.com/hellosalut/', data, function (hello) {
    $('#hello').text(hello.hello);
  });
})