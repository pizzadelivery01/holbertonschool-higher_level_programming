#!/usr/bin/node
// write file
const fs = require('fs');
const file = process.argv[2];
const output = process.argv[3];

fs.writeFile(file, output, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
