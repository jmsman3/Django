
const check_BIg_friends = (array) =>{
    let big_friend = array[0];

    for ( let i in array){
        const element = array[i];
        if( element.length > big_friend.length){
            big_friend = element;
        }
    }
    return big_friend;
}


const friends = ['randy' , 'Lesnar' ,'Shwan' , 'Breat' , 'Undertaker' ,'jerico' ,'Moxely' , 'Jerry the King']
const res = check_BIg_friends(friends);
console.log(res);
