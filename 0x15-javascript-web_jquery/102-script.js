$(function () {
  $('INPUT#btn_translate').click(() => {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data, textStatus) => {
      translate = data.hello;
      $('DIV#hello').text(translate);
    });
  });
});
