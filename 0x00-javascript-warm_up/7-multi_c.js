#!/usr/bin/node

if (process.argv[2] && Number(process.argv[2])) {
  for (let x = 0; x < Number(process.argv[2]); x++) {
    console.log('C is fun');
  }
}