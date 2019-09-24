#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
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
