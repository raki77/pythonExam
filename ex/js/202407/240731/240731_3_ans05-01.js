

// function test(a,b,c) {
//     console.log(a);
//     console.log(a*b);
//     console.log(a*b*c);
// }

// test(10, 100);


// setTimeout(function(){
//     console.log("aaaaaaaaa");
// }, 1000);

// function res3(prm1) {
//     if(typeof(prm1) == 'undefined') {
//         prm1 = 10;
//     }
//     console.log(prm1);
// }
// res3()


// function res2(prm1 = 10) {
//     console.log(prm1);
// }
// res2();

//----------------------------------------------

function power(prm1, prm2) {   
    if(typeof(prm2) == 'undefined') {
        console.log(prm1 * prm1);    
    }
    else {
        console.log(prm1**prm2);
    }
} 
power(2);
power(2,3);


let m_external = this;
//1
console.log(`${m_external == this}`);
//2
(() => {
    console.log(`${m_external == this}`);
})();
//3
(function() {
    console.log(`${m_external == this}`);
})();
//4
function f_name() {
    console.log(`${m_external == this}`);
}
f_name();





