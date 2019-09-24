#!/usr/bin/node

const fs = require('request');
const path = 'http://swapi.co/api/films/' + process.argv[2];

fs(path, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
      console.log(JSON.parse(body)['title'])
  }
});
