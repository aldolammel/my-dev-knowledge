// JavaScript "String Interpolation" Examples
// On Python language, it's similar the 'F-Strings' concept.


const name = "Alice";
const age = 25;
// Using template literals (backticks)
const greeting = `Hello, my name is ${name} and I am ${age} years old.`;
console.log(greeting);
// Output: Hello, my name is Alice and I am 25 years old.



// You can perform calculations inside the interpolation - - - - - - - - - - - - - - - - - - - - - -
const totalMessage = `The ${product} costs $${price}, and with tax (${tax * 100}%) the total is $${(price * (1 + tax)).toFixed(2)}.`;
console.log(totalMessage);
// Output: The laptop costs $999.99, and with tax (8%) the total is $1079.99.



// Interpolation with function calls - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
function getCurrentTime() {
    return new Date().toLocaleTimeString();
}
const timeMessage = `Current time is: ${getCurrentTime()}`;
console.log(timeMessage);
// Output: Current time is: [current time]