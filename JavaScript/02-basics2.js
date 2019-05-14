// FUNCTIONS
// use 'function' keyword to notify that it's a function. Name the function hello 
function hello() {
    console.log("hewwo world! uwu");     // execute some code when the fuction is called
}
hello();

// Parameters are the names listed in the function definition.
// Arguments are the real values received by the function when you call it.

function numberEntered(x) {
    console.log("The number you entered was: ", x);
}
numberEntered(37);


function addAnyTwoNumbers(x, y){
    console.log(x + y);
}
addAnyTwoNumbers(4, 5);

// "When JS reaches a return statement it will stop executing that function. 
// The return is the value that the function spits out. 
// It is the value that gets distilled down and returned out of the function." 
function getMyTaxReturnAndDoMyTaxesAndStuff(a, x, y, z){
    let myInc = a * x;
    let myTaxes = myInc - y;
    let total = myTaxes + z;
    return total; 
}
getMyTaxReturnAndDoMyTaxesAndStuff(10000, 5, 50000, 0);


// FAT ARROW NOTATION
const area = (width, height) => {
    return width * height;
};

// ========================================================================================================================

// ARRAYS
var rainbowColors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'];
var raceWinners = [33, 72, 64];
var myFavoriteThings = ['Broccoli', 46074, 'Zombie Cats From Mars'];

// An array is created like a variable.
// It can be named anything. 
// We use square brackets [] to collect values.
// We separate items with commas in the brackets.
// We can have a collection of one type or we can also collect multiple types

// indexing works the same as in python (starts at 0, can be called with [])
//                  0      1         2        3 3/0       3/1      3/3       3/4
var countryArray = ["USA", "Russia", "China", ['Germany', 'Italy', 'France', 'Norway']];
console.log(countryArray[2]); 

// INDEXING NESTED LISTS
console.log(countryArray[3][3])  // Norway

// ========================================================================================================================

// LOOPS
// for (setup; test expression; increment) {
//     body;    
// }

for (var i = 1; i < 101; i += 1){
    console.log(i);
}

for ( var i = 1;    // starting point; start count from 1
    i <= 10;        // conditional section (condition to be met); as long as i is <=10 keep going
    i++) {          // what it does when it keeps going; i++ is shorthand for saying add 1 to i
        console.log("Number: ", i);
    }

for (var i = 0; i <= 50; i += 5) {
    console.log(i);
}

for (var i = 20; i >= 1; i--) {
    console.log(i);
}

// WHILE LOOPS
const cards = ['diamond', 'spade', 'heart', 'club'];

let currentCard
while (currentCard != 'spade') {
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard);
}

var x = 0
while (x < 4) {
    console.log(x);
    x++
}

// DO/ WHILE LOOPS
let countString = '';
let i = 0;
do {
  countString = countString + i;
  i++;
} while (i < 5);
console.log(countString);

// ========================================================================================================================

// OBJECT LITERALS
// sort of like dictionaries in python?
// created using var keyword. gets wrapped in {}
var bobAlcorn = {
    // name, age, vocation, isRetired are properties
    // each property has a value after the colon
    name: 'Bob Alcorn',
    age: 59,
    vocation: "Chief Operating Officer",
    isRetired: false
};

console.log(bobAlcorn);         // prints whole object
console.log(bobAlcorn.name);    // prints object, then value for name property
console.log(bobAlcorn.middleName); // undefined bc this property does not exist


