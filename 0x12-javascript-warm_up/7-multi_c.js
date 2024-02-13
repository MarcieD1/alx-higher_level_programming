#!/usr/bin/node

// Get the first argument passed to the script
// eslint-disable-next-line no-console
const arg = process.argv[2];

// Check if the argument can be converted to an integer
// eslint-disable-next-line no-console
const num = parseInt(arg, 10);

// Check if the conversion was successful
// eslint-disable-next-line no-console
if (Number.isNaN(num)) {
  // Argument is not a number
  // eslint-disable-next-line no-console
  console.log('Missing number of occurrences');
} else {
  // Argument is a number
  for (let i = 0; i < num; i += 1) {
  // eslint-disable-next-line no-console
    console.log('C is fun');
  }
}
