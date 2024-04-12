#!/usr/bin/node
function factorial (firstArg) {
  if (firstArg < 0) {
    return NaN;
  }

  if (isNaN(firstArg)) {
    return 1;
  }

  if (firstArg === 1) {
    return firstArg;
  }
  return firstArg * factorial(firstArg - 1);
}
const input = Number(process.argv[2]);
console.log(factorial(input));
