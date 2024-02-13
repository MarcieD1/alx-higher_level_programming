#!/usr/bin/node

// Define the add function that takes two integers as arguments
function add(a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
// eslint-disable-next-line no-console
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
// eslint-disable-next-line no-console
if (isNaN(arg1) || isNaN(arg2)) {
  console.log("NaN");
} else {
  // Call the add function and print the result
  // eslint-disable-next-line no-console
  const result = add(arg1, arg2);
  console.log(result);
}
