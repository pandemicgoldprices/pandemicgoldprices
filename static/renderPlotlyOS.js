
function DJIAGoldRatioPlot(myDiv, data) {

    // Data Sample:
    // [{'_id': ObjectId('5ed42e9f4d18271a686d4b89'), 'year': 1918, 'month': 'Jan', 'dow_average': '75.66', 'month_int': 1, 'gold_price':
    // 19.84, 'DOW_div_gold': 3.81374808, 'dow_div_gold_monthly_change': 0.28}, {'_id': ObjectId('5ed42e9f4d18271a686d4b8a'), 'year': 19
    // 18, 'month': 'Feb', 'dow_average': '79.83', 'month_int': 2, 'gold_price': 19.84, 'DOW_div_gold': 4.0235635080000005, 'dow_div_gold
    // _monthly_change': 0.21}

    months = []
    dowOverGoldChange = []
   
    data.forEach(i => {
      months.push(i.year + "/" + i.month_int)
      dowOverGoldChange.push(i.dow_div_gold_monthly_change)
    });
  
    let trace = {
      x: months,
      y: dowOverGoldChange,
      mode: 'lines+markers',
      type: 'scatter',
      marker: {
        color: 'rgb(255, 215, 0)'
      },
      line: {
        color: 'rgb(255, 215, 0)'
      }
    };
  
    let plotData = [trace];
  
    let layout = {
      xaxis: {
        title: 'Months'
      },
      yaxis: {
        title: "DJIA/Gold Prices Ratio"
      }
    };
  
    Plotly.newPlot(myDiv, plotData, layout);
  };