#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(1);
} else {
  const l = process.argv;
  l.shift();
  l.shift();
  l.sort(function (a, b) { return b - a; });
  console.log(l[1]);
}
