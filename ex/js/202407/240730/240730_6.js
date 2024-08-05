//import 'repl'
//const repl=require('repl');
//import repl from 'repl';

repl.start({
    prompt:"입력",
    eval: (command, context, filename, callback) => {
        let number = Number(command);
        // 입력이 숫자인지 확인 합니다.
        if(isNaN(number)) {
            console.log("Not number");
        }
        else {
            console.log("is number");
        }
        // 처리완료
        callback();
    }
});
console.log(repl);
