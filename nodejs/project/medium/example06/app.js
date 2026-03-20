const express = require('express');
const path = require('path');
const routes = require('./routes/index');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use((req, res, next) => {
    req.user = { id: 2, name: 'guest-user' };
    next();
});

app.use('/', routes);

app.listen(3206, () => {
    console.log('example06 running on 3206');
});
