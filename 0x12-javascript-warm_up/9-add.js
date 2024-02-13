#!/usr/bin/node

// Define the add function that takes two integers as arguments
function add(a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
// eslint-disable-next-line no-console
const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

// Check if both arguments are valid integers
// eslint-disable-next-line no-console
if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
  // eslint-disable-next-line no-console
  console.log('NaN');
} else {
  // Call the add function and print the result
  // eslint-disable-next-line no-console
  const result = add(arg1, arg2);
  // eslint-disable-next-line no-console
  console.log(result);
}
