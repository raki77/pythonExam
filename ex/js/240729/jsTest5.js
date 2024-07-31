let array = [52,71,32,103,273,93];   

function selectionSort(arr) {



    let indexMin;
    for (let x = 0; x < arr.length - 1; x++) {
        
        
        indexMin = x;
        for (let y = x + 1; y < arr.length; y++) {
            
            
            if (arr[y] < arr[indexMin]) {
                indexMin = y;
            }

        }


        [arr[x], arr[indexMin]] = [arr[indexMin], arr[x]];



    }
    return arr;


}
console.log(`${selectionSort(array)}`);