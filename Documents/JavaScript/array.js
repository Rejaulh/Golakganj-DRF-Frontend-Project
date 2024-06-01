const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Opel";
console.log(cars);
console.log(cars.toString());
document.getElementById("demo").innerHTML= cars;

const person= ["jhon", "Doe", 45];
console.log(person[2]);
console.log(person.length);

const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fruit= fruits[fruits.length - 1];
console.log(fruit);
let leng= fruits.length;
let text = "<ul>";
for(let i=0; i<leng; i++)
    {
        text = text + "<li>" + fruits[i] + "</li>";
    }
    text += "</ul>";
console.log(text);
document.write("<br>" + text + "<br>");

let text1= "<ul>";
fruits.forEach(myFunction);
text1 += "</ul>";
document.write(text1);
function myFunction(value){
    text1 += "<li>" + value + "</li>";
}

fruits[6]= "Guava";
document.write("<br>" + fruits);
console.log(fruits.at(2));
console.log(fruits.join("*"));
console.log(fruits.pop());
console.log(fruits);

const fruits1 = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits1.pop());
// document.write("<br>" + fruits1.pop());
console.log(fruits1.push("Kiwi"));
console.log(fruits1);
console.log(fruits1.shift());
console.log(fruits1);
console.log(fruits1.unshift("lemon"));
console.log(fruits1);
document.write("<br>" + fruits1);
fruits1[fruits1.length]="Banana";
document.write("<br>" + fruits1);

const arr1 = ["Cecilie", "Lone"];
const arr2 = ["Emil", "Tobias", "Linus"];
const arr3 = ["Robin", "Morgan"];
const myChildren = arr1.concat(arr2, arr3);
console.log(myChildren);

const myArr = [[1,2],[3,4],[5,6]];
const newArr = myArr.flat();
console.log(newArr);
console.log(myChildren);
myChildren.splice(3,0,"Rejaul","Wasif");
console.log(myChildren);
let remove= myChildren.splice(3,2,"Hoque", "Riyan");
console.log(myChildren);
console.log(remove);

const fruit$s = ["Apple", "Orange", "Apple", "Mango"];
let position = fruit$s.indexOf("Apple") + 1;
console.log(position);
console.log(fruit$s.lastIndexOf("Apple") + 1);

/*const number= [4,9,16,25,29];
let first= number.find(myFunction);
// console.log("First number over 25 is : " + first);
function myFunction(value,index,Array){
    return value>18;
}
console.log("First number over 18 is : " + first);
let first1= number.findIndex(myFunction);
function myFunction(value,index,Array){
    return index>18 ;
}
console.log("First index over 18 is: " + first1);*/

const temp = [27, 28, 30, 40, 42, 35, 30];
let high = temp.findLast(x => x > 40);
console.log("Last Tempreture 40 was: " + high);
fruit$s.sort();
console.log(fruit$s);
console.log(fruit$s.reverse());
console.log(fruit$s.toSorted());
const month= ["Jan", "Feb", "March", "April"];
console.log(month.toSorted());
console.log(month.toReversed());

const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a,b){return a>b});
console.log(points);

const point= [40, 100, 1, 50, 35, 5, 25, 10];
point.sort(function() {return 0.5 - Math.random()});
console.log(point);

/*const point= [40, 100, 1, 5, 25, 10];
console.log(point);
function myFunction(){
    for(let m=point.length-1; m>0; m--)
        {
            let j= Math.floor(Math.random() * (m+1));
            let k= point[m];
            point[m]= point[j];
            point[j]= k;
        }
        console.log(point);
}

const points1 = [40, 100, 1, 5, 25, 10];
document.getElementById("demo").innerHTML = points1;  

function myFunction() {
  for (let i = points1.length -1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i+1));
    let k = points1[i];
    points1[i] = points1[j];
    points1[j] = k;
  }
}
  document.getElementById("demo").innerHTML = points1;*/

/*const point = [40, 100, 1, 5, 25, 10];
function myArrayMin(arr)
{
    return Math.min.apply(null, arr);
}
console.log("Min value of array is: " + myArrayMin(point));
function myArrayMax(arr)
{
    return Math.max.apply(null, arr);
}
console.log(myArrayMax(point));*/

const numbers7 = [45, 4, 9, 16, 25];

let t_xt = "";
numbers7.forEach(myFunction);
document.write(t_xt);

function myFunction(value, index, array) {
  t_xt += value + "<br>"; 
}

const $myArr= [1,2,3,4,5,6] ;
const $newArr= $myArr.flatMap((x) => x*2);
console.log($newArr);

const numbers = [45, 4, 9, 16, 25];
function myFunction(value) {
    return value > 18;
  }
  const over18 = numbers.filter(myFunction);
  console.log(over18);

  let arr4= [1,2,3,4,5,6,7];
  let sum= arr4.reduce(myFunction);
  console.log(sum);
  function myFunction(h1,h2){
    return h1+h2;
  }
  

  let arr5= [3,5,3,8,1,10];
  let mul= arr5.map(myFunction);
  console.log(mul);
  function myFunction(value){
    return value * 2;
  }

  let arr6= [3,8,9,2,4];
  let sum1= arr6.reduce(myFunction);
  console.log(sum1);
  function myFunction(total,value){
    return total + value;
  }

  let arr7= [3,8,9,2,4];
  let allover= arr7.every(myFunction);
  console.log("allover 2 is : " + allover);
  function myFunction(index,value){
    return value>2 ;
  }

  const arr8=Array.from("ABCDEFGH");
// let $form= arr8.form();
console.log(arr8);

const arr9= ["Apple","Mango","Orange","Pinaple"];
const key= arr9.keys();
let text3= " ";
for(let x of key){
  text3 +="<br>"+x + "<br>";
}
document.write(text3);

const arr10= ["Apple","Mango","Orange","Pinaple"];
const keys= arr9.entries();
let text4= " ";
for(let x of keys){
  text4 +="<br>"+x + "<br>";
}
document.write(text4);


const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "May"];
const year= [...q1, ...q2, ...q3, ...q4];
console.log(year);

const car= ["Saab", "BMW", "verna"];
console.log(car[1]);
{
  const car= ["Toyota", "Maruti", "Mohindra"];
  console.log(car[0]);
}
console.log(car[0]);

