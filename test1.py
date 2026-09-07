import yfinance as yf
import requests
import time

stock = ["1101", "2330"] 

for stockid in stock:
    # 透過 yfinance 取得最新股價
    ticker = yf.Ticker(f"{stockid}.TW")
    # 抓取今天(1d)的歷史資料，取最後一筆收盤價，並轉為小數點後兩位的字串
    try:
        latest_price = ticker.history(period="1d")['Close'].iloc[-1]
        price = f"{latest_price:.2f}"
    except Exception as e:
        price = "無法取得報價"
    
    message = f"股票 {stockid} 即時股價為 {price}"
    
    # 用 telegram bot 回報股價
    token = "8857059421:AAEL2cGLCzUSRVmqxBL61ozGo9y85af1LAo"
    chat_id = "8802148190"
    
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    
    time.sleep(3)
