$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr' + $('html')[0].lang, (data, textStatus) => {
    $('DIV#hello').text(data.hello);
  });
});
