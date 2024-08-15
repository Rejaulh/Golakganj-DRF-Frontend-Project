const person = {};
person.firstname = "Riyan";
person.lastnbame = "Wasif";
person.age = 3;
document.getElementById("demo1").innerHTML= person.firstname +"is" + person.age + "years old" ;


const person1 = new Object();
person1.firstname = "Riyan";
person1.lastnbame = "Wasif";
person1.age = 3;
document.getElementById("demo2").innerHTML= person1.firstname +"is" + person1.age + "years old" ;


function Person(first, last, age, eye){
    this.FirstName= first;
    this.LastName= last;
    this.age= age;
    this.eyeColor= eye;
}
const myFather = new Person("Rejaul", "Hoque", 33, "blue");
document.getElementById("demo").innerHTML=
"my father name is " + myFather.FirstName;


const person2 = {
    firstname:"Wahiba",
    lastname: "islam",
    age: 12
};
const person3 = {
    firstname : "Osaidi",
    lastname : "Ali"
};
Object.assign(person2 , person3);
const text = Object.entries(person2);
document.getElementById("demo3").innerHTML= text;


const fruits = {Bananas:300, Apple:200, Orange:500};
let text1 = "";
for(let[fruit,amount] of Object.entries(fruits)){
text1 += fruit +"   :     "+ amount + "<br>";
}
document.getElementById("demo4").innerHTML=text1;


const perso = {
    fname: "osaidi",
    lname : "Islam",
    age : 12
};
Object.defineProperty(perso, "year", {value:"2008"});
document.getElementById("property").innerHTML= perso.fname +"<br>"+ perso.year


const person4 = {
    firstName: "John",
    lastName: "Doe",
    language: "en",
    get lang() {
      return this.language;
    }
  };
  
  // Display data from the object using a getter:
  document.getElementById("demo5").innerHTML = person4.lang;


  class car{
    constructor(name,year){
        this.name = name;
        this.year = year;
    }
    age(){
        const date = new Date();
        return date.getFullYear()-this.year;
    }
  }
  const mycar = new car("Ford", 2020);
  document.getElementById("demo6").innerHTML=
  "My car is " + mycar.age() + " old";

  
  function checkCookies(){
    let text = "";
    if (navigator.cookieEnabled == true) {
        text = "Cookies are enabled.";
  } else {
        text = "Cookies are not enabled.";
  }
document.getElementById("demo7").innerHTML=text;
}

function mOver(obj){
    obj.innerHTML="Thank You";
}
function mOut(obj){
    obj.innerHTML="Click here";
}

document.getElementById("demo8").innerHTML = 
"Available screen width is " + screen.availWidth;
document.getElementById("demo9").innerHTML =
"Page path is: " + window.location.pathname;



const apiUrl = 'http://127.0.0.1:8000/api/worker/';
const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMTI1MzAwLCJpYXQiOjE3MjMxMTQ1MDAsImp0aSI6Ijk2YzE5MDk1Y2QwMjQwZWJhNmQ2ZDAyMTNhN2Q2YTgwIiwidXNlcl9pZCI6NH0.yM0ezcQfQ7TTiXCsWD7kx28KMuJonLzcbaB8P-AzunI";
async function fetchData() {
    // dataTableBody.innerHTML = ''; // Clear previous data

    try {
        const response = await fetch(apiUrl, {
            method: 'GET', // HTTP method
            headers: {
                'Authorization': `Bearer ${token}`, // Add the token to the Authorization header
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
        const errorRow = document.createElement('tr');
        const errorCell = document.createElement('td');
        errorCell.colSpan = 12;
        errorCell.textContent = 'Failed to load data.';
        dataTableBody.appendChild(errorRow);
    }
}