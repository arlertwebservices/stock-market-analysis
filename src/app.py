import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime, timedelta

# Setup
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# Streamlit app
st.title("Stock Market Analysis Dashboard")
st.write("Analyze stock prices, trends, and portfolio performance for selected stocks.")

# Sidebar inputs
st.sidebar.header("Stock Selection")
tickers = st.sidebar.multiselect(
    "Select Stocks",
    options=["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"],
    default=["AAPL", "TSLA"],
)
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", datetime.now())


# Fetch data
@st.cache_data
def fetch_stock_data(tickers, start_date, end_date):
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)[
            "Adj Close"
        ]
        if data.empty:
            st.warning("No data fetched from yfinance. Using sample data.")
            return load_sample_data()
        return data
    except Exception as e:
        st.warning(f"Error fetching data from yfinance: {e}. Using sample data.")
        return load_sample_data()


def load_sample_data():
    try:
        sample_data = pd.read_csv(
            "C:/Users/user/Documents/stock-market-analysis/data/sample_stock_data.csv",
            index_col="Date",
            parse_dates=True,
        )
        return sample_data
    except FileNotFoundError:
        st.error("Sample data not found. Please create data/sample_stock_data.csv.")
        st.stop()


if tickers:
    df = fetch_stock_data(tickers, start_date, end_date)
    st.write("Data loaded successfully")
    st.write(
        f"Data source: {'yfinance' if 'fetch_stock_data' in str(fetch_stock_data.__code__) else 'sample CSV'}"
    )

    # Save raw data
    df.to_csv("C:/Users/user/Documents/stock-market-analysis/data/raw_stock_data.csv")

    # EDA
    st.subheader("Exploratory Data Analysis")
    st.write("Summary Statistics:")
    st.dataframe(df.describe())
    st.write("Missing Values:")
    st.write(df.isnull().sum())

    # Price trend
    st.subheader("Stock Price Trends")
    fig, ax = plt.subplots(figsize=(10, 6))
    for ticker in tickers:
        if ticker in df.columns:
            ax.plot(df.index, df[ticker], label=ticker)
    ax.set_title("Stock Price Trends")
    ax.set_xlabel("Date")
    ax.set_ylabel("Adjusted Close Price ($)")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.savefig("C:/Users/user/Documents/stock-market-analysis/figures/price_trend.png")
    plt.close()

    # Moving averages
    st.subheader("50-Day vs. 200-Day Moving Averages")
    for ticker in tickers:
        if ticker in df.columns:
            df[f"{ticker}_MA50"] = df[ticker].rolling(window=50).mean()
            df[f"{ticker}_MA200"] = df[ticker].rolling(window=200).mean()
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df.index, df[ticker], label=f"{ticker} Price")
            ax.plot(df.index, df[f"{ticker}_MA50"], label="50-Day MA")
            ax.plot(df.index, df[f"{ticker}_MA200"], label="200-Day MA")
            ax.set_title(f"{ticker} Moving Averages")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price ($)")
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
            plt.savefig(
                f"C:/Users/user/Documents/stock-market-analysis/figures/moving_averages_{ticker}.png"
            )
            plt.close()

    # Portfolio simulation
    st.subheader("Portfolio Performance (Equal Weights)")
    valid_tickers = [t for t in tickers if t in df.columns]
    if valid_tickers:
        weights = [1 / len(valid_tickers)] * len(valid_tickers)
        daily_returns = df[valid_tickers].pct_change().dropna()
        portfolio_returns = (daily_returns * weights).sum(axis=1)
        cumulative_returns = (1 + portfolio_returns).cumprod() - 1
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(cumulative_returns.index, cumulative_returns * 100)
        ax.set_title("Portfolio Cumulative Returns")
        ax.set_xlabel("Date")
        ax.set_ylabel("Cumulative Return (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        plt.savefig(
            "C:/Users/user/Documents/stock-market-analysis/figures/portfolio_returns.png"
        )
        plt.close()
    else:
        st.warning("No valid tickers for portfolio simulation.")

    # Save processed data
    df.to_csv(
        "C:/Users/user/Documents/stock-market-analysis/data/processed_stock_data.csv"
    )
    st.write("Processed data and plots saved.")
else:
    st.warning("Please select at least one stock.")
