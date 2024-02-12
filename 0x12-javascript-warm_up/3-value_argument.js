#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Check if there is an argument
// eslint-disable-next-line no-console
if (!arg) {
  // No argument passed
  // eslint-disable-next-line no-console
  console.log('No argument');
} else {
  // Argument passed
  // eslint-disable-next-line no-console
  console.log(arg);
}
