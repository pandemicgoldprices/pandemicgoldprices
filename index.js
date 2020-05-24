
var myButton = d3.select("#myButton");
var myButtonTwo = d3.select("#myButtonTwo");

var selectedButton = 1;

myButton.on("click", function() {

    selectedButton = 1

    renderPlot(selectedButton)

});



myButton.on("click", function() {

    selectedButton = 1

    renderPlot(selectedButton)

});



myButtonTwo.on("click", function() {

    selectedButton = 2

    renderPlot(selectedButton)

});
