#!/usr/bin/node
let i;
const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < Number(x); i++) {
    console.log('C is fun');
  }
}
