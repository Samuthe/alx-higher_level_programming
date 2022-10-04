#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));

// (function (n) {
//   if (isNaN(n) || n === 1) {
//     return 1;
//   } else {
//     return n * (n - 1);
//   }
// })
// console.log((parseInt(process.argv[2])));
