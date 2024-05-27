#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const valueAtIndex = list[i];
    result.push(valueAtIndex);
  }
  return result;
};
