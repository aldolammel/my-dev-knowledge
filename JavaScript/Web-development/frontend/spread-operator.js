/* 
    
    SPREAD OPERATOR:
    The spread operator "..." in JavaScript expands an iterable (like an array, string, or object)
    into individual elements. It is commonly used for. It also simplifies code, improves
    readability, and helps avoid unintended side effects by creating copies instead of modifying 
    original data structures.

*/


// Spread Operator fixes this kind of issue:
const oldBox = [a, b, c];
const newBox = oldBox;  // It's NOT creating a copy but a reference.
newBox.push(d);  // adding a "d" to the array.
console.log(oldBox);  // Output: [a, b, c, d] because newBox is just a reference to the oldBox.



// Copying arrays and objects: Creating shallow copies of arrays or objects:
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray]; // [1, 2, 3]
copiedArray.push(4);
console.log(originalArray);  // [1, 2, 3]

const originalObject = { a: 1, b: 2 };
const copiedObject = { ...originalObject }; // { a: 1, b: 2 }



// Combining arrays: Merging multiple arrays into a single array:
const array1 = [1, 2];
const array2 = [3, 4];
const combinedArray = [...array1, ...array2]; // [1, 2, 3, 4]



// Adding elements to arrays: Inserting elements into an existing array:
const array = [1, 2, 3];
const newArray = [...array, 4, 5]; // [1, 2, 3, 4, 5]



// Passing arguments to functions: Passing multiple arguments to a function that expects individual parameters:
function sum(a, b, c) {
    return a + b + c;
}
const numbers = [1, 2, 3];
const result = sum(...numbers); // 6



// Spreading strings: Converting a string into an array of individual characters:
const str = "hello";
const charArray = [...str]; // ['h', 'e', 'l', 'l', 'o']
