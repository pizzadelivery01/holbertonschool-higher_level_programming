#!/usr/bin/node
// square
module.exports = class Square extends require('./5-square') {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
