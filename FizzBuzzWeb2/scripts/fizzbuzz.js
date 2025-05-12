/**
 * Yay for fizzbuzz
 */

$(document).ready(function() {

    $("#start-button").on("click", function() {
        let data = get_inputs()
        if (!bValid(data)) {
            console.log("invalid data:")
            console.log(data)
            return
        }
        $(this).hide()
        fizzBuzz(data)
    });

    $("#factor-one").on("input", function() {
        dynamicUpdate($(this), $("#output-number-one"), { preText: "if divisible by", postText: ":" })
    });

    $("#word-one").on("input", function() {
        dynamicUpdate($(this), $("#output-word-one"));
    });

    $("#factor-two").on("input", function() {
        dynamicUpdate($(this), $("#output-number-two"), { preText: "if divisible by", postText: ":" })
    });

    $("#word-two").on("input", function() {
        dynamicUpdate($(this), $("#output-word-two"), { preText: " " });
    });

    $("#reset-all").on("click", function() {
        resetAll()
    })

});

function dynamicUpdate(source, destination, extras) {
    if (source == null || source == undefined) {
        console.log("missing source")
        return
    }

    if ($(source).val() == "" || $(source).val() == NaN) {
        $(destination).empty();
        return
    }

    var pre = "";
    var text = $(source).val()
    var post = "";

    if (extras != undefined) {
        pre = extras.preText ? extras.preText + " " : ""
        post = extras.postText ? " " + extras.postText : ""
    }

    $(destination).text(`${pre}${text}${post}`)

}

/**
 * Gets the inputs.
 *
 * @returns {object} the input data
 */
function get_inputs() {
    data = {}
    inputs = $("#controls")  // get the controls div
        .find("input")       // find the inputs in the controls div
        .each(function() {   // act on each of the inputs

            if ($(this).attr("data-type") == "number") {
                data[$(this).attr("name")] = parseInt($(this).val())
            } else {
                data[$(this).attr("name")] = $(this).val()
            }
        })

    return data
}

function fizzBuzz(data) {
    for (let i = 1; i <= data.playTo; i++) {
        console.log(`${i} is prime: ${isPrime(i)}`)
        let result = ""
        if (i % data.factorOne == 0) {
            result = result + data.wordOne
        }
        if (i % data.factorTwo == 0) {
            result = result + data.wordTwo
        }

        result = result ? result : i

        let resultContainer = $("<p>")
        $(resultContainer).text(result)
        switch (result) {
            case data.wordOne:
                $(resultContainer).addClass("optOne")
                break;
            case data.wordTwo:
                $(resultContainer).addClass("optTwo")
                break;
            case `${data.wordOne}${data.wordTwo}`:
                $(resultContainer).addClass("combined")
                break;
        }

        $("#results-output").append(resultContainer)
        // console.log(result)
    }
}

/**
 * Validates that the data is valid for use.
 *
 * @param {any} data The data to validate
 * @returns {boolean} `true` if valid, otherwise `false`
 */
function bValid(data) {
    if (isNaN(data.factorOne)) {
        return false
    }
    if (data.wordOne == "") {
        return false
    }
    if (isNaN(data.factorTwo)) {
        return false
    }
    return true
}

/** 
 * Resets all the inputs and text displays
 */
function resetAll() {
    console.log("resetting")
    $("#controls")  // get the controls div
        .find("input")       // find the inputs in the controls div
        .each(function() {   // act on each of the inputs
            $(this).val('')
            $(this).val()
        });
    $("#dynamic-outputs")
        .find("span")
        .each(function() {
            $(this).empty()
        });

    $("#results-output").empty();

    $("#start-button").show();
}


/**
    * determines if a number is prime or not
    */
function isPrime(number) {

    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            return false
        }
    }
    return true
}
