const car1 = {type:"Fiat", model:"500", color:"white"};
console.log(car1.type);
console.log(car1["color"]);

const person1 = {
    firstName:"Riyan" ,
    lastName:"Wasif",
    idNumber: 5456,
    fullName: function(){
         return this.firstName + " " + this.lastName;
    }
};
console.log(person1.fullName());
// alert(person1.fullName());
// Disply the current date and time;
console.log(Date());
function displayDate(){
    // console.log(Date());
    document.getElementById("demo").innerHTML= Date();
}
// Templet string:
let text2= `He is a Boy
The quick
brown fox
jumps over
the lazy dog`;
document.write(text2);
console.log(text2);

let text3 = "Rejaul H";
let length = text3.length;
console.log(length);

let text4 = "The character \" is\" called backslash.";
console.log(text4);

let text5= "Osaidi";
let text6= new String('Islam');
console.log(typeof text5 + "<br>" + typeof text6);

let text7= "Hello World";
console.log(text7.charAt(0));
console.log(text7.charCodeAt(3));
console.log(text7.at(6));
console.log(text7[7]);

let text8= "Apple, Banana, Kiwi";
let part= text8.slice(7,13);
console.log(part);
document.getElementById("demo").innerHTML= part;
let part1= text8.slice(7);
console.log(part1);
let part2= text8.slice(-11);
console.log(part2);
let part3= text8.slice(-12,-7);
console.log(part3);

console.log(text8.substring(7,13));
console.log(text8.substring(7));
console.log(text8.substring(-4));

let text9= "Hello World!";
let uppercase= text9.toUpperCase();
console.log(uppercase);
let lowercase= text9.toLowerCase();
console.log(lowercase);

let part4= "Hello";
let part5= "India !";
let part6= part4.concat(" ", part5);
console.log(part6);

let text_1 = "     Hello World!     ";
let text_2 = text_1.trim();
console.log(text_2);

let $text= "5";
let padded= $text.padStart(6,"0");
console.log(padded);
let padded$= $text.padStart(9,"X");
document.write("<br>" + padded$);
console.log($text.padEnd(6,"&"));

let txt= "Hello Darling. ";
let rep= txt.repeat(3);
console.log(rep);

let txt1= "I Love You";
let newtxt= txt1.replace("Love","Like");
console.log(newtxt);

let txt2 = "I love cats. Cats are very easy to love. Cats are very popular."
txt2 = txt2.replaceAll("Cats","Dogs");
txt2 = txt2.replaceAll("cats","dogs");
document.write("<br>" + txt2 + "<br>");

let txt3= "a,b,c,d,e,f";
const myArr= txt3.split(",");
console.log(myArr[4]);

let txt4= "WAHIBA";
const myArra= txt4.split("");
txt4= "";
for(let i=0; i<myArra.length; i++)
    {
        txt4 += myArra[i] + "<br>";
    }
document.write(txt4);
