#!/usr/bin/node

(function () {
  if (process.argv.length === 2) {
    console.log('Argument found');

  } else if (process.argv.length === 3) {
    console.log('Arguments found');

  } else {
    console.log('No argument');
  }
  
})();
