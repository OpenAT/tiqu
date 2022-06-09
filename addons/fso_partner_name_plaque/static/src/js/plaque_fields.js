/**
 * Created on 09.06.22.
 */
function checkValuesToggleFields(amountLimit, classname) {
    var donationvalue = document.querySelector('[name="price_donate"]').value;
    var donationvalueToInt = parseInt(donationvalue);

    var objElements = document.getElementsByClassName(classname);

    for (index = 0; index < objElements.length; index++) {

        var element = objElements[index];
        if (donationvalueToInt > amountLimit) {
            element.classList.remove("hidden");
        }
        else {
            element.classList.add("hidden");
        }
}

/*    var element1 = document.getElementsByClassName("plaque")[0];
    var element2 = document.getElementsByClassName("plaque")[1];

    if (donationvalueToInt > 20) {
        element1.classList.remove("hidden");
        element2.classList.remove("hidden");
    }
    else {
        element1.classList.add("hidden");
        element2.classList.add("hidden");
    }*/
}
$(document).ready( function() {
    checkValuesToggleFields(20, "plaque");
    /*const queryString = window.location.search;*/
    //console.log("url: ", queryString); // ?tiqu_plaque_value=True
    /*const urlParams = new URLSearchParams(queryString);*/
    //console.log("Parametercheck: ", urlParams.has('tiqu_plaque_value')); // true
    // if we wanna be dynamic for the value additionally use this parameter
/*    if ( urlParams.has('tiqu_plaque_value') ) {
        const tiquplaqueParamter = urlParams.get('tiqu_plaque_value')
        //console.log("paramteronly: ", tiquplaqueParamter);
        if ( tiquplaqueParamter ) {
            //this class needs to be added in the "plaque-1 and plaque-2" at name plaue line 1 and 2 
            //document.querySelector('.plaque-*').style.display = 'none'
            //teurer als nur display none
            var element1 = document.getElementsByClassName("plaque-1")[0];
            //console.log("element:", element);
            //var element = $(this).find('.company-web');
            element1.classList.add("hidden");
            //to unhide, really remove the class or better only display none or block .... for performance reasons?
            //this class needs to be added in the "shopfields" at company web
            //document.querySelector('.company-web').style.display = 'none'
            var element1 = document.getElementsByClassName("plaque-2")[0];
            //var element = $(this).find('.wita-em');
            element1.classList.add("hidden");
        }
    }*/
/*    var element1 = document.getElementsByClassName("plaque")[0];
    var element2 = document.getElementsByClassName("plaque")[1];

    if (donationvalueToInt > 20) {
        element1.classList.remove("hidden");
        element2.classList.remove("hidden");
    }*/
});

$("#price_donate").on("change keyup paste", function(){
        checkValuesToggleFields(20, "plaque");

/*    var donationvalue = document.querySelector('[name="price_donate"]').value;
    var donationvalueToInt = parseInt(donationvalue);
    console.log("donationvalueInt: ", donationvalueToInt)
    var element1 = document.getElementsByClassName("plaque")[0];
    var element2 = document.getElementsByClassName("plaque")[1];

    console.log("element: ", element1, element2);
//    for (index = 0; index < element.length; index++) {
        console.log("element", element1, element2);
        if (donationvalueToInt > 20) {
            element1.classList.remove("hidden");
            element2.classList.remove("hidden");
        }
        else {
            element1.classList.add("hidden");
            element2.classList.add("hidden");
        }*/
  //  }
    //console.log("donationvalue evented: ", donationvalue);
});