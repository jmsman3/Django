// const target = document.getElementById("title");
// console.log(target);

// const all_box = document.getElementsByClassName("box");

// for ( let i = 0; i<all_box.length; i++){
//     const element = all_box[i];

//     element.style.backgroundColor = "green";
//     if( element.innerText =='box-5'){
//         element.style.backgroundColor = 'red';
//     }
// }

document.getElementById("handleAdd").addEventListener("click", (event) => {
  const inputValue = document.getElementById("searchBox").value;
  const container = document.getElementById("comment_container");

  const p = document.createElement("p");
  p.innerText = inputValue;

  container.appendChild(p);

  document.getElementById("searchBox").value = "";

  p.classList.add("child");
  const allComment = document.getElementsByClassName("child");

  for (const element of allComment) {
    element.addEventListener("click", (e) => {
      e.target.parentNode.removeChild(element);
    });
  }
});

fetch("https://jsonplaceholder.typicode.com/users")
  .then((res) => res.json())
  .then((data) => {
    displayData(data);
  })

  .catch((err) => {
    console.log(err);
  });

const displayData = (userData) => {
  const container = document.getElementById("userData-container");

  userData.forEach((user) => {
    const div = document.createElement("div");

    div.classList.add("user");

    div.innerHTML = `
        <h4>title</h4>
        <p>Description</p>
        <button>Details</button>`;
    container.appendChild(div);
  });
};
