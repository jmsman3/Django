// var friends = [
//   "hero",
//   56,
//   "alom",
//   "test",
//   { name: "john" },
//   ["rohim", "karim"],
// ];

// // for( let i in friends){

// //     let element  = friends[i];
// //     if ( element == 'alom'){
// //         console.log("YEssssss");
// //     }
// //     else{
// //         console.log("Noooooo");
// //     }
// // }

// for (var i = 0; i < friends.length; i++) {
//   var element = friends[i];

//   if (element == 'alom') {
//     console.log("Yesssssssssss");
//   } else {
//     console.log("Nooooo");
//   }
// }
// ==================================================================================
// for Loop
// while Loop
// do...while Loop
// for...in Loop
// for...of Loop

// ========For Loop==============
for ( i = 0; i<5; i++){
    console.log('Number' + ':'+ i);
}
console.log('\n---------break----------\n');
// ========While Loop==============
let j = 0;
while( j <5){
    console.log('Number is '+':' + j);
    j++;
}
console.log('\n---------break----------\n');
// ========do while Loop==============

let k = 0;
do{
    console.log('Your Number ' + ':'+ k);
    k++;
}
while( k<5);

console.log('\n---------break----------\n');
// ========For in Loop==============

const person = { name:'jms', roll: '3434', class :'varsity'};
for ( let key in person){
    console.log( key + ": " + person[key]);
}


console.log('\n---------break----------\n');
// ========For of Loop==============

const numbers = [ 1,2,3,4,5,6,7,8,9,10];
for ( number of numbers){
    console.log('the number' + ":"+ number);
}


