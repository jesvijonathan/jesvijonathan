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

//init();
// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function () {
  bg();
  scrollFunction();

  heads();
};

function heads() {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    //checkPosition();
    document.getElementById("header-container").style.opacity = "0";
    //document.getElementById("logo_id").style.opacity = "0";
  } else {
    document.getElementById("header-container").style.opacity = "1";
    //document.getElementById("logo_id").style.opacity = "1";
  }
}

function scrollFunction() {
  if (
    document.body.scrollTop > 177 ||
    document.documentElement.scrollTop > 177
  ) {
    document.getElementById("cover-name").style.opacity = "0";
    document.getElementById("logo_id").style.opacity = "1";

    if (!window.matchMedia("(max-width: 768px)").matches) {
      document.getElementById("logoi").style.right = "-50px";
      document.getElementById("logoi").style.opacity = "0";
      document.getElementById("logoi").style.visibility = "hidden";
    }
  } else {
    document.getElementById("cover-name").style.opacity = "1";
    document.getElementById("logo_id").style.opacity = "0";

    if (!window.matchMedia("(max-width: 768px)").matches) {
      document.getElementById("logoi").style.visibility = "visible";
      document.getElementById("logoi").style.right = "0px";
      document.getElementById("logoi").style.opacity = "1";
    }
  }

  //checkPosition();
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

var slideIndex = 1;

// Next/previous controls
function plusSlides(n) {
  showSlides((slideIndex += n));
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
/*
var elements;
var windowHeight;

function init() {
  elements = document.querySelectorAll(".hidden");
  windowHeight = window.innerHeight;
}

function checkPosition() {
  for (var i = 0; i < elements.length; i++) {
    var element = elements[i];
    var positionFromTop = elements[i].getBoundingClientRect().top;

    if (positionFromTop - windowHeight <= 0) {
      element.classList.add("fade-in-element");
      element.classList.remove("hidden");
    }
  }
}

window.addEventListener("resize", init);
*/

var i = 0;
var j = 0;
var s = 0;
var t = 0;
var g = 0;

var txt = "Hey ! ";
var txt1 = "Hey ! This is Jesvi Jonathan"; /* The text  Jesvi Jonathan here ✌️*/
var txt2 =
  "I am a sophomore persuing a degree in Bachelor of Technology in artificial intelligence & data science engineering.";
var txt3 =
  "Music, gaming, projects, etc is how I spend my paste time and my areas of ineterest are wide and am still exploring all oppurtunities.. Feel free to Contact me for collaboration :)";
var txt4 = "Wanna know more ?";
var speed = 20; /* The speed/duration of the effect in milliseconds */

function contact() {
  document.getElementById("inbtwId").style.height = "80px";
  document.getElementById("ncontact").style.visibility = "visible";
  document.getElementById("ncontact").style.opacity = "1";
  document.getElementById("ncontact").style.animation =
    "fade-in-glow 3s infinite ease-in-out";
}
function typeWriter() {
  document.getElementById("secl").style.minHeight = "720px";
  document.getElementById("header-container").style.opacity = "0";
  document.getElementById("gifo").style.opacity = "0";
  document.getElementById("revb").style.opacity = "0";

  typewr();
  setTimeout(typeWriter1, 1500);
  setTimeout(typeWriter2, 3000);
  setTimeout(typeWriter3, 5700);
  setTimeout(contact, 6500);

  if (window.matchMedia("(max-height: 480px)").matches) {
    document.getElementById("prof-im").style.height = "0px";
    document.getElementById("prof-im").style.width = "0px";
    document.getElementById("prof-im").style.marginBottom = "0px";
    document.getElementById("prof-im").style.marginTop = "30px";
  } else {
    document.getElementById("prof-im").style.marginTop = "40px";
    document.getElementById("prof-im").style.marginBottom = "40px";
  }
}
function typewr() {
  document.getElementById("demo").style.opacity = "1";
}
function typeWriter1() {
  document.getElementById("demo1").style.opacity = "1";
}
function typeWriter2() {
  document.getElementById("demo2").style.opacity = "1";
}
function typeWriter3() {
  document.getElementById("demo3").style.opacity = "1";
}
/*
function typeWriter4() {
  if (g < txt4.length) {
    document.getElementById("demo4").innerHTML += txt4.charAt(g);
    g++;
    setTimeout(typeWriter4, speed);
  }
}*/
//https://media.istockphoto.com/vectors/user-profile-icon-vector-avatar-portrait-symbol-flat-shape-person-vector-id1225790722?s=612x612
