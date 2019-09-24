#!/usr/bin/node
let x = 0;
exports.logMe = function (item) {
  function counter () {
    console.log(x + ':' + item);
    x++;
  }
  counter();
};
