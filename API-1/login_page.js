const url = "http://127.0.0.1:8000/api/login/";
document.getElementById("login-form").addEventListener('submit', function(e){
e.preventDefault();

fetch(url, {
    method : "POST",
    headers : {
        "content-Type":"application/json",
    },
    body: JSON.stringify({
        username:document.getElementById("username").value,
        password: document.getElementById("password").value
    })
})
.then(response => response.json())
.then(data => {
    if (data.access){
        localStorage.setItem("token", data.access);
        alert("Login Succesfull !");
    }else {
        alert("Login Failed!");
    }
})
.catch(error => {
    console.log('Error:', error);
});
});