#!/usr/bin/node

// Get the number of arguments passed to the script
const numArgs = process.argv.length - 2;

// Check the number of arguments
// eslint-disable-next-line no-console
if (numArgs === 0) {
  // No arguments passed
  // eslint-disable-next-line no-console
  console.log('No argument');
} else if (numArgs === 1) {
  // Only one argument passed
  // eslint-disable-next-line no-console
  console.log('Argument found');
} else {
  // More than one argument passed
  // eslint-disable-next-line no-console
  console.log('Arguments found');
}
