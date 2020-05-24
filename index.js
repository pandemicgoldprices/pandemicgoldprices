<<<<<<< HEAD
var myButton = d3.select("#myButton");
var myButtonTwo = d3.select("#myButtonTwo")

var selectedButton = 1

myButton.on("click", function() {

    selectedButton = 1

    renderPlot(selectedButton)

});

myButtonTwo.on("click", function() {

    selectedButton = 2

    renderPlot(selectedButton)

=======
var myButton = d3.select("#myButton");
var myButtonTwo = d3.select("#myButtonTwo")

var selectedButton = 1

myButton.on("click", function() {

    selectedButton = 1

    renderPlot(selectedButton)

});

myButtonTwo.on("click", function() {

    selectedButton = 2

    renderPlot(selectedButton)

>>>>>>> 2251c79e3f08eddc4e5b4faace0417255cc6f6af
});