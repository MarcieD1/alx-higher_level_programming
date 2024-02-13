#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    let result = '';
    while (number > 0) {
      const remainder = number % base;
      result = String.fromCharCode(remainder + (remainder < 10 ? 48 : 87)) + result;
      number = Math.floor(number / base);
    }
    return result;
  };
};
