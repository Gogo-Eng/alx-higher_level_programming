function factorial(firstArg) {
    firstArg = Number(process.argv[2]);

    if (isNaN(firstArg)) { // Check if firstArg is NaN
        return 'NaN'; // Return 'NaN' if firstArg is not a number
    }

    if (firstArg < 0) { // Check if firstArg is negative
        return 'NaN'; // Return 'NaN' if firstArg is negative
    }

    let result = 1;
    for (let i = 2; i <= firstArg; i++) {
        result *= i;
    }
    return result;
}

console.log(factorial());
