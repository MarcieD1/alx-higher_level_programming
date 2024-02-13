#!/usr/bin/node

// Get the first argument passed to the script
// eslint-disable-next-line no-console
const arg = process.argv[2];

// Check if the argument can be converted to an integer
// eslint-disable-next-line no-console
const size = parseInt(arg, 10);

// Check if the conversion was successful and the size is a positive number
// eslint-disable-next-line no-console
if (Number.isNaN(size) || size <= 0) {
  // Invalid size
  // eslint-disable-next-line no-console
  console.log('Missing size');
} else {
  // Print the square
  // eslint-disable-next-line no-console
  for (let i = 0; i < size; i += i) {
    let row = '';
    for (let j = 0; j < size; j += j) {
      row += 'X';
    }
    // eslint-disable-next-line no-console
    console.log(row);
  }
}
