// fetch("https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata#")
//   .then((res) => res.json())
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.log(error);
//   });

// const container = document.getElementsByClassName("container");

function searchFood() {
  const searchInput = document.getElementsByClassName("input_search")[0].value;
  const foodResult = document.getElementById("foodResult");

  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searchInput}`)
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      if (data.meals === null) {
        foodResult.innerHTML =
          "<P id='p_For_no_result'>Sorry,Vaia<br>No result Found<br>Please input Exact Food name<br>Or input Any Single English Alphabet</p>";
      } else {
        document.getElementsByClassName("input_search")[0].value = "";
        const The_container = document.getElementById("f-container");
        foodResult.innerHTML = "";
        // display food items
        data.meals.forEach((meal) => {
          const foodItem = document.createElement("div");
          foodItem.classList.add("foodItem");

          foodItem.innerHTML = ` 
          <img  src="${meal.strMealThumb}" >
          <p> ${meal.strMeal} </p>
          <p> Catagory:-${meal.strCategory} </p>
          <button id= "btn_Deatail" onclick="ShowDetail('${meal.idMeal}')" > Details</button>
          <button id= "btn_Cart" onclick="ShowCart('${meal.idMeal}')"> Add to Cart</button>`;
          foodResult.appendChild(foodItem);
        });
        The_container.style.display = "block";
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      foodResult.innerHTML = "<p>An error occured.Please Try again later</p>";
    });
}

const searchButton = document.getElementById("searchButton");
searchButton.addEventListener("click", function () {
  searchFood();
});

function ShowDetail(id) {
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.meals) {
        const meal = data.meals[0];
        const detailBar = document.getElementById("detailBar");

        detailBar.innerHTML = ` 
        <img id= "detail_image_bar" src="${meal.strMealThumb}" alt="">
        <h2 id ="first_h2">Food name:  ${meal.strMeal}</h2>
        <h2 id ="first_h2">Food Demaing Area:  ${meal.strArea}</h2>
        <h2>Food Catagory: ${meal.strCategory}</h2>
          <p class="meal_p_class"> ${meal.strInstructions}</p>
          <p class="meal_p_class"> ${meal.strIngredient1}</p>
          `;
        detailBar.style.display = "block";

        detailBar.appendChild("f-container");
      }
    })
    .catch((error) => {
      console.error("Error Detais,try again:", error);
    });
}
function ShowCart(id) {
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.meals) {
        const meal = data.meals[0];
        const addCartElement = document.getElementById("add-cart");
        addCartElement.innerHTML = `  <p class= "p_for_add_cart"> 
             <span>Thanks for adding this food :( ${meal.strMeal})</span> <br>
             Khuda Lagse ? <br> Sorry,Bondhu....Ai Segment e Kono Khabar nai...!</p>;`;
      }
    })
    .catch((error) => {
      console.error("Error Detais,try again:", error);
    });
}
