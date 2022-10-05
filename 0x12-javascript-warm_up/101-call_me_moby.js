#!/usr/bin/node
//a funct that executes itself a number of times
callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};

// function callMeMoby(x, theFunction){
//   if (x > 0){
//     theFunction();
//     x--
//   }
// }

exports.callMeMoby = callMeMoby;
