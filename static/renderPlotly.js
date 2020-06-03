
function apiData(data){
  console.log(data)

}




function myFunc(vars) {
  return vars
}
/// a function which renders new plots based on what is passed in
function renderPlotsType1() {

    new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
        labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
        datasets: [{ 
            data: [86,114,106,106,107,111,133,221,783,2478],
            label: "Africa",
            borderColor: "#3e95cd",
            fill: false
            }
        ]
    },
    options: {
    title: {
        display: true,
        text: 'World population per region (in millions)'
    }
    }
})
}   





function renderPlotsType2(){

new Chart(document.getElementById("mixed-chart"), {
    type: 'bar',
    data: {
      labels: ["1900", "1950", "1999", "2050"],
      datasets: [{
          label: "Europe",
          type: "line",
          borderColor: "#8e5ea2",
          data: [408,547,675,734],
          fill: false
        }, {
          label: "Africa",
          type: "line",
          borderColor: "#3e95cd",
          data: [133,221,783,2478],
          fill: false
        }, {
          label: "Europe",
          type: "bar",
          backgroundColor: "rgba(0,0,0,0.2)",
          data: [408,547,675,734],
        }, {
          label: "Africa",
          type: "bar",
          backgroundColor: "rgba(0,0,0,0.2)",
          backgroundColorHover: "#3e95cd",
          data: [133,221,783,2478]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Population growth (millions): Europe & Africa'
      },
      legend: { display: false }
    }
})
}



/** a function which renders the dow/gold monthly change for a period of years */
/** divID is the id placeholder in the html div  */
function renderDowOverGoldPlot(divId, data){

  /*** data sample 
  [{'_id': ObjectId('5ed42e9f4d18271a686d4b89'), 'year': 1918, 'month': 'Jan', 'dow_average': '75.66', 'month_int': 1, 'gold_price':
  19.84, 'DOW_div_gold': 3.81374808, 'dow_div_gold_monthly_change': 0.28}, {'_id': ObjectId('5ed42e9f4d18271a686d4b8a'), 'year': 19
 18, 'month': 'Feb', 'dow_average': '79.83', 'month_int': 2, 'gold_price': 19.84, 'DOW_div_gold': 4.0235635080000005, 'dow_div_gold
 _monthly_change': 0.21},

 */

 

//chartData = myFunc({data})
console.log("data in plot function")
console.log(data)


 Months = []
 Change_in_DOWoverGold = []
 
data.forEach(e => {
  Months.push(e.year + "/" + e.month_int)
  Change_in_DOWoverGold.push(e.dow_div_gold_monthly_change)
  
});

let trace1 = {
  x: Months,
  y: Change_in_DOWoverGold,
  mode: 'lines+markers',
  type: 'scatter'
};

let plotData = [trace1];

Plotly.newPlot(divId, plotData);



}

/** a function to render monthly deaths in some pandemics 
 * arguments are the id of the div and the data passed in 
 */

function renderDeathsMonthly(divId, data){


 /**
  * {'_id': ObjectId('5ed5be86f621c1b0029d96b3'), 'Month': '2020/4', 'US_Deaths_per_100k': 21.6, 'dow_gold_change_next_month': 0.37}
  */

//chartData = myFunc({data})

console.log(data)


 Months = []
 Deaths = []
 
data.forEach(e => {
  Months.push(e.Month)
  Deaths.push(e.US_Deaths_per_100k)
  
});

let trace2 = {
  x: Months,
  y: Deaths,
  mode: 'lines+markers',
  type: 'scatter'
};

let plotData2 = [trace2];

Plotly.newPlot(divId, plotData2);



}



