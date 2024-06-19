const num = parseInt(2018);

if (num % 4 === 0 && num % 100 !== 0 || num % 400 === 0) {
    console.log( `YEs, ${num} is a Leap Year`);
}
else{
    console.log( `Sorry, ${num} is NOt a Leap Year`);
}
