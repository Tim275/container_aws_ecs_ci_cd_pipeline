const express = require('express');
const app = express();
const hostname = '127.0.0.1'; // Your server IP address
const port = 3000;
const version = '3.0.0';

app.get('/', (req, res) => {
    // Set response content    
    res.send(`<html>
                <body>
                    <h1 style="color:blue;text-align: center;">[Version ${version}]: This is AMAZING!!! Like & Subscribe!</h1>
                    <div style="text-align: center;">
                        <img src="https://picsum.photos/400/400?random=1" style="margin-top: 20px;">
                    </div>
                </body>
              </html>`);

    console.log(`[Version ${version}]: New request => http://${hostname}:${port}` + req.url);
})

app.listen(port, () => {
    console.log(`[Version ${version}]: Server running at http://${hostname}:${port}/`);
})