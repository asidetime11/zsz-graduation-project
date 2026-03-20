const express = require('express');
const path = require('path');
const routes = require('./routes/index');

const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use((req, res, next) => {
    req.currentAgent = { id: 2, role: 'agent' };
    next();
});

app.use('/', routes);

app.listen(3201, () => {
    console.log('example01 running on 3201');
});
