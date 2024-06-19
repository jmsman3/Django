const num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

const  calculateOdd_EvenNumbers= (array) =>{
                     
    const odd_numbers = [];
    const even_numbes = [];

    for( let i in num){
        const element =array[i];
        if(element %2 == 0){
            even_numbes.push(element);
        }
        else{
            odd_numbers.push(element);
        }

    }
  return even_numbes;

}
const result = calculateOdd_EvenNumbers(num);
console.log(result);

