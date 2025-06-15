fetch('/.navbar/navbar.html')
    .then(r => r.text())
    .then(t => document.getElementById('navbar').innerHTML = t);