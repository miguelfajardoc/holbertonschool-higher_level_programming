#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  let i;
  for (i in list) {
    if (list[i] === searchElement) {
      a++;
    }
  }
  return a;
};
