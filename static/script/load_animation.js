var loading_var = "What The Heck Are You Doing ?!";

console.log(loading_var);


function load_tout(){
    document.querySelector("#load-fill").style.visibility = "hidden";
    document.querySelector("body").style.overflowY = "scroll";

    document.onreadystatechange = function () {
        if (document.readyState == "complete") {

            document.querySelector(".loading").style.visibility = "hidden";
            document.querySelector(".loading").style.position = "absolute";

            // var myDiv = document.getElementById("#sec2");
            // myDiv.innerHTML = variableLongText;
            // myDiv.scrollTop = 0;
        }
    };
};

document.onreadystatechange = function () {
  if (document.readyState == "complete") {
    document.querySelector("#load-fill").style.visibility = "hidden";
    document.querySelector("body").style.overflowY = "scroll";

    //document.querySelector("#cover-name").style.position = "relative";

    document.querySelector(".loading").style.visibility = "hidden";
    document.querySelector(".loading").style.position = "absolute";

    // var myDiv = document.getElementById("#sec2");
    // myDiv.innerHTML = variableLongText;
    // myDiv.scrollTop = 0;
  } else {
    document.querySelector("#load-fill").style.visibility = "visible";
    document.querySelector("body").style.overflowY = "hidden";

    //document.querySelector("#cover-name").style.position = "fixed";
    document.querySelector(".loading").style.visibility = "visible";
    document.querySelector(".loading").style.position = "fixed";

    setTimeout(function() { load_tout(); }, 3000);
  }
};




// document.addEventListener("contextmenu", function (e) {
//   e.preventDefault();
// });
// document.addEventListener("contextmenu", function (e) {
//   e.preventDefault();
// });
