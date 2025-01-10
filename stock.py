import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer!")

stock_name = st.text_input("Which stock do you want to analyze?", "MSFT")

ticker_data = yf.Ticker(stock_name)

start_date = st.date_input("What should be the start date", datetime.date(2024, 1, 1))

end_date = st.date_input("What should be the end date", datetime.date(2025, 1, 1))

ticker_df = ticker_data.history(period = "1d", start = start_date, end = end_date)

st.subheader("This is the raw day wise stock price.")
st.dataframe(ticker_df.head())

st.subheader("Price movement over time")
st.line_chart(ticker_df['Close'])

st.subheader("Volume movement over time")
st.line_chart(ticker_df['Volume'])