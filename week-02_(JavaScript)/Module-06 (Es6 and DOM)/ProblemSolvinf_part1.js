const Find_Odd_Even = (array) => {
  let even = [];
  let odd = [];

  for (let i in array) {
    const element = array[i];
    if (element % 2 == 0) {
      even.push(element);
    } else {
      odd.push(element);
    }
  }
  return { even ,odd};
};
const Numbers = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
];
const result = Find_Odd_Even(Numbers);
console.log(result);
