const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
}
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach((n) => n.addEventListener("click", closeMenu));

function closeMenu() {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function () {
  bg();
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 177 ||
    document.documentElement.scrollTop > 177
  ) {
    document.getElementById("cover-name").style.opacity = "0";
    document.getElementById("logo_id").style.opacity = "1";
  } else {
    document.getElementById("cover-name").style.opacity = "1";
    document.getElementById("logo_id").style.opacity = "0";
  }
}

function bg() {
  if (
    document.body.scrollTop > 230 ||
    document.documentElement.scrollTop > 230
  ) {
    document.getElementById("sec1").style.animation = "ba 0.3s 1 ease-in-out";
    document.getElementById("sec1").style.opacity = 0;
  } else {
    document.getElementById("sec1").style.animation = "bb 0.3s 1 ease-in-out";
    document.getElementById("sec1").style.opacity = 1;
  }
}
