var express = require('express');
var router = express.Router();

var async = require('async');

router.get('/', function(req, res, next) {
  res.render('deploy', {});
});

module.exports = router
