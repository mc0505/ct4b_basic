function showPopup() {
    console.log("Clicked!!")
}
function changeContent() {
    document.getElementById("changeColor").innerHTML= "Tadaaa. Chữ sau khi được thẩm mỹ!!"
    document.getElementById("changeColor").style.color = "red";
}
function colorChange() {
    document.getElementById("rect").style.backgroundColor = "red";
}
function getRid() {
    document.getElementsByTagName("p")[1].removeAttribute("id"); 
}
function start() {
    document.getElementsByTagName("p")[2].removeAttribute("start");
}
var x = 0
function addScore() {
    x++;
    console.log("Your score is",x);
}
function subtractScore() {
    x--;
    console.log("Your score is",x)
}