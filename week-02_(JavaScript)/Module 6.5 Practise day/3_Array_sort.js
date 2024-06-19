const array = [
  20, 19, 18, 17, 15, 16, 14, 12, 13, 11, 10, 9, 7, 8, 6, 4, 5, 2, 3, 1,
];

for (let i = 0; i < array.length; i++) {
  for (let j = i + 1; j < array.length; j++) {
    if (array[i] > array[j]) {
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
}

console.log('Here is Ypur Sorted array:-' , array);
