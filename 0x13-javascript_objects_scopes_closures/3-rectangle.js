#!/usr/bin/node
// rectangle
module.exports = class Rectangle {
    constructor (w, h) {
	if (w > 0 && h > 0){
	    this.width = w;
	    this.height = h;
	}
    }

    print() {
	for (let i = 0;  < this.height; i++) {
	    console.log('X'.repeat(this.width));
	}
    }
};
