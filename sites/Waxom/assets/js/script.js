burgermenu.onclick = function myFunction1(){
    var x = document.getElementById("mytopnav");

    if (x.className ==="menu"){
        x.className +="-responsive";
    } else{
        x.className = "menu";
    }

}

var link = document.getElementById("myLink");
var div = document.getElementById("myDiv");
var video = document.getElementById("myVideo");

link.addEventListener("click", function(event) {
    event.preventDefault();
    
    if (div.style.display === "none") {
        div.style.display = "flex";
        
        video.pause();
        video.currentTime = 0;
    } else {
        div.style.display = "none";
        
        video.play();
    }
});

video.addEventListener("ended", function() {
    div.style.display = "flex";
});

video.addEventListener("pause", function() {
    div.style.display = "flex";
});