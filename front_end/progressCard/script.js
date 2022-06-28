const panels = document.querySelectorAll('.panel') /* all the panels will be in an array form*/


panels.forEach((panel) => {
    panel.addEventListener('click',() => {
        removeActiveClasses()
        panel.classList.add('active')
    })
})


function removeActiveClasses(){
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}


var mySong = document.getElementById('mySong');
var icon = document.getElementById('icon');

icon.onclick = function() {
    if(mySong.paused){
        mySong.play();
        icon.src = "images/pause-button.png";
    }
    else{
        mySong.pause();
        icon.src = "images/play.png";
    }
}