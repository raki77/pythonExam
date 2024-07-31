let array = [273,52,103,57,271];
let min = Number.MAX_VALUE;
let max = Number.MIN_VALUE;

if(array.length > 0) {
    mid = ((array.length/2) > 2)? Number(array.length/2): array.length;
    mid = Math.floor(mid); 
   // job1 
   for(let i = 0; i < mid; i++) {
        if (i == 0) {
            max = array[i];
            min = array[i]; 
        }
        else { 
            if(max < array[i]) {
                max = array[i]; 
            }
            if(min > array[i]) {
                min = array[i]; 
            }
        }
    }       
    // job2
    for(let j = mid; j < array.length; j++) {
        if(max < array[j]) {
            max = array[j]; 
        }
        if(min > array[j]) {
            min = array[j]; 
        }
    } 
}
 
console.log(`가장 큰 수: ${max}`);
console.log(`가장 작은 수: ${min}`);
