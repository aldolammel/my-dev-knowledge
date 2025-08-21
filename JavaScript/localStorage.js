/* 
    JAVASCRIPT: localStorage

    localStorage is a property of the browser's window object, coming from the JavaScript Web API, 
    that allows you to store data locally within the user's browser with no expiration time. 
    The data persists even after the browser window is closed.

    Key Characteristics:

        - Persistence: Data survives browser restarts and computer reboots;
        - Scope: Data is specific to the protocol and domain (origin);
        - Storage Limit: Usually around 5-10MB per origin (varies by browser);
        - Synchronous: All operations are synchronous (blocking);
        - String Only: Can only store strings (use JSON.stringify/parse for objects);

    localStorage vs sessionStorage vs cookies:
        /JavaScript/sessionStorage.js

        - localStorage: Persists until explicitly removed;
        - sessionStorage: Persists only for the browser session;
        - cookies: Can be set with expiration dates, sent to server with requests;

*/

// Basic Usage - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

// Storing data
localStorage.setItem('username', 'john_doe');
localStorage.setItem('userAge', '25');

// Retrieving data
const username = localStorage.getItem('username');
const userAge = localStorage.getItem('userAge');

console.log(username); // 'john_doe'
console.log(userAge);  // '25'

// Removing a specific item
localStorage.removeItem('username');

// Clearing all localStorage data
localStorage.clear();


// Working with Objects and Arrays - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

// localStorage only stores strings, so you need to stringify objects
const user = {
    name: 'John',
    age: 30,
    preferences: ['coding', 'music']
};

// Store object (convert to JSON string)
localStorage.setItem('user', JSON.stringify(user));

// Retrieve and parse object
const retrievedUser = JSON.parse(localStorage.getItem('user'));
console.log(retrievedUser.name); // 'John'



// Checking if localStorage is Available - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

// Check if localStorage is supported
function isLocalStorageAvailable() {
    try {
        const test = 'test';
        localStorage.setItem(test, test);
        localStorage.removeItem(test);
        return true;
    } catch (e) {
        return false;
    }
}

if (isLocalStorageAvailable()) {
    // Use localStorage
    localStorage.setItem('data', 'some value');
} else {
    // Fallback for browsers that don't support it
    console.log('localStorage not available');
}