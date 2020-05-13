#!/usr/bin/node
// Wedge movie count
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
    if (err) {
	console.log(err);
    } else if (response.statusCode === 200) {
	let films = JSON.parse(body).results;
	let count = 0;
	for (let movies in films) {
	    let chars = films[movies].characters;
	    for (let index in Chars) {
		if (Chars[index].includes('18')) {
		    count++;
		}
	    }
	}
	console.log(count);
    } else {
	console.log('An error occured. Status code: ' + response.statusCode);
    }
});
