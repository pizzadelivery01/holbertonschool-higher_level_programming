#!/usr/bin/node
// starwars titles
const request = require('request');
const url = 'http://swapi.co/api/films/';
const episode = process.argv[2];
request(url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
