  
let array = [52,71,32,103,273,93];   

function merge(leftArr, rightArr) {
    const sortedArr = [];
    let l = 0;
    let r = 0;
  
    while (l < leftArr.length && r < rightArr.length) {
      if (leftArr[l] <= rightArr[r]) {
        sortedArr.push(leftArr[l]);
        l++;
      } else {
        sortedArr.push(rightArr[r]);
        r++;
      }
    } 
    while (l < leftArr.length) {
      sortedArr.push(leftArr[l]);
      l++;
    } 
    while (r < rightArr.length) {
      sortedArr.push(rightArr[r]);
      r++;
    } 
    return sortedArr;
  }
  
  function mergeSort(arr) {
    if (arr.length === 1) {
      return arr;
    }  
    const mid = Math.ceil(arr.length / 2);  
    const leftArr = arr.slice(0, mid);
    const rightArr = arr.slice(mid);  
    return merge(mergeSort(leftArr), mergeSort(rightArr));
  }


  console.log(`${mergeSort(array)}`);