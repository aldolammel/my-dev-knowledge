

// FUNCTION: BASIC

// Define the function
function addNumbers(a, b) {
    return a + b;
}
// Call the function
let result = addNumbers(5, 3);
// Output: 8
console.log(result);



// Other example with params/args:
function greet(name) {
    return "Hello, " + name + "!";
}
// Defining var:
let greeting = greet("Alice");
// Output: "Hello, Alice!
console.log(greeting);



// Another but without args:
function greetSimple() {
    return "Hello, dude!";
};



// ARROW FUNCTION (MODERN JS)
const addNumbers = (a, b) => a + b;
// Output: 6
console.log(addNumbers(2, 4));