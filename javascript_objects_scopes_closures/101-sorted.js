#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.entries(dict);
const keys = [];
for (const data of newDict) keys.push(data[1]);

const uniqueKey = [...new Set(keys)];
const values = [];

for (let i = 0; i < uniqueKey.length; i++) {
  const list = [];
  for (const [index, value] of newDict) {
    if (value === uniqueKey[i]) list.push(index);
  }
  values.push(list);
}

const dictionary = {};
for (let i = 0; i < uniqueKey.length; i++) {
  dictionary[uniqueKey[i]] = values[i];
}

console.log(dictionary);
