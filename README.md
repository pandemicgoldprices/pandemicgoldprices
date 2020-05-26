# pandemicgoldprices

Compiling data and analysing it and presenting it to answer the question " How will the covid 19 pandemic influence the price of gold in relation to the DOW "


fred-gold-dow-api.ipynb uses this repo : https://github.com/mortada/fredapi
to get it working : 
1) from a terminal window in the directory where you launch the notebook $ pip install fredapi
2) visit https://research.stlouisfed.org/useraccount/apikey and get yourself an api key 
3) in the first cell of the notebook add your key into the "my_key" variable between the inverted commas :
my_key = ""
fred = Fred(api_key=my_key)
restart and run the notebook 

