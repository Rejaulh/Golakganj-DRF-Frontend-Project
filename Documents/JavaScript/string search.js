let text10 = "Please locate where 'locate' occurs!";
let index= text10.indexOf("locate");
console.log(index);
let index1= text10.lastIndexOf("locate");
console.log(index1);

let text11 = "Please locate where 'locate' occurs!";
let index2= text11.indexOf("locate", 15);
console.log(index2);


let text12 = "Please locate where 'locate' occurs!";
let index3= text12.search(/locate/);
console.log(index3);

let text13 = "The rain in SPAIN stays mainly in the plain";
const myArr1 = text13.match("ain");
console.log(myArr1);
const myArr2 = text13.match(/ain/gi);
console.log(myArr2);
document.getElementById("demo").innerHTML= myArr2.length + " " + myArr2;

let text14 = "I love cats. Cats are very easy to love. Cats are very popular."
const iterator = text14.matchAll("Cats");
console.log(Array.from(iterator));
// document.write(Array.from(iterator));
// document.getElementById("demo").innerHTML= Array.from(iterator); 

let fName= "Mohibul";
let lName= "Hoque";
let text15= `Welcome ${fName} ${lName}`;
console.log(text15);

let price = 10;
let VAT = 0.25;
let total = `Total: ${(price * (1 + VAT)).toFixed(2)}`;
console.log(total);
// list Item
let header = "Template Strings";
let tags = ["template strings", "javascript", "es6"];

let html = `<h2>${header}</h2><ul>`;

for (const x of tags) {
  html += `<li>${x}</li>`;
}

html += `</ul>`;
document.getElementById("demo").innerHTML = html;

let x1= 100;
let x2= "Apple";
let x3= isNaN(x1/x2);
console.log(x3);
console.log(typeof(NaN));

let number= 2;
let _txt = " ";
while(number!=Infinity){
    number *= number;
    _txt += number + "<br>";
}
console.log(_txt);
document.write(_txt);

let nnumber= 0xFF;
console.log(nnumber);

let myNumber1 = 32;
document.write(
"Decimal 32 = " + "<br><br>" + 

"Hexatrigesimal (base 36): " + myNumber1.toString(36) + "<br>" +
"Duotrigesimal (base 32): " + myNumber1.toString(32) + "<br>" +
"Hexadecimal (base 16): " + myNumber1.toString(16) + "<br>" +
"Duodecimal (base 12): " + myNumber1.toString(12) + "<br>" +
"Decimal (base 10): " + myNumber1.toString(10) + "<br>" +
"Octal (base 8): " + myNumber1.toString(8) + "<br>" +
"Binary (base 2): " + myNumber1.toString(2));

let m= 500;
let n= new Number(500);
console.log(m==n);

let x_1 = 99999999999999999999;
let x_2 = BigInt("99999999999999999999");
document.write("<br>" + x_1 + "<br>" + x_2);
console.log(typeof(x_2));

let x$x = 9007199254740995n;
let y$y = 9007199254740995n;
let z$z = (x * y);
console.log(z$z);

let r= 5n;
let s= Number(r)/2;
console.log(s);

let hex = 0x20000000000003n;
let oct = 0o400000000000000003n;
let bin = 0b100000000000000000000000000000000000000000000000000011n;
document.write("<br>" + hex +"<br>" + oct + "<br>" + bin + "<br>");

let max= Number.MAX_SAFE_INTEGER;
console.log(max);
let min= Number.MIN_SAFE_INTEGER;
console.log(min);

let xd = new Date("1970-01-02");
console.log(Number(xd));