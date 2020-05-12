#!/usr/bin/node
// map
let data = require('./100-data').list;
console.log(data);
console.log(data.map((x, y) => x * y));
