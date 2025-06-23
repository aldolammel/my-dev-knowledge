/*

  STOPPING A LOOP: BREAK

  Stop the loop if the loop condition is reached.

*/


// TRADITIONAL FOR() LOOP:
// More about: /33-Web-development/frontend/javascript/for.js

// Break works to stop the loop:
for (let i = 0; i < array.length; i++) {
    const item = array[i];
    if (condition) {
        break; // <---------------
    }
}


// FOREACH() LOOP:
// More about: /33-Web-development/frontend/javascript/forEach-loop.js

// Break doesn't work with forEach:
array.forEach((item, index) => {
    if (condition) {
        wasFound = true;
        return wasFound;  // <---------------
    }
});


// SOME() LOOP:
// More about: /33-Web-development/frontend/javascript/some.js

// Use some() which stops when you return true:
array.some((item, index) => {
    if (condition) {
        // Do your action here
        console.log('Found it!', item);
        return true; // This stops the iteration immetiatelly!
    }
    // Continue processing
    return false; // Continue to next item
});