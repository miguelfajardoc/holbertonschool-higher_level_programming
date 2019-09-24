#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) & Number.isInteger(h)) {
      if (w > 0 & h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    let string = '';
    let i = 0;
    for (i = 0; i < this.width; i++) {
      string += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
}

module.exports = Rectangle;
