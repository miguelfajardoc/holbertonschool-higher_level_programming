#!/usr/bin/node

const x = parseInt(process.argv[2]);

function factorial (a) {
  if (!a) { return 1; }
  if (a === 1 || a === -1) { return 1; }
  if (a > 1) {
    return (a * factorial(--a));
  } else {
    return (a * factorial(++a));
  }
}

console.log(factorial(x));
