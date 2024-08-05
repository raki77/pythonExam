// 이벤트 방식 - 콜백방식
// setTimeout(함수, 시간)
// setInterval(함수, 시간)

// 익명 함수
// > p1 = function() { console.log("hi2"); }
// [Function: p1]
// > setTimeout
// [Function: setTimeout] {
//   [Symbol(nodejs.util.promisify.custom)]: [Getter]
// }
// > setTimeout(p1, 3000)
// Timeout {
//   _idleTimeout: 3000,
//   _idlePrev: [TimersList],
//   _idleNext: [TimersList],
//   _idleStart: 79176,
//   _onTimeout: [Function: p1],
//   _timerArgs: undefined,
//   _timerArgs: undefined,
//   _timerArgs: undefined,
//   _timerArgs: undefined,
//   _repeat: null,
//   _destroyed: false,
//   [Symbol(refed)]: true,
//   [Symbol(kHasPrimitive)]: false,
//   [Symbol(asyncId)]: 196,
//   [Symbol(triggerId)]: 6
// }
// > ;
// undefined
// > hi2
// >

p1 = function () {
    console.log("111");
}
setInterval(p1,3000)
