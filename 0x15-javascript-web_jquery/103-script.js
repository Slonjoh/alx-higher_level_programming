$(function () {
  $('INPUT#btn_translate').click(() => {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data, textStatus) => {
      translate = data.hello;
      $('DIV#hello').text(translate);
    });
  });
  $('INPUT#language_code').keypress((e) => {
    if (e.which === 13) {
      $.get('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data, textStatus) => {
        translate = data.hello;
        $('DIV#hello').text(translate);
      });
    }
  });
});
