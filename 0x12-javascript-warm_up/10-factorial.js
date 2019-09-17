#!/usr/bin/node

const x = Number(process.argv[2]);

function factorial (a) {
  if (!a) { return a; }
  if (a === 1) { return 1; }
  return (a * factorial(--a));
}

console.log(factorial(x));
