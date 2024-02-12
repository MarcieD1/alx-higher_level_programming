#!/usr/bin/node

// Get the number of arguments passed to the script
const numArgs = process.argv.length - 2;

// Check the number of arguments
if (numArgs === 0) {
  // No arguments passed
  console.log("No argument");
} else if (numArgs === 1) {
  // Only one argument passed
  console.log("Argument found");
} else {
  // More than one argument passed
  console.log("Arguments found");
}
