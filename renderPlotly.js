

/// a function which renders new plots based on what is passed in
function renderPlots(plot) {


    switch(plot) {

        case(1):

            var xData = [1, 2, 3]
            var yData = [4, 5, 6]
            let trace1 = {
                x: xData,
                y: yData,
                mode: 'lines+markers',
                type: 'scatter'
            };

            let plotData1 = [trace1];

            Plotly.newPlot('myPlot', plotData1);
            break;

        case(2):

            var xData2 = [1, 2, 3]
            var yData2 = [6, 7, 8]
            let trace2 = {
                x: xData2,
                y: yData2,
                mode: 'lines+markers',
                type: 'scatter'
            };

            let plotData2 = [trace2];

            Plotly.newPlot('myPlot2', plotData2);
            break;
    }
}