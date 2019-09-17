#!/usr/bin/node

let x = Number(process.argv[2]);
let y = x;
let string = '';
if (x) {
  while (x !== 0) {
    if (x < 0){ break; }
    while (y !== 0){
      string += 'X';
      y--;
      }
      console.log(string);
    x--;
  }
} else {
  console.log('Missing size');
}
