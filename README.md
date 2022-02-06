# Final-project

This projects aim is to create a simple financial dashboard monitoring the stock market price of selected firms in the last 30 trading days.
The dashboard consists of 5 cards, 2 of them show the current value of financial indexes. The other 3 show price evolution Microsoft, Apple and Tesla stocks as well as their return on equity, return on assets and debt to equity ratios.
The stock prices are automatically updated every day, to update the value of indexes the code needs to be re-run.

## How to run
1. download the depository
2. open the view_code.ipynb in Jupyter Notebook
3. if neccesary, install packages mentioned in the first cell (Jupyter Dash requires JupyterLab version 2.0 or above)
4. run the notebook
5. the dashboard will appear within the notebook

## Note:
The api is limited to 100 requests per day. In case of depletion, anyone can obtain free personal key from the Yahoo finance api and rewrite it in Url_Information.JSON
