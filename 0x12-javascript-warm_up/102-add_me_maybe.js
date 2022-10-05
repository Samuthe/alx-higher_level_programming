#!/usr/bin/node

const addMeMaybe = function (number, theFunction) {
  return theFunction(number + 1);
};

exports.addMeMaybe = addMeMaybe;
