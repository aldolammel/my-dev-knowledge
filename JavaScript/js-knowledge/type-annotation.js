/*
TYPE ANNOTATIONS / DATA HINT DECLARATIONS

    Concept: /Programming-Concepts/type-annotation.txt

    Types in JS (JSDoc):
        integer = {number}
        float = {number}
        string = {string}
        boolean = {boolean}
        object = {Object}
        anything = {*}
        containers = {number[]}, {string[]}, {[number, string]}, {Set<number>}, {Object.<string, number>}
*/

// Without:

let num = 10;
let name = "Aldo";
let data = { "vini": 1, "azevedo": 2 };

function getSomething() {
  return { 'abc': 1, 'def': 2 };
}

// With:

/** @type {number} */
let num = 10;

/** @type {string} */
let name = 'Aldo';

/** @type {Object.<string, number>} */
let data = { 'vini': 1, 'azevedo': 2 };

/**
* @returns {Object.<string, number>}
*/
function getSomething() {
  return { 'abc': 1, 'def': 2 };
}