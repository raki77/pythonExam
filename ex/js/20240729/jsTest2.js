
console.log(Boolean(0));
console.log(Boolean(""));
console.log(Boolean(null));
console.log(Boolean(NaN));
console.log(Boolean(undefined));

/*

> 1 == 1
true
> 1 != 1
false
> 1 === 1
true
> 1 === Boolean(888)
false
>
> 1 == Boolean(888)
true

*/

// let x, y;
// if (x>4) {
//     if(y>2) {
//         console.log(x*y);
//     }
// } else {
//     console.log();
// }

// let level = 1;

// switch(level) {
//     case 1:
//         console.log("수강해야 하는 전공 학점: 12학점");    
//         break;
//     case 2:
//         console.log("수강해야 하는 전공 학점: 18학점");    
//         break;
//     case 3:
//         console.log("수강해야 하는 전공 학점: 10학점");    
//         break;
//     case 4:
//         console.log("수강해야 하는 전공 학점: 18학점");    
//         break;
// }

//result = [1,2,3,5,5];
//for (const x of result) {
// for (const idx in result) {
//     console.log("x:" + x);
// }

// for(let i=0 ; i<20 ; i = i+2) {
//     console.log("출력1");    
// }

// cnt = 0
// while(true) {
//     if(cnt >= 10) {
//         break;
//     }
//     console.log("출력2");
//     cnt++;
// }

output = "";
for (let i=0 ; i<9 ;i ++) {
    result = 2*i+1;
    for (let j=0 ; j<16 ;j ++) {
        if(j == result) {
            space = (15-result)/2;
            console.log(space);
            //console.log(" "*space + "*"*j);
            for (let x = 0; x < space; x++) {
                output += " ";
            }
            for (let y = 0; y < j; y++) {
                output += "*";    
            }
                    
        }
        else {
            continue;
        }        
    } 
    output += "\n";
}
console.log(output);  
       
 
