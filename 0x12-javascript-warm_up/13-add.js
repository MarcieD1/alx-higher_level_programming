#!/usr/bin/node

// Define the function add that takes two integers as arguments and returns their sum
function add(a, b) {
  return a + b;
}

// Export the add function to make it visible from outside
module.exports = {
  add,
};
