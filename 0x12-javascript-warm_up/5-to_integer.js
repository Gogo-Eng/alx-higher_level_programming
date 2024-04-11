#!/usr/bin/node

const firstArgument = process.argv[2];
if (!Number(firstArgument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(firstArgument)}`);
}
