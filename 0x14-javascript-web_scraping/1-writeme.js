#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const input = process.argv[3];

fs.writeFile(path, input, function (error, response) {
  if (error) {
    console.log(error);
  }
});
