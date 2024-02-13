#!/usr/bin/node

// Get the arguments passed to the script
// eslint-disable-next-line no-console
const args = process.argv.slice(2);

// Check the number of arguments
// eslint-disable-next-line no-console
if (args.length <= 1) {
  // Not enough arguments passed
  // eslint-disable-next-line no-console
  console.log(0);
} else {
  // Convert arguments to integers and sort them in ascending order
  // eslint-disable-next-line no-console
  const numbers = args.map(Number).sort((a, b) => a - b);

  // Print the second largest number
  // eslint-disable-next-line no-console
  console.log(numbers[numbers.length - 2]);
}
