let x;
x ??=7;
console.log(x);

let y = 16 + 4 + "Volvo";
console.log(y);
let z = "Volvo" + 16 + 4;
console.log(z);

let a;
a= 5;
a= "Rejaul";
console.log(a);

let answer1 = "It's alright";
let answer2 = "He is called 'Johnny'";
let answer3 = 'He is called "Johnny"';
console.log(answer1 + "<br>" + answer2 + "<br>" + answer3);
document.write(answer1 + "<br>" + answer2 + "<br>" + answer3 + "<br>");

let b= 123e5;
let c= 123e-5
console.log(b + "<br>" + c);
document.write(b + "<br>" + c + "<br>");

let d = BigInt("123456789012345678901234567890");
console.log(d);

let e= 5;
let f= 5;
let g= 6;
console.log(e==f + "<br>" + e==g);
document.write(e == f + "<br>" + e == g);

document.getElementById("demo").innerHTML =
(e == f) + "<br>" + (e == g);

const car= ["Saab" , "Audi" , "Volvo"];
console.log(car[1]);

const person= {firstName:"Rejaul" , lastName:"Hoque" , age:33 , eyeColor:"Blue"}
document.write("<br>" + person.firstName + " is " + person.age + " years old .");

console.log(typeof "" + "<br>" + typeof "Rejaul");
console.log(typeof 5);
console.log(typeof 3.145);
console.log(typeof (2+5));
let bus;
console.log(typeof bus);