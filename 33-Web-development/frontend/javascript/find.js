/* 
    JAVASCRIPT: 'FIND' METHOD
    This method checks an array and returns the first element that makes the conditional true.
*/

array1 = [5, 12, 8, 130, 44];

const found = array1.find(element => element > 10);

console.log(found);  // Output: 12