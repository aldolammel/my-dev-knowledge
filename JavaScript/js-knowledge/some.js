/*

    SOME() LOOP

    Purpose: ....... Test if at least one element passes a condition;
    Returns: ....... boolean;
    Early Exit: .... Stops immediately when condition is met;
    Use Case: ...... When you need to check if any element meets criteria;

    Traditional For() loop method:
        /JavaScript/for.js

    Find() method:
        /JavaScript/find.js

    ForEach() loop method:
        /JavaScript/forEach-loop.js
*/


const numbers = [1, 2, 3, 4, 5];
// Check if any number is greater than 3
const hasLargeNumber = numbers.some(num => {
    console.log(`Checking ${num}`);
    return num > 3;
});
// Output: Checking 1, Checking 2, Checking 3, Checking 4
// Returns: true (stops at 4, doesn't check 5)


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// IMPORTANT: if you wanna know what is the element found, use find() method!