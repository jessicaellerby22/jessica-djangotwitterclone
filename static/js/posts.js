////////////////////////////
// JavaScript for Posts page
////////////////////////////

$(function () {
    $('.js-menu-icon').click(function() {
        $(this).next().toggle();
    })
})

function myFunction(x) {
    x.classList.toggle("fa-thumbs-down");
    }