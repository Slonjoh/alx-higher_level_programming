window.onload = () => {
  $(function () {
    $('DIV#add_item').click(() => {
      $('ul.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(() => {
      $('li').last().remove();
    });
    $('DIV#clear_list').click(() => {
      $('ul.my_list').empty();
    });
  });
};
