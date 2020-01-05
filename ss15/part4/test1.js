var delSongs = document.getElementsByClassName("del_func");
for (var i=0;i<delSongs.length;i++) {
    var delSong=delSongs[i];
    delSong.addEventListener('click', function(e) {
        var selectedDel=e.target;
        var div = selectedDel.parentNode;
        div.remove()
    });
    
}
