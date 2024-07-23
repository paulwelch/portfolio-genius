
class PortfolioManager:
    def __init__(self):
        pass

    def manage_portfolio(self, query: str, sources: list):
        print(f'********* PORTFOLIO MANAGER QUERY: {query} SOURCES: {sources}')

        prompt = [{
            "role": "system",
            "content": "You are a portfolio manager responsible for requesting information from your team of analysts "
                       "and using their input to compute a recommendation for portfolio assets. Your sole purpose is "
                       "to analyze stock market information provided by analysts, define an investment strategy based "
                       "on them, and calculate the stocks and quantities that should be in the portfolio.\n "
        }, {
            "role": "user",
            "content": f"TODO: write prompt content\n "
        }]

        response = f"TODO: call model"
        return response