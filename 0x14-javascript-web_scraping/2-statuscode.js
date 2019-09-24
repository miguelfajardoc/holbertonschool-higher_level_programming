#!/usr/bin/node

const fs = require('request');
const path = process.argv[2];

fs(path, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log("Code: " + response.statusCode);
  }
});
