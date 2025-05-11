/**
 * Yay for fizzbuzz
 **/

$(document).ready(function() {

    $("#start-button").on("click", function() {
        console.log("start buttong clicked")
        $("#game-input-dialog")[0].showModal()
    })

    $("#push-me").on("click", function() {

        $("#game-input-dialog")[0].close()
    })

});

