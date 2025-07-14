/* 
    JAVASCRIPT: 'FINDINDEX' METHOD
    The findIndex() method executes a function for each array element.
    The findIndex() method returns the index (position) of the first element that passes a test.
    The findIndex() method returns -1 if no match is found.
    The findIndex() method does not execute the function for empty array elements.
    The findIndex() method does not change the original array.
*/


// Return the index of the first element found:
const ages = [2, 10, 18, 20];
ages.findIndex(checkAge);
age => ages === userIdToRemove

function checkAge(age) {
  return age > 18;
}
// Result: 3