while (condition) {
    // code block to be executed
  }

// EXAMPLE:
let i = 0;

while (i < 5) {
  console.log("The number is " + i);
  i++;  // make sure to increment to avoid infinite loop
}

// Output is:
// The number is 0
// The number is 1
// The number is 2
// The number is 3
// The number is 4
