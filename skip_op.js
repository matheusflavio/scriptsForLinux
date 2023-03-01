function hmsToSecondsOnly(str) {
    let timeStamp = str.split(':'), s = 0, m = 1;

    while (timeStamp.length > 0) {
        s += m * parseInt(timeStamp.pop(), 10);
        m *= 60;
    }

    return s;
}
function skipOP() {
    time = window.prompt("Digite o tempo para ir:")
    let videO
    if(isNaN(time))
        time = hmsToSecondsOnly(time)
    if(location.href.includes("crunchyroll"))
        videO = document.getElementById('player0')
    else if(location.href.includes("youtube"))
        videO = document.getElementsByClassName("video-stream html5-main-video")[0]
    videO.currentTime = time
}
skipOP()