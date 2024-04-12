#!/usr/bin/node
let i, j;
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(x); i++) {
    let row = 'l';
    for (j = 0; j < 4; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
