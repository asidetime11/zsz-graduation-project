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

app.use((req, res, next) => {
    res.cookie('session_id', 'policy-session-1', { httpOnly: true });
    next();
});

app.use('/', routes);

app.listen(3204, () => {
    console.log('example04 running on 3204');
});
