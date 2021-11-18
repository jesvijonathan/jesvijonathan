function delay(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

document.onreadystatechange = function () {
  if (document.readyState == "complete") {
    document.querySelector("#load-fill").style.visibility = "hidden";
    //    document.querySelector("#loader").style.visibility = "hidden";
    // document.querySelector("#loader-text").style.visibility = "hidden";
  } else {
    document.querySelector("#load-fill").style.visibility = "visible";

    //    document.querySelector("#loader").style.visibility = "visible";
    // document.querySelector("#loader-text").style.visibility = "visible";
  }
};

document.onreadystatechange = function () {
  if (document.readyState == "complete") {
    document.querySelector(".loading").style.visibility = "hidden";
    document.querySelector(".mini-loadering").style.visibility = "hidden";
  } else {
    document.querySelector(".loading").style.visibility = "visible";
    document.querySelector(".mini-loadering").style.visibility = "visible";
  }
};
