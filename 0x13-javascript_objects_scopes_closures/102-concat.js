#!/usr/bin/node

const theArgs = process.argv.slice(2);
const myFile = require('fs');
const file1 = myFile.readFileSync('./' + theArgs[0]);
const file2 = myFile.readFileSync('./' + theArgs[1]);
myFile.writeFileSync('./' + theArgs[2], file1 + file2);
