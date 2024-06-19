const countryName = "Bangladesh";
const country = `My country name is ${countryName}`;
console.log(country);

let name = "Alice";
let age = 30;
const message  = `Hello , my name i s${name} and my age is ${age}`;
console.log(message);

const num1 = [1,2,3,4,5]
const num2 = [ 6,7,8,9,10]
const total_array = [...num1 , ...num2]
console.log(total_array);

let person = { name :'abul', age:25}
let company = { title :"ABTech" , location :"Mars"}
let final = {...person , ...company}
console.log(final);