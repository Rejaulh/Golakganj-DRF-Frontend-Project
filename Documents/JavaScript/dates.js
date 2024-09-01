let d= new Date("2022-03-24");
console.log(d);
const da= new Date();
console.log(da);
console.log(da.toString());
console.log(da.toDateString());
console.log(da.toISOString());
console.count(da.toUTCString());
const dat= new Date("2023-03-25");
let de= dat.getFullYear();
console.log(de);
console.log(Math.round(4.5));
console.log(Math.round(4.4));
console.log(Math.round(4.6));

console.log(Math.ceil(4.9));
console.log(Math.ceil(4.7));
console.log(Math.ceil(4.4));
console.log(Math.ceil(4.2));
console.log(Math.ceil(-4.2));
console.log(new Date());
console.log(Math.floor(4.9));
console.log(Math.floor(4.7));
console.log(Math.floor(4.4));
console.log(Math.floor(4.2));
console.log(Math.floor(-4.2));

console.log(Math.trunc(4.9));
console.log(Math.trunc(4.7));
console.log(Math.trunc(4.4));
console.log(Math.trunc(4.2));
console.log(Math.trunc(-4.2));

console.log(Math.sign(-4));
console.log(Math.sign(0));
console.log(Math.sign(4));

console.log("sin 90 is: " + Math.sin(90 * Math.PI/180));
console.log(Math.random() * 10) + 1;
console.log(Math.floor(Math.random()*10)+1);

function getRndInteger(min,max){
    return Math.floor(Math.random()*(max-min)+min);
}
console.log(getRndInteger(5,10));


console.log(Boolean());
console.log(Boolean(3));
console.log(Boolean(5>7));
console.log(Boolean(2>1));
console.log(Boolean(0));
console.log(Boolean(0<1));console.log(Boolean(0>-3));
console.log(Boolean("Hello"));
let b= Boolean(-0);
console.log(b);
let c= false;
Boolean(c);
console.log(c);

console.log(Boolean(false));
let x= 5;
let y= "5";
// x==y;
console.log(x==y);

let age= 15;
let votable= (age<18) ? "To Young" : "Old Enough";
console.log(votable);