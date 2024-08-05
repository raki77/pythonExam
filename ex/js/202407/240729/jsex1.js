/*
    "hi"
    console.log("hi1");
    console.log("hi1");
    console.log("hi1");

    //REPL 을 사용한 출력
    //찍고 돌리고, 루프

    > typeof(1)
    'number'
    > typeof(1.34)
    'number'
    > typeof('a')
    'string'
    > typeof('abcde')
    'string'
    >
    > typeof(true)
    'boolean'
    > typeof(false)
    'boolean'
    > 2**3
    8
    > 5%3
    2
    >
    > "hello"[1]
    'e'
    > "hello"[-1]
    undefined
    > `52 + 273 = ${52+273}`
    '52 + 273 = 325'
    >

    > Date()
    'Mon Jul 29 2024 16:13:28 GMT+0900 (대한민국 표준시)'  
    '생성자, 앞 대문자 ()'
    > date = Date()
    'Mon Jul 29 2024 16:14:19 GMT+0900 (대한민국 표준시)'
    > date
    'Mon Jul 29 2024 16:14:19 GMT+0900 (대한민국 표준시)'
    > new Date()
    2024-07-29T07:15:47.760Z
    > date2 = new Date()
    2024-07-29T07:15:55.239Z
    > date2.getFullYear
    [Function: getFullYear]
    > date2.getFullYear()
    2024

    > `올해는 ${date2.getFullYear()}년`
    '올해는 2024년'
    >

    > 1 == 1
    true
    > 1 != 2
    true 
    > true && true
    true
    > true && false
    false
    > false  && true
    false
    > false && false
    false
    >
    >
    > true || true
    true
    > true || false
    true
    > false || true
    true
    > false || false
    false
    >
    > ! true
    false
    > ! false
    true
    > !!true
    true
    > !!false
    false
    >

    > new Date().getHours()
    16
    > (new Date()).getHours()
    16
    > num1 = 5
    5
    > let pi;
    Uncaught SyntaxError: Identifier 'pi' has already been declared
    >
    >
    > pi = 3.14159265;
    3.14159265
    >
    >
    > let num2 ;
    undefined
    > typeof(num2)
    'undefined'
    > let num3 = 6;
    undefined
    > typeof(num3)
    'number'
    > 'undefined 자료형이 따로 하나가 있다'
    'undefined 자료형이 따로 하나가 있다'
    >

    > typeof({})
    'object'
    > typeof(log)
    'undefined'
    > typeof(console)
    'object'  // 이 세상 모든 것

    // dictionary 구조 , 키벨류
    > typeof(console.log)
    'function'
    >

    

    > 'hi'+4
    'hi4'
    > 'hi'+4.7
    'hi4.7'
    > 1+4.7
    5.7
    > Number('5')
    5
    > typeof('5')
    'string'
    > typeof(Number('5'))
    'number'
    >

    > typeof(String(5))
    'string'
    > typeof(String(5.4))
    'string'
    > boolean(0)
    Uncaught ReferenceError: boolean is not defined
    > Boolean(0)
    false
    > Boolean(1)
    true
    > Boolean('hi')
    true
    > Boolean('')
    false
    > Boolean(' ')
    true
    > Boolean({})
    true
    > Boolean(0.0)
    false
    > Boolean([])
    true
    > Boolean(null)
    false
    >



    >
    > Number(false)
    0
    > Number(true)
    1
    > Number("hi")
    NaN
    >
    > isNaN(Number("hi"))
    true
    > typeof(null)
    'object'
    > typeof(NaN)
    'number'
    > typeof(undefined)
    'undefined'
*/


let array = [52, 273, 32, 93, 103];

// for(let element of array) {
//     console.log(element);
// }

for(let element in array) {
    console.log(array[element]);
}