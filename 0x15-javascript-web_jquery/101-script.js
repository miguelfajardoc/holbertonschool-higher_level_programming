window.addEventListener("load", function(){
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
})
