// script.js

function searchFood() {
  const searchInput = document.getElementById("searchInput").value.trim();
  const foodResults = document.getElementById("foodResults");

  // Clear previous results
  foodResults.innerHTML = "";

  if (searchInput === "") {
    // If search input is empty, do nothing
    return;
  }

  // Fetch data from API
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searchInput}`)
    .then((response) => response.json())
    .then((data) => {
      if (data.meals === null) {
        // If no results found
        foodResults.innerHTML = "<p>No results found</p>";
      } else {
        // Display food items
        data.meals.forEach((meal) => {
          const foodItem = document.createElement("div");
          foodItem.classList.add("foodItem");
          foodItem.innerHTML = `
                          <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
                          <p>${meal.strMeal}</p>
                          <button onclick="showDetails('${meal.idMeal}')">Details</button>
                          <button onclick="addToCart('${meal.strMeal}')">Add to Cart</button>
                      `;
          foodResults.appendChild(foodItem);
        });
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      foodResults.innerHTML =
        "<p>An error occurred. Please try again later.</p>";
    });
}

function showDetails(id) {
  // Fetch meal details by id
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((response) => response.json())
    .then((data) => {
      const meal = data.meals[0];
      const detailBar = document.getElementById("detailBar");
      detailBar.innerHTML = `
                  <h2>${meal.strMeal}</h2>
                  <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
                  <p>${meal.strInstructions}</p>
              `;
      detailBar.style.display = "block";
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function addToCart(foodName) {
  // You can implement the logic to add the food item to the cart here
  console.log(`Added "${foodName}" to cart`);
}
