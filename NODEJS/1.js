//console.log("hello world");

const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`<!DOCTYPE html>
<html>
<head>
    <title>Simple Page with Buttons</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background-color: #f5f5f5;
        }

        h1 {
            color: #333;
        }

        .btn {
            padding: 12px 25px;
            font-size: 16px;
            margin: 10px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        .btn1 {
            background-color: #4CAF50;
            color: white;
        }

        .btn2 {
            background-color: #2196F3;
            color: white;
        }

        .btn:hover {
            opacity: 0.8;
        }
    </style>
</head>

<body>
    <h1>Simple HTML Page</h1>

    <button class="btn btn1">Button 1</button>
    <button class="btn btn2">Button 2</button>

</body>
</html>
`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
