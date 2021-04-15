# Stock market prediction using various machine learning models

This repo contain code and implementation for Stacked LSTM, Logistic Regression, Random Forest, Naïve Bayes, Linear Support Vector Machine and Non-Linear Support Vector Machine.

### Method

We have used NLP using historical News data with these algorithms: Logistic Regression, Random Forest, Naïve Bayes, Linear Support Vector Machine and Non-Linear Support Vector Machine.

And we have done Time-seris analysis with current data using Stacked LSTM model.


## Requirements

Python Anaconda(preffered), tensorflow v2, pandas, numpy, keras, sklearn, datetime, matplotlib, seaborn
Account in Tiingo for API key (only used in Stacked LSTM model)


## Data Scraping

### Historical News Data for NLP

We use The Guardian's API to gather the historical News data to be used for NLP for all algorithms (except Stacked LSTM).

### Recent Stock data Data

In order to gather Recent/Historical stock data (like open, close, date, high, low, volume), we use [Tingoo's API](https://https://api.tiingo.com/) to scrape the data.


## Prediction 

Run the desired .ipynb according to the algorithm you need to implement.

## Result

Here is the Accuracy graph of our project:

![ScaledGraph](https://github.com/MithasKumar/Stock-market-prediction-using-various-machine-learning-models/Images/ScaledGraph.png)

## License

The underlying code of this project is licensed under the MIT license.
