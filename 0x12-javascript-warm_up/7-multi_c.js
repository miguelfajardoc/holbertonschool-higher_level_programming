#!/usr/bin/node

let x = Number(process.argv[2]);
if (x) {
  while (x !== 0) {
    console.log('C is fun');
    if (x < 0) { x++; } else { x--; }
  }
} else {
  console.log('Missing number of occurrences');
}
