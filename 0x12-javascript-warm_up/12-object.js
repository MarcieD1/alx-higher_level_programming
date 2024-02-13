#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
};
// eslint-disable-next-line no-console
console.log(myObject);

myObject.value = 89;
// eslint-disable-next-line no-console
console.log(myObject);
