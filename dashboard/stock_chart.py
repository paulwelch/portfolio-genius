from datetime import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import mplfinance as mpf
import yfinance as yf
import panel as pn

pn.extension()


def _get_daily_history(symbol: str) -> pd.DataFrame:
    data = yf.download(symbol, interval="1d", start=datetime.now() - relativedelta(years=3),
                       end=datetime.now().strftime("%Y-%m-%d"))
    # TODO: convert this to MA indicator
    # TODO: add ability to add/remove indicators to chart
    # add MA indicators
    data["15_MA"] = data["Adj Close"].rolling(window=15).mean()
    data["50_MA"] = data["Adj Close"].rolling(window=50).mean()
    data["200_MA"] = data["Adj Close"].rolling(window=200).mean()
    return data


def generate_chart(symbol: str) -> pn.pane.Matplotlib:
    data = _get_daily_history(symbol)

    start_row = len(data.index) - 252  # 12 months

    ma_15 = mpf.make_addplot(data["15_MA"].iloc[start_row:], color="orange")
    ma_50 = mpf.make_addplot(data["50_MA"].iloc[start_row:], color="green")
    ma_200 = mpf.make_addplot(data["200_MA"].iloc[start_row:], color="red")

    mpl_fig = mpf.plot(data.iloc[start_row:],
                       returnfig=True,
                       # title=f"{symbol} - 1Y Daily",
                       figscale=0.6,
                       fontscale=0.5,
                       scale_padding=0.0,
                       figratio=(8.00, 6.0),
                       type="candle",
                       style="charles",
                       volume=True,
                       ylabel="",
                       ylabel_lower="",
                       tight_layout=False,
                       addplot=[ma_15, ma_50, ma_200],
                       )[0]

    for ax in mpl_fig.axes:
        ax.set_facecolor("white")

    pane = pn.pane.Matplotlib(
        mpl_fig,
        interactive=False,
        format="svg",
        fixed_aspect=True,
        sizing_mode="stretch_both",
        styles={"background": "white", "border": "0px"},
    )
    return pane
