var header = document.getElementById("header-cont");

var request = new XMLHttpRequest();
request.onreadystatechange = function() {
    if (request.readyState == XMLHttpRequest.DONE && request.status == 200) {
        header.innerHTML = request.responseText;
    }
}

request.open("GET", "/res/header.html");
request.send();