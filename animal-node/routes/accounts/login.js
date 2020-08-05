var express = require('express')
, router = express.Router();

router.get('/', function(req, res, next){
    console.log('load login page');
    res.render('./accounts/login.ejs');
});

module.exports = router;