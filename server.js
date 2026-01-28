const express = require('express');
const crypto = require('crypto');
const app = express();
const port = 8080;

app.get('/', (req, res) => {
    res.send("Serwer JS działa! Spróbuj mnie powalić na /heavy.");
});

app.get('/heavy', (req, res) => {
    let data = "some_random_data_to_hash";
    
    // Symulacja pracy: haszowanie
    for (let i = 0; i < 100_000; i++) {
        data = crypto.createHash('sha256').update(data).digest('hex');
    }

    res.send(`Operacja zakończona. Wynik: ${data.substring(0, 10)}...`);
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Serwer JS nasłuchuje na http://0.0.0.0:${port}`);
    console.log("UWAGA: Node.js jest jednowątkowy. /heavy zablokuje cały serwer!");
});