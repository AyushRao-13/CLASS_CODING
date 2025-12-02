const fs = require('fs').promises;

async function readFile() {
  try {
    const data = await fs.readFile('a.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}

readFile();
