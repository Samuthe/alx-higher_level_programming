#!/usr/bin/node

(function () {
  const arg1 = 'X';
  if (isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      // if (parseInt(process.argv[2]) === arg1){
      console.log(arg1.repeat(parseInt((process.argv[2]))));
    }
  }
})();
