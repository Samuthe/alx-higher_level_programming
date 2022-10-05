#!/usr/bin/node

// (function () {
//   if (process.argv.length <= 3) {
//     console.log(0);
//   } else {
//     const sorting = process.argv.sort();
//     console.log(sorting.reverse()[1]);
//   }
// })();

// function factorization () {
//   if (process.argv.length <= 3) {
//     console.log(0);
//   } else {
//     const sorting = process.argv.sort();
//     console.log(sorting.reverse()[1]);
//   }
// }
// factorization();

// if (process.argv.length <= 3) {
//   console.log(0);
// } else {
//   // const sorting = process.argv.sort();
//   console.log(process.argv.sort().reverse()[1]);
// }

const list = process.argv;
if (list.length <= 3) {
  console.log(0);
} else {
  console.log(list.sort((x, y) => y - x).slice(3)[0]);
}
