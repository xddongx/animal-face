var express = require('express')
, router = express.Router()
, face_result = require('./face_result');

router.get('/', function(req, res, next){
    console.log('load face page');
    res.render('./face/face.ejs');
});

router.use('/result', face_result);

module.exports = router;