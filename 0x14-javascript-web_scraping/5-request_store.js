#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const path = process.argv[2];

req(path, function (error, respond, body) {
  if (error) { console.log(error); }
  fs.writeFile(process.argv[3], body, 'utf-8', (error) => { if (error) { console.log(error); } });
});
