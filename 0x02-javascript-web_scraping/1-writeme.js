#!/usr/bin/node

const filePath = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, string, (err, data) => {
  if (err) {
    console.error(err);
  }
});
