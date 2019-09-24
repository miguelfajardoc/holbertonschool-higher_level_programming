#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let string = '';
    let i = 0;
    for (i = 0; i < this.width; i++) {
      string += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
}

module.exports = Square;
