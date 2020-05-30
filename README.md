# pandemicgoldprices

We are compiling data, analyzing it, and presenting it to answer the following question in a statistical manner: "How will the COVID-19 pandemic influence the price of gold in relation to the Dow Jones Industrial Average?"

"fred-gold-dow-api.ipynb" uses this repo: https://github.com/mortada/fredapi
To get it working:
1) from a terminal window in the directory where you launch the notebook, do a $pip install fredapi
2) visit https://research.stlouisfed.org/useraccount/apikey and get yourself an API key
3) in the first cell of the notebook, add your key into the "my_key" variable between the inverted commas; so "my_key = ''", "fred = Fred(api_key=my_key)", and finally restart and run the notebook

List of pandemics to be studied:
1899–1923: Sixth cholera pandemic
1918–1920: Spanish flu (H1N1)
1957–1958: Asian flu (H2N2)
1968–1969: Hong Kong flu
2009–2010: Swine flu (H1N1)
2019-Present: COVID-19
