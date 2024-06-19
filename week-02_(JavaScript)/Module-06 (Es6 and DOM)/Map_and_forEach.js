const Product = [
    {id : 1 , name:'Xaomi', description:'This is Xaomi', price : 500 , color:"Black"},
    {id : 2 , name:'Xaomi', description:'This is Xaomi', price : 500 , color:"Black"},
    {id : 3 , name:'Apple', description:'This is apple', price : 1500 , color:"white"},
    {id : 4 , name:'Apple', description:'This is apple', price : 1500 , color:"white"},
    {id : 5 , name:'Xaomi', description:'This is Xaomi', price : 500 , color:"Black"},
    {id : 6 , name:'Xaomi', description:'This is Xaomi', price : 500 , color:"Black"},
                       
]

const sum = Product.map( Product => Product.id *2);
console.log(sum);

const res = Product.forEach( Product => { console.log(Product.id)});