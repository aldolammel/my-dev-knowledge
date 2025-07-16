/* 
    JAVASCRIPT: 'SPLICE' METHOD
    The splice() method adds and/or removes array elements.
    The splice() method overwrites the original array.
*/

// Remove first occurrence and modify original array
const array = [1, 2, 3, 2, 4, 5];
const elementToRemove = 2;
const index = array.indexOf(elementToRemove);
if (index > -1) {
  array.splice(index, 1); // Removes 1 element at index position
}
// array is now [1, 3, 2, 4, 5] - only first occurrence removed


// Remove specific object by property (plus findIndex() method):
const users = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Bob' }
];
const userIdToRemove = 2;
const idx = users.findIndex(user => user.id === userIdToRemove);
if (idx > -1) {
  users.splice(idx, 1);
}



// Remove all occurrences of a specific value:
//  /JavaScript/filter.js


// Remove by object property:
//  /JavaScript/filter.js
