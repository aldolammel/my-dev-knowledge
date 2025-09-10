

// FUNCTION: BASIC - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    // Define the function
    function addNumbers(a, b) {
        return a + b;
    }
    // Call the function
    let result = addNumbers(5, 3);
    // Output: 8
    console.log(result);

    

    // Other example with params/args:
    function greet(name) {
        return "Hello, " + name + "!";
    }
    // Defining var:
    let greeting = greet("Alice");
    // Output: "Hello, Alice!
    console.log(greeting);



    // Another but without args:
    function greetSimple() {
        return "Hello, dude!";
    };



// FUNCTION: ARROW FUNCTION (SINCE 2015) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --
    
    // Traditional function expression
    const add1 = function(a, b) {
        return a + b;
    };

    // Arrow function equivalent
    const add2 = (a, b) => {
        return a + b;
    };

    // Even shorter for single expressions
    const add3 = (a, b) => a + b;