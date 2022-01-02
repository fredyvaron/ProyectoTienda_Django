// $(document).ready(function() {
//     let tabs = document.querySelectorAll('.tabs');
//     let tabsHeader = document.querySelector(".tabs_header");
//     let tabsBody = document.querySelector(".tabs_body");
//     let tabsHeaderNodes = document.querySelectorAll(".tabs_header> div");
//     console.log(tabsHeaderNodes)
//     let tabsBodyNodes = document.querySelector(".tabs_body > div");
//     for (let i = 0; i < tabsHeaderNodes.length; i++) {
//         tabsHeaderNodes[i].addEventListener("click", function() {
//             tabsHeader.querySelector(".active").classList.remove("active")
//             console.log("entro 2");
//             tabsHeaderNodes[i].classList.add("active")
//             tabsBody.querySelector(".active").classList.remove("active")
//             tabsBodyNodes[i].classList.add("active")
//         });
//     }
// });

$(document).ready(function() {
    let tabHeader = document.getElementsByClassName("tabs_header")[0];
    let tabBody = document.getElementsByClassName("tabs_body")[0];
    let tabPane = tabHeader.getElementsByTagName("div");
    for (let i = 0; i < tabPane.length; i++) {
        tabPane[i].addEventListener("click", function() {
            tabHeader.getElementsByClassName("active")[0].classList.remove("active");
            tabPane[i].classList.add("active");

            tabBody.getElementsByClassName("active")[0].classList.remove("active");
            tabBody.getElementsByTagName("div")[i].classList.add("active");

        });
    }
});