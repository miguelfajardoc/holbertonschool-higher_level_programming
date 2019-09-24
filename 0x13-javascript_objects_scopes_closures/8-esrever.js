#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  const rever = [];
  while (i < list.length) {
    rever[list.length - i - 1] = list[i];
    i++;
  }
  return rever;
};
