#!/usr/bin/node
//search second biggest arg in a list of passed argv

(function () {
  if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const sorting = process.argv.sort();
    console.log(sorting.reverse()[1]);
  }
})();
