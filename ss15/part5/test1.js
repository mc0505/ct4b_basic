var songList = document.getElementById("song_container");
var songs = document.getElementsByClassName("song");
var songTitles = document.getElementsByClassName("title");
var songArtists = document.getElementsByClassName("artist");
// for ( var i =0; i < songs.length; i++) {
//     console.log(songs[i]);
//     console.log(songTitles[i].innerHTML);
//     console.log(songArtists[i].innerHTML);
// };
var songDelete = document.getElementsByClassName("del_func")
for (var i = 0; i < songDelete.length; i++) {
    var song = songDelete[i];
    song.addEventListener('click', function (e) {
        var delSong = e.target;
        var div = delSong.parentNode;
        div.remove()
    })
};
var songIds = document.getElementsByClassName("print_id");
for (var i = 0; i < songIds.length; i++) {
    songId = songIds[i];
    songId.addEventListener("click", function (e) {
        var printId = e.target;
        var id = printId.parentNode;
        console.log("Song's id is", id.getAttribute("song_id"))
    })
};
var songInfos = document.getElementsByClassName("print_all");
for (var i = 0; i < songInfos.length; i++) {
    songInfo = songInfos[i];
    songInfo.addEventListener("click", function (e) {
        var printInfo = e.target;
        var id = printInfo.parentNode;
        console.log("Song's id is", id.getAttribute("song_id"));
        console.log("Song's name is", songTitles[0].innerText)
        console.log("Song's artist is", songArtists[0].innerText)
    });
}
function addSong() {
    var songContainer = document.getElementById("song_container");
    var newSong = document.createElement("div");
    var name = document.createTextNode("Sunflower")
    var spacing = document.createElement("hr");
    var songName = document.createElement("h4");
    var artist = document.createElement("h5");
    var singer = document.createTextNode("Post Malone");
    artist.appendChild(singer);
    songName.appendChild(name);
    songContainer.appendChild(newSong);
    songContainer.appendChild(spacing);
    songContainer.appendChild(songName)
    songContainer.appendChild(artist);

}

