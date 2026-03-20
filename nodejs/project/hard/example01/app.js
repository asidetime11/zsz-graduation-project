const express = require('express');
const path = require('path');
const routes = require('./routes');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true }));
app.use((req, res, next) => {
    req.user = {
        id: req.headers['x-user-id'] || 'u-101',
        role: req.headers['x-user-role'] || 'analyst'
    };
    next();
});
app.use('/', routes);

const port = process.env.PORT || 3101;
app.listen(port, () => {
    console.log(`example01 running on ${port}`);
});
