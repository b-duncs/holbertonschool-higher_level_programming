#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max = Number(process.argv[2]);
  let int = Number(process.argv[3]);
  for (let i = 0; i < process.argv.length; i++) {
    if (max < Number(process.argv[i + 1])) {
      int = max;
      max = Number(process.argv[i + 1]);
    } else if (Number(process.argv[i + 1] > int) && Number(process.argv[i + 1]) < max) {
      int = Number(process.argv[i + 1]);
    }
  }
  console.log(int);
}
