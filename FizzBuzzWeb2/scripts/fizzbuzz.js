/**
 * Yay for fizzbuzz
 **/

$(document).ready(function() {

    $("#start-button").on("click", function() {
        console.log("start buttong clicked")
        let data = get_inputs()
        fizzBuzz(data)
    })
});

function get_inputs() {
    data = {}
    inputs = $("#controls").find("input")

        .each(function() {
            if ($(this).attr("type") == "number") {

                data[$(this).attr("id")] = parseInt($(this).val())
            } else {
                data[$(this).attr("id")] = $(this).val()
            }
        })

    return data
}

function fizzBuzz(data) {
    console.log(data)
}
