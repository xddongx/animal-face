// EXpress 기본 모듈 불러오기
var express = require('express'), path = require('path');

// Express 미들웨어 불러오기
var bodyParser = require('body-parser')
, static = require('serve-static')
, cookieParser = require('cookie-parser')
, errorHandler = require('errorhandler')
, routes = require('./routes/index');

// 에러 핸들러 모듈 사용
var expressErrorHandler = require('express-error-handler');

// Session 미들웨어 불러오기
var expressSession = require('express-session');

// 설정 모듈 불러오기
var config = require('./config');


// 익스프레스 객체 생성
var app = express();

// =======서버 변수 설정 및 static으로 [public] 폴더 설정 =====//
console.log('config.server_port : %d', config.server_port );
app.set('port', process.env.PORT || config.server_port);

// body-parser를 사용해 application/x-www-form-urlencode 파싱
app.use(bodyParser.urlencoded({ extended: true}));

// app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

// public 폴더를 static으로 오픈
app.use('/public', static(path.join(__dirname, 'public')));

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
// app.use(expressSession({
//     secret: 'my key',
//     resave:true,
//     saveUninitialized:ture
// }));

// 404 에러 페이지 처리
// var errorHandler = expressErrorHandler({
//     static:{
//         '404': './public/404.html'
//     }
// });

// app.use(expressErrorHandler.httpError(404));
// app.use(errorHandler);






// =======서버 시작 ========//
process.on('SIGTERM', function(){
    console.log('프로세스가 종료됩니다.');
    app.close();
});

app.on('close', function(){
    console.log('Express 서버 객체가 종료 됩니다.');
    if (databse.db){
        database.db.close();
    }
});

app.use(routes);

// 기본 포트를 app 객체에 속성으로 설정
app.listen(app.get('port'), function(){
    console.log('express 서버를 시작했습니다. : ' + app.get('port'));
});



