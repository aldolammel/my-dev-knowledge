/*

    FOR() LOOP

    Purpose: ....... General-purpose iteration with full control;
    Returns: ....... Nothing (it's a statement, not a method);
    Early Exit: .... Full control with break, continue;
    Use Case: ...... When you need maximum control over iteration;

    ForEach() loop method:
        /33-Web-development/frontend/javascript/forEach-loop.js

    Some() loop method:
        /33-Web-development/frontend/javascript/some.js

    Find() method:
        /33-Web-development/frontend/javascript/find.js
*/


const numbers = [1, 2, 3, 4, 5];
// Traditional for loop with full control
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 3) {
        console.log('Skipping 3');
        continue; // Skip this iteration
    }
    if (numbers[i] === 4) {
        console.log('Breaking at 4');
        break; // Exit the loop completely
    }
    console.log(`Processing: ${numbers[i]}`);
}
// Output: Processing: 1, Processing: 2, Skipping 3, Breaking at 4


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// Traditional for loop with break support
for (let i = 0; i < array.length; i++) {
    const item = array[i];
    if (condition) {
        // Do your action
        break; // Stops the searching.
    }
    // Continue processing
}