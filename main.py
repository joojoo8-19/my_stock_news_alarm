from kakao_manager import KakaoManager
from news_manager import NewsManager
from stock_manager import StockManager
from email_manager import EmailManager
import yfinance

stock_manager = StockManager()
news_manager = NewsManager()
email_manager = EmailManager()
kakao_manager = KakaoManager()

high_change_stocks = stock_manager.stocks_over_5pct_change()

for ticker in stock_manager.tickers:
    company = yfinance.Ticker(ticker).info["longName"]

    articles = news_manager.fetch_news(q=ticker)

    email_subject = f"{company} news today "
    email_contents = f""

    for article in articles:
        email_contents += (f"{article.title} by {article.author} | written {article.published_at}\n"
                           f"{article.description}\n"
                           f"{article.url}\n"
                           f"\n")

    email_manager.send_email_to_me(subject=email_subject, contents=email_contents)
    kakao_manager.send_message(contents=email_contents)

if len(high_change_stocks) == 0:
    pass
else:
    for stock in high_change_stocks:
        company = yfinance.Ticker(stock.symbol).info["longName"]
        articles = news_manager.fetch_news(q=stock.symbol)

        email_subject = f"{company} stocks value changed 5% today "
        email_contents = f""

        for article in articles:
            email_contents += (f"{article.title} by {article.author} | written {article.published_at}\n"
                               f"{article.description}\n"
                               f"{article.url}\n"
                               f"\n")

        email_manager.send_email_to_me(subject=email_subject, contents=email_contents)
        kakao_manager.send_message(contents=email_contents)
