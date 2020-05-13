#!/usr/bin/node
// scrape page
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
