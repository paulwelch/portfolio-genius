import yfinance as yf
import panel as pn


class Portfolio:
    symbols = []

    def __init__(self):
        # TODO: add persistence and load
        self.symbols = ["AAPL", "AMZN", "MSFT", "TSLA", "GOOGL", "META", "NVDA"]

    def _get_basic_info(self, symbol: str) -> dict:
        ticker_data = yf.Ticker(symbol)
        return ticker_data.info

    def _get_quote_box(self, bid: int, ask: int) -> pn.GridBox:
        quote_bid = pn.pane.HTML("<strong><p>Bid</p><p>" + str(bid) + "</p></strong>",
                                 styles={"background": "#FF3333", "text-align": "center", "color": "black"}, width=65,
                                 height=90)
        quote_ask = pn.pane.HTML("<strong><p>Ask</p><p>" + str(ask) + "</p></strong>",
                                 styles={"background": "#66FF66", "text-align": "center", "color": "black"}, width=65,
                                 height=90)
        return pn.GridBox(quote_bid, quote_ask, ncols=2, sizing_mode="stretch_both", margin=(0, 0, 0, 0))

    def generate_quote_box(self, symbol: str) -> pn.GridBox:
        basic_info = self._get_basic_info(symbol)
        box = self._get_quote_box(basic_info["bid"], basic_info["ask"])
        return box


