const express = require('express')
const app = express();
const PORT = process.env.PORT || 3000;
const APP_MESSAGE = process.env.APP_MESSAGE || 'No APP_MESSAGE supplied in env';

app.get('/', (req, res) => {
  res.send(APP_MESSAGE)
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}!`)
});