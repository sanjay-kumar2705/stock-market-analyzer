import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st

# Page config 
st.set_page_config(page_title="Stock Market Analysis", page_icon="📊", layout="wide")

st.title("📈 Stock Market Analysis")
st.markdown("**Analyze stock data with interactive charts**")


st.sidebar.title("**🔍 Filters**")
tickers = {
    "Apple": "AAPL",
    "Microsoft":"MSFT",
    "Nvidia":"NVDA",
    "Amazon":"AMZN",
    "Google":"GOOG",
    "Meta/Facebook":"META",
    "Saudi Aramco":"2222.SR",
    "Broacom":"AVGO",
    "Taiwan Semiconductors":"TSM",
    "Berkshire Hathway":"BRK.A",
    "Tesla":"TSLA",
    "Eli Lilly":"LLY",
    "JP Morgan":"JPM",
    "Wallmart": "WMT",
    "Visa":"V",
    
}
company = st.sidebar.selectbox("Select Company", list(tickers.keys()))
ticker = tickers[company]


start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))


# Fetch Data
data = yf.download(ticker, start=start_date, end=end_date)

# --------flattening the columns
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [col[0] for col in data.columns]


if not data.empty:

      latest_price = data["Close"].iloc[-1]
      prev_close = data["Close"].iloc[-2] if len(data) > 1 else latest_price
      delta = latest_price - prev_close

    # Show stock price in sidebar
      st.sidebar.metric(label=f"{company} Current Price", 
                      value=f"${latest_price:.2f}", 
                      delta=f"{delta:.2f}")


    # Tabs
      tab1, tab2, tab3, tab4, tab5 = st.tabs([ "🏠 Home", "📊 Price", "📦 Volume", "📉 Moving Average", "📑 Data Table", ])

      with tab1:
         st.subheader("👋 Introduction")
         st.write("""
                 ### 📊 Welcome to the Stock Market Analyzer!

                 - ✅ **Track stock prices** of the **top 15 global companies** in real-time .
                 - 🔍 **View detailed insights** including:
                     - Opening and closing prices 📈📉 
                     - Volume of stocks sold 📦
                     - Moving averages for trend analysis 🔄
                     - Data Table for deep study of stock 📑
                 - 📈 Get the **current stock price** of your favorite company in real-time!
                 - ⚙️ **Easily choose** your desired **stock ticker** from the sidebar settings.
                 - 📌 **Analyze** trends, and get a quick overview of stock performance.
                 - 🚀 Designed to help you make **smarter investment decisions** at a glance.
                 """)
         st.success("NOTE-: Apple Ticker is selected bydefault")

         with tab2:
    #    Opening Price
           st.subheader(f"{ticker} Opening Price")
           fig = px.line(data, x=data.index, y="Open", title=f"{ticker} Opening Price", template="plotly_dark")
           st.plotly_chart(fig, use_container_width=True)

       # Closing Price
           st.subheader(f"{ticker} Closing Price")
           fig = px.line(data, x=data.index, y="Close", title=f"{ticker} Closing Price", template="plotly_dark")
           st.plotly_chart(fig, use_container_width=True)




      with tab3:
        st.subheader("Volume Traded")
        fig2 = px.bar(data, x=data.index, y="Volume", title="Daily Volume", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

      with tab4:
        st.subheader("50-Day Moving Average")
        data['MA50'] = data['Open'].rolling(50).mean()
        fig3 = px.line(data, x=data.index, y=["Open", "MA50"], 
                       labels={"value": "Price", "variable": "Legend"}, 
                       title="Opening Price vs 50-Day MA", template="plotly_dark")
        st.plotly_chart(fig3, use_container_width=True)



        st.subheader("50-Day Moving Average")
        data['MA50'] = data['Close'].rolling(50).mean()
        fig3 = px.line(data, x=data.index, y=["Close", "MA50"], 
                       labels={"value": "Price", "variable": "Legend"}, 
                       title="Closing Price vs 50-Day MA", template="plotly_dark")
        st.plotly_chart(fig3, use_container_width=True)

      with tab5:
        st.subheader("Raw Data")
        st.dataframe(data.tail(500).style.highlight_max(axis=0))

      
else:
      st.warning("⚠ No data found. Try another ticker.")
           








