# pandemicgoldprices

We are compiling data, analyzing it, and presenting it in order to answer the following question (in a statistical manner): "*How will the COVID-19 pandemic influence the price of gold in relation to the Dow Jones Industrial Average?*"  

List of pandemics to be studied:  
1918–1920: Spanish Flu (H1N1) - Ognjen S.  
1957–1958: Asian Flu (H2N2) - Tyler N.  
1968–1969: Hong Kong Flu - Luis R.  
2009–2010: Swine Flu (H1N1) - Todd M.  
2019-Present: COVID-19 - Sean W.

**Note:**  
The Jupyter Notebook file "fred-gold-dow-api.ipynb" uses this repository: https://github.com/mortada/fredapi.
To get it working:  
1) from a terminal window in the directory where you launch the notebook, do a $pip install fredapi  
2) visit https://research.stlouisfed.org/useraccount/apikey and get yourself an API key  
3) in the first cell of the notebook, add your key into the "my_key" variable between the inverted commas; so "my_key = ''", "fred = Fred(api_key=my_key)", and finally restart and run the notebook
