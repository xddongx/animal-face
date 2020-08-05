var express = require('express')
, router = express.Router();

router.get('/', function(req, res, next){
    console.log('load logout page');
    res.render('./accounts/logout.ejs');
});

module.exports = router;