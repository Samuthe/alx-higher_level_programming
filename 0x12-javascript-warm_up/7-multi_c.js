#!/usr/bin/node

(function (arg) {
  arg = 'C is fun';
  if (isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
  } else {
    for (let x = 0; x < parseInt(process.argv[2]); x++) {
      console.log(arg);
    }
  }
})();
