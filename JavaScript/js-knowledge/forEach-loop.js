/*

    FOREACH() LOOP

    Purpose: ....... Execute a function for each array element;
    Returns: ....... undefined (always);
    Early Exit: .... No way to break/stop;
    Use Case: ...... When you need to perform an action on every element;

    Traditional For() loop method:
        /JavaScript/for.js

    Some() loop method:
        /JavaScript/some.js

    Find() method:
        /JavaScript/find.js
*/

const numbers = [1, 2, 3, 4, 5];

// Execute code for every element
numbers.forEach((num, index) => {
    console.log(`Index ${index}: ${num * 2}`);
});
// Output: Index 0: 2, Index 1: 4, Index 2: 6, Index 3: 8, Index 4: 10
// Returns: undefined


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


const myArray = ['apple', 'banana', 'orange'];

// Basic syntax
myArray.forEach(function (item, index, array) {
    console.log(item, index);
});

// Using arrow function (more modern)
myArray.forEach((item, index) => {
    console.log(`Item at position ${index}: ${item}`);
});

// One-liner for simple operations
myArray.forEach(item => console.log(item));


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// ARRAY DESTRUCTURING / DESTRUCTURING ASSIGNMENT:
// In Python, this is called as "dictionary unpacking" or "tuple unpacking" but in JavaScript
//  the concept is called "Array Destructuring":

// Object
const myObj = { name: 'John', age: 30, city: 'New York' };

// Using Object.entries() with destructuring assignment
for (const [key, value] of Object.entries(myObj)) {
    console.log(`Key: ${key}, Value: ${value}`);
}

// Another:
// Array destructuring
const [first, second] = [1, 2];

// Object destructuring  
const { name, age } = { name: 'John', age: 30 };

// In function parameters
function processEntry([key, value]) {
    console.log(key, value);
}