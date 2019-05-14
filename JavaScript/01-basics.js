// press fn + f8 to run code
// most of this is from this gitbook: https://eleven-fifty-academy.gitbook.io/javascript-100-prework-gitbook/javascript-library/0-prework/4-js-basics
// some of this i added while doing Codecademy lessons

// ======================================================================================================================

// MATH
console.log(5 + 5);
console.log(6 - 6);
console.log(7 * 7);
console.log(8 / 8);
console.log(10 % 5);

// ======================================================================================================================

// VARIABLES
// variable names should be camelCased
var age = 40;   // declares the variable 'age' and initializes it with the value 40 
// can also be done on separate lines: 
// var x:
// x = 5
age += 1;
age -= 20;
age *= 20;
console.log(age);

let a = 9;  // this variable can be reassigned later
a = 10;
console.log(a);

const b = 8;    // this variable cannot be reassigned and will throw an error if you try

// you can declare but not initialize "let" variables 
// (in which case they'll be given the value 'undefined') 
// but "const" variables MUST be initialized when declared)

// ======================================================================================================================

// STRINGS
console.log("I was born in St.Louis.");
var birthCity = "St.Louis ";
var birthState = "Missouri";
console.log(birthCity + ", " + birthState);
console.log("Birth place: ", birthCity);
console.log(`I was born in ${birthCity}, ${birthState}.`)

// String methods
//length - returns the length of a string (including spaces)
console.log(highSchool.length); 

//lower or upper case
console.log(highSchool.toUpperCase()); //BILL MURRAY HIGH SCHOOL
console.log(highSchool.toLowerCase()); //bill murray high school

console.log(highSchool.split(" ")); //splits the string into an array on each space['Bill', 'Murray', 'High', 'School' ]
console.log(highSchool.slice(10)); // cuts off everything before the nth index

// ======================================================================================================================

// BOOLEANS
var isAuthenticated = true;
var hasLoggedInToday = false;

// == Equality
// === Strict Equality
// != inequality
// !== strict inequality
// > greater than
// >= greater than or equal to
// < less than
// <= less than or equal to

console.log(2 > 1); //true
console.log(3 < 2); //false

var test = 2 >= 3; 
console.log(test);
console.log("Two is greater than one? " + (2 > 1));

// important rule about == and ===
// == checks to see if the values are the same, not the type. === checks to see if the values AND the equality are the same
// 2 == '2'   TRUE
// 2 === '2'  FALSE
// 2 === 2    FALSE
// 'Password12!!' === 'Password12!!'   TRUE

// LOGICAL OPERATORS
// && = and
// || = or
// ! = not

// ======================================================================================================================

// CONDITIONALS
var isOn = true;
if(isOn === true) {
    console.log("The light is on."); // if isOn == true, execute console log
}

// shorter phrasing
var isOn = true;
if(isOn) {
    console.log("The light is on. It's bright.");
} 

var weather = 75;
if(weather > 70){
    console.log("Wear shorts today! It's going to be hot!");
} else if (weather < 70) {
    console.log("It's not that hot.");
} else {
    console.log('it is exactly 70 degrees');
}


// TERNARY OPERATORS // shorthand if/else
let isNightTime = true
isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');
// Condition provided before the '?'
// 2 expressions follow the ? and are separated by a :
// if condition is true, first expression executes
// if condition is false, second expression executes


// SWITCH STATEMENTS 
var animal = "cat"
switch (animal) {
    case 'cat':
        console.log('meow');
        break;
    case 'dog':
        console.log('woof');
        break;
    case 'bird':
        console.log('squawk');
        break;
    case 'fish':
        console.log('glub');
        break;
    default:
        console.log("i don't know that animal");
        break;
}
// can be used in place of a bunch of 'if else' statements
// The switch keyword initiates the statement and is followed by (), which contains the value that each case will compare. In the example, the value or expression of the switch statement is animal.
// the value of animal is 'cat', so the first case runs
// use break so it'll stop and not check the rest of the cases (unless that's what you want)
// if none of the cases are met, the default runs

