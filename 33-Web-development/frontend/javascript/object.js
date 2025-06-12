/*
    JAVASCRIPT: CREATING AN OBJECT
*/

let newObj = {}  // empty obj.



// Basic object literal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
const person = {
    name: "John",
    age: 30,
    city: "New York",
    // Method inside object
    greet: function() {
        return `Hello, I'm ${this.name}`;
    },
    // ES6 shorthand method syntax
    introduce() {
        return `I'm ${this.name}, ${this.age} years old`;
    }
};

console.log(person.name); // "John"
console.log(person.greet()); // "Hello, I'm John"





// MODERN APPROACH / SIMILAR WAY TO OTHER LANGUAGES - - - - - - - - - - - - - - - - - - - - - - - - 

class Animal {
    // Constructor method
    constructor(name, species, age) {
        this.name = name;
        this.species = species;
        this.age = age;
    }
    
    // Instance method
    makeSound() {
        return `${this.name} makes a sound`;
    }
    
    // Static method (belongs to class, not instance)
    static getSpeciesCount() {
        return "Many species exist";
    }
    
    // Getter method
    get description() {
        return `${this.name} is a ${this.age}-year-old ${this.species}`;
    }
    
    // Setter method
    set newAge(age) {
        if (age > 0) {
            this.age = age;
        }
    }
}

// Creating objects from class
const dog = new Animal("Buddy", "Dog", 3);
const cat = new Animal("Whiskers", "Cat", 2);

console.log(dog.makeSound()); // "Buddy makes a sound"
console.log(dog.description); // "Buddy is a 3-year-old Dog"
dog.newAge = 4; // Using setter
console.log(Animal.getSpeciesCount()); // "Many species exist"