// 홀짝프로그램
// for (let i=0; i < 50; i++) {
//     if(i%2 == 0) {
//         console.log("짝수");
//     }
//     else {
//         console.log("홀수");
//     }
// }

// window 객체가 최상위
// JS -> 
// *** BOM (Browser Object Model), DOM (Document Object Model)
// node : 점, 위치

//let score = window.prompt("input score (");
// let score = 100;
// let res = Math.floor(score/10);
// switch (res) {
//     case 10: console.log("A"); break;
//     case 9: console.log("A"); break;
//     case 8: console.log("B"); break;
//     case 7: console.log("C"); break;
//     case 6: console.log("D"); break;
//     case 5: console.log("E"); break;    
//     default:
//         console.log("F"); 
//         break;
// }

// let menu = 1;
// switch (menu) {
//     case 1: console.log("짜 선택"); break;
//     case 2: console.log("짬 선택"); break;
//     case 3: console.log("볶음밥 선택"); break;
//     case 4: console.log("탕수육 선택"); break;    
//     default: console.log("4가지 중에 선택하시오."); break;
// }

let youNum = 1;
switch(youNum) {
    case 1: console.log("입금"); break;
    case 2: console.log("출금"); break;
    case 3: console.log("이체"); break;
    case 4: console.log("조회"); break;    
    default: console.log("1-4중에 선택하시오."); break;
}


