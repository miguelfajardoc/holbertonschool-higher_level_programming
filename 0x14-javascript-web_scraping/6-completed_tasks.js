#!/usr/bin/node

const req = require('request');
const path = process.argv[2];
const todos = {};

req(path, function (error, respond, body) {
  const tareas = JSON.parse(body);
  if (error) { console.log(error); }
  for (const i in tareas) {
    if (tareas[i].completed === true) {
      const n = tareas[i].userId;
      if (n in todos) {
        todos[tareas[i].userId]++;
      } else {
        todos[tareas[i].userId] = 1;
      }
    }
  }
  console.log(todos);
});
