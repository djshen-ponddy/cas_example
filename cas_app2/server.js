const express = require('express');
const CAS = require('cas-authentication');
const session = require('express-session');

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();

const cas = new CAS({
  cas_url: 'http://172.28.1.1/cas',
  service_url: 'http://172.28.1.3',
  session_info: 'info',
  destroy_session: true
});

app.use(session({
  secret: 'secret',
  resave: false,
  saveUninitialized: true
}));

app.get('/', cas.bounce, (req, res) => {
  res.send(JSON.stringify(req.session['cas_user']) + ', ' + JSON.stringify(req.session['info']));
});

app.get('/logout', cas.logout);

app.listen(PORT, HOST);
