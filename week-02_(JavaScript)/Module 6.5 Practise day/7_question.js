var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

// const ans = [...new Set(numbers)];
// console.log(ans);

const array = [];
for (let i = 0; i < numbers.length; i++) {

  let flag = true;

  for (let j = i + 1; j < numbers.length; j++) {

    if (numbers[i] === numbers[j]) {

      flag = false;
      break;
    }
    
  }
  if (flag == true) {
    array.push(numbers[i]);
  }
}

console.log(array);
