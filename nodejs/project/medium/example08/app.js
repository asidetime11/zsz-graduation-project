const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const routes = require('./routes/index');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cookieParser());

app.use('/', routes);

app.listen(3208, () => {
    console.log('example08 running on 3208');
});
