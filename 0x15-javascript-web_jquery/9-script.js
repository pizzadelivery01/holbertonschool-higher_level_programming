// gets value of hello from link
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function hello(data) {
    $('div#hello').text(data.hello);
});