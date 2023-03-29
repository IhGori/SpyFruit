const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");


toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
})


//Script para animação de hover da sidebar de acordo com a href atual
//const activePage = window.location.pathname;
//const navLinks = document.querySelectorAll('.sidebar a').forEach(link => {
//  if(link.href.includes(`${activePage}`)){
//    link.classList.add('active');
//    console.log(link);
 // }
//})

