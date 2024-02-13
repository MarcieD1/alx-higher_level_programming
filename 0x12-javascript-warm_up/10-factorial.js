#!/usr/bin/node

// Define the factorial function recursively
function factorial(n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }
  // Recursive case: factorial of n is n multiplied by factorial of n-1
  return n * factorial(n - 1);
}

// Get the argument passed to the script and convert it to an integer
const arg = parseInt(process.argv[2], 10);

// Check if the argument is a valid integer
if (Number.isNaN(arg)) {
  // eslint-disable-next-line no-console
  console.log(1);
} else {
  // Call the factorial function and print the result
  const result = factorial(arg);
  // eslint-disable-next-line no-console
  console.log(result);
}
