const express = require('express');
const path = require('path');
const routes = require('./routes');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/', routes);

const port = process.env.PORT || 3102;
app.listen(port, () => console.log(`example02 running on ${port}`));
