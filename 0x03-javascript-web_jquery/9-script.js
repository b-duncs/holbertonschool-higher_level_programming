#!/usr/bin/node
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});
