// read-async.js
const fs = require('fs');
fs.readFile('./hello.txt', 'utf8', (err, data) => {
  if (err) return console.error('Error reading', err);
  console.log('File says:', data);
});
console.log('Read initiated');
// You will see "Read initiated" before file contents because it's async.
