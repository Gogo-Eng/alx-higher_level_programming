#!/usr/bin/node
const allArg = process.argv.length;

if (allArg < 3) {
  console.log('No argument');
} else if (allArg > 3) {
  console.log('Arguments found');
} else if (allArg === 3) {
  console.log('Argument found');
}
