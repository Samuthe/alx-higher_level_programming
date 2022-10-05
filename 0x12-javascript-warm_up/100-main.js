#!/usr/bin/node

const { upDate } = require('./100-let_me_const');

myVar = 89;
require('./100-let_me_const');
upDate();
console.log(myVar)