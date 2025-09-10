/*

    FIND() METHOD

    Purpose: ....... Find the first element that matches a condition;
    Returns: ....... The actual element (or undefined if not found);
    Early Exit: .... Stops immediately when element is found;
    Use Case: ...... When you need to retrieve a specific element;

    Traditional For() loop method:
        /JavaScript/for.js

    Some() loop method:
        /JavaScript/some.js

    ForEach() loop method:
        /JavaScript/forEach-loop.js
*/

const users = [
    { id: 1, name: 'Alice', age: 25 },
    { id: 2, name: 'Bob', age: 30 },
    { id: 3, name: 'Charlie', age: 35 }
];

// Find the first user older than 28
const foundUser = users.find(user => {
    console.log(`Checking ${user.name}`);
    return user.age > 28;
});
// Output: Checking Alice, Checking Bob
// Returns: { id: 2, name: 'Bob', age: 30 }


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


array1 = [5, 12, 8, 130, 44];
const found = array1.find(element => element > 10);
console.log(found);  // Output: 12


// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// IMPORTANT: if you just wanna know if the element was found (true/false), use some() method!