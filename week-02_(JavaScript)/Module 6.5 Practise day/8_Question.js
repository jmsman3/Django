// var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

// let element = numbers[0];
// for( let i = 1; i<numbers.length; i++){

//     if( element < numbers[i]){
//         element = numbers[i];
//     }

// }
// console.log(element);

function monthlySavings(payments, livingCost) {
  if (!Array.isArray(payments)) {
    return "invalid input";
  }

  if (typeof livingCost !== "number") {
    return "invalid input";
  }

  let totalIncome = 0;
  let totalTax = 0;

  for (let payment of payments) {
    totalIncome += payment;
    if (payment >= 3000) {
      totalTax += 0.2 * payment;
    }
  }

  // Sompurno Hesab
  let savings = totalIncome - totalTax - livingCost;

  // Aitku kornar case r ki...
  if (savings >= 0) {
    return savings;
  } else {
    return "earn more";
  }
}

console.log(monthlySavings([1000, 2000, 3000], 5400)); // prothom ta Output: 0
console.log(monthlySavings([1000, 2000, 2500], 5000)); // Detiyo ta  Output: 500
console.log(monthlySavings([900, 2700, 3400], 10000)); // third ta Output: 100
console.log(monthlySavings(100, [900, 2700, 3400])); // aita last er ta Output: "invalid input"
