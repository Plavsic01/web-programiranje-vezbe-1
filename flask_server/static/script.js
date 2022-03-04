function validation(){
    let indexValue = document.getElementById("index").value;
    let reg = new RegExp("^[0-9]{4}/[0-9]{6}$")
    let isValid = reg.test(indexValue);
    if(isValid){
        return true;
    }
    alert("Greska!")

}