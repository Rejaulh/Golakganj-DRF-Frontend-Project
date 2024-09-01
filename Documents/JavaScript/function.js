function myFunction(p1,p2)
{
return p1*p2;
}
let result= myFunction(4,3);
document.write("<br>" + result);
console.log(result);

let k= myFunction(3,3);
function myFunction(a,b)
{
    return a*b ;
}
console.log(k);

function toCelcius(f)
{
    return (5/9)*(f-32);
}
let value = toCelcius(77);
console.log(value);

let text = "The temperature is " + toCelsius(77) + " Celsius.";
// document.getElementById("demo").innerHTML = text;
console.log(text);

function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
} 

let text1= "Outside: " + typeof carName;
console.log(text1);
function myFunction()
{
    let carName= "Volvo";
    let text1= "Inside: " + typeof carName + " " + carName;
    console.log(text1);
}
myFunction();