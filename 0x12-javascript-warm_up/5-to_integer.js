#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Check if the argument can be converted to an integer
// eslint-disable-next-line no-console
const number = parseInt(arg, 10);
if (Number.isNaN(number)) {
  // Not a number
  // eslint-disable-next-line no-console
  console.log('Not a number');
} else {
  // Number
  // eslint-disable-next-line no-console
  console.log(`My number: ${number}`);
}
