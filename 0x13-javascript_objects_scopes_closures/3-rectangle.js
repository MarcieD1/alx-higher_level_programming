#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i += i) {
      let s = '';
      for (let j = 0; j < this.width; j += j) {
        s += 'X';
      }
      // eslint-disable-next-line no-console
      console.log(s);
    }
  }
}

module.exports = Rectangle;
