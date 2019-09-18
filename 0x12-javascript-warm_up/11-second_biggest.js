#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(1);
}
else {
  let l = process.argv;
  l.shift();
  l.shift();
  l.sort();
  l.pop();
  console.log(Math.max.apply(null, l));
}
