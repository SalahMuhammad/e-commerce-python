// rest main image
links = document.getElementsByClassName('links')[0]
img = document.getElementsByClassName('img')[0]

links.addEventListener('click', (e) => {
    img.src = e.target["src"];
})