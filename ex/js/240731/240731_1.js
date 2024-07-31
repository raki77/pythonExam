
// Uncaught SyntaxError: Unexpected identifier 'i'
// > for (let i in "abc") { console.log(i)}
// 0
// 1
// 2
// undefined
// > for (let i of "abc") { console.log(i) }
// a
// b
// c
// undefined
// > for (let i of "12345") { console.log(i+1) }
// 11
// 21
// 31
// 41
// 51
// undefined
// > for (let i of "12345") { console.log(Number(i)+1) }
// 2
// 3
// 4
// 5
// 6
// undefined
// > typeof([1,'a'])
// 'object'
// >
// > let arr = [1, 'a']
// undefined
// > arr[0]
// 1
// > arr[1]
// 'a'
// >
// > let num = 1
// undefined
// > ;
// undefined
// > while (num < 5) { console.log(num); num=num+1 }
// 1
// 2
// 3
// 4
// 5
// > while (num < 5) { console.log(num); num++; }
// undefined
// > while (num < 5) { console.log(num); num++ }
// undefined
// > let num = 1
// Uncaught SyntaxError: Identifier 'num' has already been declared
// > while (num < 5) { console.log(num); num++; }
// undefined
// > let num2 = 1;
// undefined