// 1 ~ 10 찍기
// for(초;조;증) {
// for(let i=0; i<=5; i++) {
//     console.log(i);
// }

// 누적합
tot = 0;
for(let i=1; i<= 10; i++) {
    tot += i;
}
console.log("tot : " + tot);

// 홀짝 
for(let i=1; i<= 10; i++) {
    if(i%2== 0) {
        console.log(`${i}는 짝수`);
    }
    else {
        console.log(`${i}는 홀수`);
    }
} 

// 구구단
for (i=1 ; i<= 9; i++) {
    for(j=1 ; j<=9; j++) {
        console.log(`${i} * ${j} = ${i*j}`);
    }
    console.log("");
}

// 별찍기
for(let i=1; i<7; i++) {
    let result = "";
    for(let j=1; j<i ; j++) {         
        result += "*"
    }
    console.log(result)
}

// 배열을 반복문으로 돌리기
let arr = ['apple', 'banana', 'candy']; 
for(let i=0 ; i < arr.length ; i++) {
    console.log(arr[i]);
}
for (let i in arr) {
    console.log(arr[i]);
}
for (let j of arr) {
    console.log(j);
}
