let cartItems = [];
let addToCartCount = 0;

function handleAddToCart(id) {
  fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${id}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.players) {
        const eachPlayer = data.players[0];

        if (addToCartCount >= 11) {
          alert("Hello, Bondhu Sorry, you cannot add more than 11 people to the cart.");
          return;
        }

        if (cartItems.some((item) => item.id === id)) {
          alert("Already added this item, ekta item ekbar er besi Add kora jabe nah, sorry");
          return;
        }

        cartItems.push({
          id: id,
          name: eachPlayer.strPlayer,
          photo: eachPlayer.strThumb,
          nationality: eachPlayer.strNationality,
          team: eachPlayer.strTeam,
          sport: eachPlayer.strSport,
        });

        addToCartCount++;
        updateCartDisplay();
      }
    })
    .catch((error) => {
      console.error("Error adding to cart:", error);
    });
}

function updateCartDisplay() {
  const cartCount = document.getElementById("count");
  cartCount.innerText = cartItems.length;

  const cartContainer = document.getElementById("cart-main-container");
  cartContainer.innerHTML = "";

  cartItems.forEach((item) => {
    const div = document.createElement("div");
    div.classList.add("cart-info");

    div.innerHTML = `
     <img src="${item.photo}" alt="${item.name}" width="50px" height="50px">
       <p>Name: ${item.name}</p>
       <p>Nationality: ${item.nationality}</p>
       <p>Team: ${item.team}</p>
       <p>Sport: ${item.sport}</p>
       <hr>
     `;
    cartContainer.appendChild(div);
  });

  const totalCount = document.getElementById("total");
  totalCount.innerText = addToCartCount;
}

// function staticPlayersAdd(){
//           const containerStatic = document.getElementsByClassName("left-container");
//           for( let i= 0; i<=12 ; i++){
//             const staticBoys = Search();
//             containerStatic.appendChild(staticBoys);
//           }
// }




function Search() {
  const searchField = document.getElementById("input-form-here").value;
  const leftContainer = document.querySelector(".left-container");
  fetch(`https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=${searchField}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.player === null) {
        leftContainer.innerHTML = "Sorry, no result found";
      } else {
        leftContainer.innerHTML = "";
        data.player.forEach((eachplayer) => {
          if (eachplayer.strThumb && eachplayer.strThumb.includes(".jpg") &&
              eachplayer.strDescriptionEN !== null && eachplayer.strFacebook !== null &&
              eachplayer.strInstagram !== null && eachplayer.strTwitter !== null) {
            const atlhetitem = document.createElement("div");
            atlhetitem.classList.add("atletitem");

            const words = eachplayer.strDescriptionEN.split(" ");
            const truncatedDescription = words.length > 20 ?
              words.slice(0, 20).join(" ") + "..." : eachplayer.strDescriptionEN;

            atlhetitem.innerHTML = `
                <img id="sportsmanimgid" src="${eachplayer.strThumb}">
                <p>Name: ${eachplayer.strPlayer}</p>
                <p>Nationallity: ${eachplayer.strNationality}</p>
                <p>Team: ${eachplayer.strTeam}</p>
                <p>Sports: ${eachplayer.strSport}</p>
                <p>Description: ${truncatedDescription}</p>

                <div class="social-links">
                    <a href="https://www.facebook.com/${eachplayer.strPlayer}">
                        <i class="fa-brands fa-facebook" style="color: #0088f0;"></i>
                    </a>
                    <a href="https://x.com/${eachplayer.strPlayer}">
                        <i class="fa-brands fa-twitter" style="color: #2977ff;"></i>
                    </a>
                    <a href="https://www.instagram.com/${eachplayer.strPlayer}">
                        <i class="fa-brands fa-instagram" style="color: #E1306C;"></i>
                    </a>
                </div>
                
                <div class="btn-flex-make">
                  <button data-id="${eachplayer.idPlayer}" onclick="handleAddToCart('${eachplayer.idPlayer}')">Add to Cart</button>
                  <button onclick="ShowDetail('${eachplayer.idPlayer}')">Detail</button>
                </div>`;
            leftContainer.appendChild(atlhetitem);
          }
        });
      }
    })
    .catch((error) => {
      console.error("Error Happened here:", error);
      leftContainer.innerHTML = "<p>An error Happened here, Please Try Again later...!!</p>";
    });
}


const the_search_button = document.getElementById("search-Bar-here");
the_search_button.addEventListener("click", function () {
  Search();
});

function ShowDetail(id) {
  fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${id}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.players) {
        const eachPlayer = data.players[0];
        const detailBar = document.getElementById("detailBar");

        const words = eachPlayer.strDescriptionEN.split(" ");
        const truncatedDescription = words.length > 20 ?
          words.slice(0, 20).join(" ") + "..." : eachPlayer.strDescriptionEN;

        detailBar.innerHTML = `
          <p>Name: ${eachPlayer.strPlayer}</p>
          <p>Nationality: ${eachPlayer.strNationality}</p>
          <p>Team: ${eachPlayer.strTeam}</p>
          <p>Sports: ${eachPlayer.strSport}</p>
          <p>Description: ${truncatedDescription}</p>
        `;

        detailBar.style.display = "block";
      }
    })
    .catch((error) => {
      console.error("Error fetching player details:", error);
    });
}
