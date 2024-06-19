const LoadAllProducts = () => {
  fetch("https://fakestoreapi.com/products")
    .then((res) => res.json())
    .then((data) => {
      displayProduct(data);
    });
};

const displayProduct = (products) => {
  const productsContainer = document.getElementById("product-container");

  products.forEach((product) => {
    console.log(product);
    const div = document.createElement("div");
    div.classList.add("card");
    div.innerHTML = ` 
    <img  class ="card-img" src="${product.image}" alt="">
            <h5>${product.title}</h5>
            <h3> Price: $${product.price}</h3>
            <p>${product.description.slice(0, 50)}</p>

            <button onclick = "singleProduct('${product.id}')">Details</button>
            <button onclick="handleAddToCart('${product.title}',${
      product.price
    })" >Add to Cart</button>`;

    productsContainer.appendChild(div);
  });
};

const handleAddToCart = (name, price) => {
  const cartCount = document.getElementById("count").innerText;
  let convertedCount = parseInt(cartCount);
  convertedCount = convertedCount + 1;
  document.getElementById("count").innerText = convertedCount;

  console.log(convertedCount);

  const container = document.getElementById("cart-main-container");

  const div = document.createElement("div");
  div.classList.add("cart-info");

  div.innerHTML = `
  <p> ${name.slice(0, 10)}: </p> 
  <h3 class="price" >${price}</h3>`;

  container.appendChild(div);
  updateTotal();
};

const updateTotal = () => {
  const allPrice = document.getElementsByClassName("price");
  let count = 0;
  for (const element of allPrice) {
    count = count + parseFloat(element.innerText);
  }
  document.getElementById("total").innerText = count.toFixed(2);
};

const singleProduct = (id) => {
  console.log(id);
  fetch(`https://fakestoreapi.com/products/${id}`)
    .then((res) => res.json())
    .then((json) => console.log(json));
};

LoadAllProducts();
