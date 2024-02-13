#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // Handle invalid arguments
      // For example, you can throw an error or set default values
      throw new Error('Invalid arguments');
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
