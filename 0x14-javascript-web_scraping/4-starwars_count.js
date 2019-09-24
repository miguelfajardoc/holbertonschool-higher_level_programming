#!/usr/bin/node

const req = require('request');
const path = process.argv[2];
let count = 0;

req(path, function (error, respond, body) {
  const response = JSON.parse(body).results;
  if (error) { console.log(error); }
  for (const i in response) {
    for (const j in response[i].characters) {
      if (response[i].characters[j].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
