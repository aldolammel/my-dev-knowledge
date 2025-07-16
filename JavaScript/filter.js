/* 
    JAVASCRIPT: 'FILTER' METHOD
    The filter() method creates a new array filled with elements that pass a test provided by a fnc.
    The filter() method does not execute the function for empty elements.
    The filter() method does not change the original array.
*/

// Remove all occurrences of a specific value (example 1)
const ages = [8, 32, 33, 16, 40];
const result = ages.filter(checkAdult);

function checkAdult(age) {
  return age >= 18;
}
// Result: [32, 33, 40]

// Remove all occurrences of a specific value (example 2)
const originalArray = [1, 2, 3, 2, 4, 5];
const elementToRemove = 2;
const filteredArray = originalArray.filter(item => item !== elementToRemove);
// Result: [1, 3, 4, 5]

// Remove by object property
const users = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Bob' }
];
const userIdToRemove = 2;
const filteredUsers = users.filter(user => user.id !== userIdToRemove);

// Remove first occurrence and modify original array:
//  /JavaScript/splice.js