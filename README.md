# Stock Market Analysis Dashboard

This project creates an interactive Streamlit dashboard to analyze historical stock prices, visualize trends and technical indicators (e.g., moving averages), and simulate portfolio performance for selected stocks (e.g., Apple, Tesla, Microsoft). It uses Python and the `yfinance` library to fetch stock data from Yahoo Finance.

## Features

- Fetches historical stock data for user-selected tickers.
- Performs exploratory data analysis (EDA) with summary statistics and missing value checks.
- Visualizes stock price trends, 50-day and 200-day moving averages.
- Simulates an equal-weight portfolio and plots cumulative returns.
- Interactive Streamlit dashboard for selecting stocks and date ranges.
- Saves processed data and visualizations for portfolio documentation.

## Prerequisites

- Python 3.12
- Git
- Required libraries (listed in `requirements.txt`)

## Setup

1. Clone the repository:

   git clone https://github.com/arlertwebservices/stock-market-analysis.git
   cd stock-market-analysis

2. Install dependencies:

   pip install -r requirements.txt

3. Run the Streamlit app:

   cd src
   streamlit run app.py

   - Open `http://localhost:8501` in your browser to view the dashboard.

4. (Optional) Run the Jupyter notebook for detailed analysis:

   cd notebooks
   jupyter notebook analysis.ipynb

## Folder Structure

stock-market-analysis/
├── data/
│ ├── raw*stock_data.csv
│ ├── processed_stock_data.csv
├── figures/
│ ├── price_trend.png
│ ├── moving_averages*[ticker].png
│ ├── portfolio_returns.png
├── notebooks/
│ ├── analysis.ipynb
├── src/
│ ├── app.py
├── requirements.txt
├── README.md

## Outputs

- **Raw Data**: `data/raw_stock_data.csv` (fetched stock prices).
- **Processed Data**: `data/processed_stock_data.csv` (includes moving averages).
- **Visualizations**:
  - `figures/price_trend.png`: Stock price trends for selected tickers.
  - `figures/moving_averages_[ticker].png`: Moving averages per stock.
  - `figures/portfolio_returns.png`: Portfolio cumulative returns.
- **Streamlit Dashboard**: Interactive app with EDA, plots, and portfolio simulation.

## Results

(To be updated with screenshots)

- Stock Price Trends: [Add screenshot]
- Moving Averages: [Add screenshot]
- Portfolio Returns: [Add screenshot]
- Streamlit Dashboard: [Add screenshot]

## License

MIT License

If you experience issues with having to dowload the required info from yfinance you can use the sample data and the fallback app.py script in the fallback folder to aid your analysis.
