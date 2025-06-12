
/*
    LET

    - Block-scoped (exists only within the nearest enclosing block)
    - Cannot be redeclared in the same scope
    - Can be updated/reassigned
    - Hoisted but not initialized (temporal dead zone)
    - Preferred for variables that need to change
*/

function example() {
    if (true) {
        let y = 1; // Block-scoped
    }
    // console.log(y); // Error! y is not defined outside the block
    
    let z = 2;
    // let z = 3; // Error! Cannot redeclare
    z = 3;        // Reassignment allowed
}


/*
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    CONST

    - Block-scoped (like let)
    - Cannot be redeclared in the same scope
    - Cannot be reassigned (but objects/arrays can be mutated)
    - Must be initialized at declaration
    - Hoisted but not initialized (temporal dead zone)
    - Preferred for values that shouldn't be reassigned
*/

function example() {
    const PI = 3.14159; // Must initialize
    // PI = 3.14;       // Error! Cannot reassign
    
    const user = { name: "John" };
    user.name = "Jane";  // Allowed! Object mutation is fine
    user.age = 25;       // Allowed! Adding properties is fine
    // user = {};        // Error! Cannot reassign the variable itself
}



/*
    VAR (NOT RECOMMENDED)

    - Function-scoped or globally-scoped (not block-scoped)
    - Can be redeclared in the same scope
    - Can be updated/reassigned
    - Hoisted to the top of their scope and initialized with undefined
    - Considered the "old way" and generally avoided in modern JavaScript
*/

function example() {
    if (true) {
        var x = 1; // Function-scoped, not block-scoped
    }
    console.log(x); // Works! Prints 1
    
    var x = 2; // Redeclaration allowed
    x = 3;     // Reassignment allowed
}



/*
    BEST PRACTICES

    Use const by default for values that won't be reassigned.
    Use let when you need to reassign the variable.
    Avoid var in modern JavaScript due to its confusing scoping rules.

    The block-scoping of let and const makes code more predictable and helps prevent common bugs
    that can occur with var's function-scoping behavior.

*/



