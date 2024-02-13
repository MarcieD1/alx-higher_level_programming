#!/usr/bin/node

// Get the arguments passed to the script
// eslint-disable-next-line no-console
const args = process.argv.slice(2);

// Check the number of arguments
// eslint-disable-next-line no-console
if (args.length === 2) {
  // Two arguments passed
  // eslint-disable-next-line no-console
  console.log(`${args[0]} is ${args[1]}`);
} else {
  // Not two arguments passed
  // eslint-disable-next-line no-console
  console.log('Wrong number of arguments');
}
