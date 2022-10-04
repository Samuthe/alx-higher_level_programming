#!/usr/bin/node

(function () {
  if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const sorting = process.argv.sort();
    console.log(sorting.reverse()[1]);
  }
})();
