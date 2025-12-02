const path = require('path');
const filePath = path.join(__dirname, 'data', 'notes.txt');
console.log('Full path:', filePath);
console.log('Base name:', path.basename(filePath));
