var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

let element = friends[0];
for( let i = 1; i<friends.length; i++){

    if( element.length < friends[i].length){
        element = friends[i];
    }

}
console.log(element);