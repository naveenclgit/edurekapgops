
document.getElementById("sellstk").addEventListener("change", setvalue());
document.getElementById("passwordc").addEventListener("change", passwordveri());


function passwordveri() {

    var pwdo = document.getElementById("password").value;
    var pwdc = document.getElementById("passwordc").value;
    var name = document.getElementById("username").value;

    if(name == "") {
        alert ("**Fill the first name");
    return false;
    }
    if(pwdo == "") or (pwdc == "") {
        alert ("Fill the password please!");
    return false;
    }
   if(pwd1 != pwdc) {
        alert ("Passwords are not same!");
    return false;
    }
    else {
    alert ("Account created!");
    document.write("Form has been submitted successfully");
    }
}


function setvalue(){
    alert ("Function called 1")
    document.getElementById('symbol').value = document.getElementById("sellstk").value;
    alert ("Function called 2")
}


