#!/usr/bin/node

let x = Number(process.argv[2]);
if (x) {
  while (x !== 0) {
    if (x < 0) { return; }
    console.log('C is fun');
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
