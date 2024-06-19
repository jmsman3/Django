let person = {
  firstName: "jubaer",
  lastName: "Mahmud",
  age: 20,
  isEmployed: true,
  Hobby: ["gardening", "travelling", "swimming"],
  address: {
    street: "A1 Capital Road",
    city: "Dubai",
    county: "Saudi Arabia",
  },
  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};

console.log(person.firstName);
console.log(person.lastName);
console.log(person.age);
console.log(person.Hobby);
console.log(person.address);
console.log(person.isEmployed);
console.log(person.address.city);
console.log(person.address.county);
console.log(person.address.street);

delete person.isEmployed;
console.log(person.isEmployed);

for ( let randy in person.address){
    console.log( randy + ":" + " "+ person.address[randy])
}

