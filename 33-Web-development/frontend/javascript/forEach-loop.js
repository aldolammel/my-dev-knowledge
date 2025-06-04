

// FOREACH LOOP:


const myArray = ['apple', 'banana', 'orange'];

// Basic syntax
myArray.forEach(function(item, index, array) {
    console.log(item, index);
});

// Using arrow function (more modern)
myArray.forEach((item, index) => {
    console.log(`Item at position ${index}: ${item}`);
});

// One-liner for simple operations
myArray.forEach(item => console.log(item));



// ARRAY DESTRUCTURING / DESTRUCTURING ASSIGNMENT:
// In Python, this is called as "dictionary unpacking" or "tuple unpacking" but in JavaScript
//  the concept is called "Array Destructuring":

// Object
const myObj = {name: 'John', age: 30, city: 'New York'};

// Using Object.entries() with destructuring assignment
for (const [key, value] of Object.entries(myObj)) {
    console.log(`Key: ${key}, Value: ${value}`);
}

// Another:
// Array destructuring
const [first, second] = [1, 2];

// Object destructuring  
const {name, age} = {name: 'John', age: 30};

// In function parameters
function processEntry([key, value]) {
    console.log(key, value);
}