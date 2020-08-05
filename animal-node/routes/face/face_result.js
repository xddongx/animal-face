var express = require('express')
, router = express.Router();

router.get('/', function(req, res, next){
    console.log('load face result page');
    res.render('./face/face_result.ejs');
});

module.exports = router;