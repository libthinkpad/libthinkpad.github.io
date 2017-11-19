var footer = document.getElementById("footer-cont");

var req = new XMLHttpRequest();
req.onreadystatechange = function() {
    if (req.readyState == XMLHttpRequest.DONE && req.status == 200) {
        footer.innerHTML = req.responseText;
    }
}

req.open("GET", "/res/footer.html");
req.send();