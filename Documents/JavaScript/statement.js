// const hour= new Date.getHours();
if(new Date().getHours()<18){
    // greting= "Good Day";
    console.log("Good Day");
}

const hour= new Date().getHours();
let greeting;
if(hour>18)
    {
        greeting= "Good Day!";
    }
    else{
        greeting= "Good evening";
    }
    console.log(greeting);

    const time= new Date().getHours();
    let message;
    if(time<10){
        message= "Good Morning!";
    }
    else if(time<18){
        message="Good Day!";
    }
    else{
        message= "Good evening!";
    }
    console.log(message);


    const expression= new Date().getDay();
    let day;
    switch(expression){
        case 0:
            day= "Sunday";
            break;
            case 1:
                day= "Monday";
                break;
                case 2:
                    day= "Twesday";
                    break;
                    case 3:
                        day= "Wednesday";
                        break;
                        case 4:
                            day= "Thursday";
                            break;
                            case 5:
                                day= "Friday";
                                break;
                                case 6:
                                    day= "Saturday";
    }
    console.log("Today is : " + day);

    let text;
switch (new Date().getDay()) {
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
    break;
  default:
    text = "Looking forward to the Weekend";
}
console.log(text);

let text1;
switch (new Date().getDay()) {
  case 4:
  case 5:
    text1 = "Soon it is Weekend";
    break;
  case 2:
  case 6:
    text1 = "It is Weekend";
    break;
  default:
    text1 = "Looking forward to the Weekend";
}
console.log(text1);

let x="0";
switch(x){
    case 0:
        x= "Off";
        case 1:
            x= "On";
            default:
                x= "No value found";
}
console.log(x);

const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
let text2= "";
for(let i=0; i<cars.length; i++){
    text2 += cars[i] + "<br>";
}
document.write("<br>" +text2);

let text3= "";
for(let i=0; i<5; i++){
    text3 += "The number is : " + i ;
}
console.log(text3);

const cars1 = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
let i, len, text4;
for(i=0, len= cars1.length, text4=""; i<len; i++){
    text4 += cars1[i] + "<br>";
}
document.write(text4);

const person = {fname:"John", lname:"Doe", age:25};
let text5= "";
for(let x in person){
    text5 += person[x] + " ";
}
console.log(text5);

let language="JAVASCRIPT";
let text6= "";
for(let x of language){
    text6 += x + "<br>";
}
console.log(text6);

let y=0;
let text7= "";
do{
    text7 += "<br>" + "The value is : " + y ;
    y++;
}
while(y<10)
    document.write(text7);

const cars2 = ["BMW", "Volvo", "Saab", "Ford"];
let text8 = "";

list: {
  text8 += cars2[0] + "<br>"; 
  text8 += cars2[1] + "<br>"; 
  break list;
  text8 += cars2[2] + "<br>"; 
  text8 += cars2[3] + "<br>"; 
}
document.write("<br>" + text8);

// Create an Object
myNumbers = {};

// Make it Iterable
myNumbers[Symbol.iterator] = function() {
  let n = 0;
  done = false;
  return {
    next() {
      n += 10;
      if (n == 100) {done = true}
      return {value:n, done:done};
    }
  };
}

let $text = ""
for (const num of myNumbers) {
  $text += num +"<br>"
}

document.getElementById("demo").innerHTML = $text;


const letters= new Set(["1","2","3"]);
letters.add("4");
console.log(letters.size);

const letter= new Set();
const a= "a";
const b= "b";
const c= "c";

letter.add(a);
letter.add(b);
letter.add(c);
console.log(letter);
console.log(typeof letter);
console.log(letter instanceof Set);

const _letters = new Set();

// Add Values to the Set
_letters.add("a");
_letters.add("b");
_letters.add("c");
_letters.add("c");
_letters.add("c");
_letters.add("c");
_letters.add("c");
_letters.add("c");
console.log(_letters);
// listring set of elements
let txt= "";
for(let x of _letters){
    txt += "<br>" + "The value is : " + x;
}
document.write(txt);

const letter1= new Set(["A","B","C","D"]);
let iterator= letter1.entries();
let txt1= "";
for( let entry of iterator){
txt1 += "<br>" + entry;
}
document.write(txt1);

const fruits= new Map(
    [
        ["Apple", 500],
        ["Orange", 600],
        ["Banana", 700]
    ]
)
let value= fruits.get("Apple");
console.log("There are " + value + " apples");

let txt2= "";
fruits.forEach(function(num,key){
    txt2 += "<br>" + key + ' = ' + num;
})
document.write(txt2);


const $fruits= new Map(
    [
        ["Apple", 500],
        ["Orange", 600],
        ["Banana", 700]
    ]
)
let total= 0;
for(let x of $fruits.values()){
    total += x;
}
console.log(total);

let z= "123";
console.log(String("123"));

let d= new Date();
console.log(Number(d));
console.log(String(Date()));
console.log(String("false"));
console.log(Number(true));
console.log(~5);
console.log(5&1);
console.log(5|1);
console.log(5<<1);
console.log(-5>>1);

function dec2bin(dec){
    return (dec>>>0).toString(2);
}
console.log(dec2bin(-5));

function bin2dec(bin){
    return parseInt(bin, 2).toString(10);
  }
  console.log(bin2dec(101));

  let text9= "Rejaul Hoque";
  let resul= text9.match(/Rejaul/g);
  console.log(resul);

  let exp= "Give 100% discount";
  let digit= exp.match(/\d/g);
  console.log(digit);

  try {
    adddlert("Welcome guest!");
  }
  catch(err) {
    document.getElementById("demo").innerHTML = err.message;
  }


  /*function myFunction() {
    const message = document.getElementById("p01");
    message.innerHTML = "";
    let x = document.getElementById("demo").value;
    try { 
      if(x.trim() == "")  throw "empty";
      if(isNaN(x)) throw "not a number";
      x = Number(x);
      if(x < 5)  throw "too low";
      if(x > 10)   throw "too high";
    }
    catch(err) {
      message.innerHTML = "Input is " + err;
    }
  }*/
  

  
  x1=5;
  elem= document.getElementById("demo");
  elem.innerHTML= x1;
var x1;

"use strict";
let th= this;
console.log(th);

"use strict";
console.log(myFunction());
function myFunction()
  {
    return this;
  }

  const person1 = {
    firstName:"John",
    lastName: "Doe",
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  }
  
  const member = {
    firstName:"Hege",
    lastName: "Nilsen",
  }
  
  let fullName = person1.fullName.bind(member);
  console.log(fullName());

  let value6= (a,b)=>a*b ;
  let resul1= value6(4,5);
  console.log(resul1);
  
  let hello="";
  hello= ()=>{
    return "Hellow World!"
  }
  console.log(hello());

  class car {
    constructor(name,year){
      this.name = name;
      this.year = year;
    }
    age(){
      const date= new Date();
      return date.getFullYear() - this.year;
    }
  }
  const myCar1= new car("Fort", 2012);
  const myCar2= new car("Audi", 2019);
  console.log(myCar1.name + "  " + myCar2.name)
  console.log("This Fort car is " + myCar1.age() + " yeras old.");

 import { name,age } from "./module1.js";
//  let txt3= name + age;

//  document.getElementById("demo").innerHTML = txt3();
 console.log(name);

