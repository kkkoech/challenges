/*
Given the array below, write a function to sum all the numeric elements, including sub-arrays. The solution should work for arbitrary depth of sub-arrays.

var arr = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]]
*/


var nestedArr = ['a', 1, 2, [3, 'b', 4, [5, 6, 'c']], 'd', 7, [8, 9]];

function flattenArray(arr){
    var flattenedArr = [];
    for (var i=0; i<arr.length;i++){
        if (typeof arr[i] === 'number') {
            flattenedArr.push(arr[i]);
        } else if (typeof arr[i] === 'object') {
            flattenedArr = flattenedArr.concat(flattenArray(arr[i]));
        }
    }
    return flattenedArr;
}

console.log(flattenArray(nestedArr));
