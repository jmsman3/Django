// Example: Function with No Parameters

function great(){
    console.log("hello world...!")
}
great();

// Example: Function with Multiple Statements

function CalculateArea(radius){
    let area = Math.PI * radius * radius;
    return area;
}

let CircleArea = CalculateArea(2);
console.log(CircleArea);

console.log('\n---------Multiply below----------\n');

function doMultiply(num, num){
    let res = num * num;
    return res;
}
let Multitiply = doMultiply(5,5);
console.log("Your Mul result: ", Multitiply);

console.log('\n---------greet below----------\n');

function greetings( name, greeting){
    console.log(greeting + '! ,'+ name   );
}

greetings("jubaer Mahmud" , "Hello");