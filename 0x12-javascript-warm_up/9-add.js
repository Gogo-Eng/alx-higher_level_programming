#!/usr/bin/node
function add (a, b) {
  a = Number(process.argv[2]);
  b = Number(process.argv[3]);

  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = a + b;
    console.log(Number(sum));
  }
}

add();
