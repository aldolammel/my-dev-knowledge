

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