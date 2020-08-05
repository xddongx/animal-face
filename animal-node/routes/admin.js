var express = require('express')
, router = express.Router();

router.get('/', function(req, res, next){
    console.log('load admin page');
    res.render('admin.ejs');
});

module.exports = router;