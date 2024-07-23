from stock_chart import generate_chart
from portfolio import Portfolio

import panel as pn

pn.extension()

port = Portfolio()

template = pn.template.FastGridTemplate(
    title="Portfolio Genius",
    prevent_collision=True,
    save_layout=False,
    theme_toggle=True,
    corner_radius=5,
    neutral_color="#000000",
    theme="default",
)

symbols = pn.widgets.Select(name="Stock", options=port.symbols, value="TSLA")
quote_box = pn.bind(
    port.generate_quote_box, symbol=symbols
)
chart_pane = pn.bind(
    generate_chart, symbol=symbols
)
tabs = pn.Tabs(("1YR Daily", chart_pane), ("Genius", chart_pane))

template.main[0:1, 0:4] = symbols
template.main[0:1, 7:9] = quote_box
template.main[1:5, :] = tabs

if pn.state.served:
    print("Serving app...")
    template.servable()
