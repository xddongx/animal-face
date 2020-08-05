// 모듈 불러오기
var express = require('express')
, router = express.Router()
, admin = require('./admin')
, login = require('./accounts/login')
, logout = require('./accounts/logout')
, face = require('./face/face')
, face_result = require('./face/face_result');

// main page router
router.get('/', function(req,res, next){
    console.log('load main page');
    res.render('main.ejs', {title:'ss'});
});

router.use('/admin', admin);
router.use('/login', login);
router.use('/logout', logout);
router.use('/face', face);
// router.get('/face/result', face_result);


module.exports = router;