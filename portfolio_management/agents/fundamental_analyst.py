
class FundamentalAnalyst:
    def __init__(self):
        pass

    def analyze(self, query: str, sources: list):
        print(f'********* FUNDAMENTAL ANALYST QUERY: {query} SOURCES: {sources}')

        prompt = [{
            "role": "system",
            "content": "You are a stock market analyst specializing in company fundamentals. Your sole purpose is "
                       "to analyze the stock market and provide a short summary of the current market conditions.\n "
        }, {
            "role": "user",
            "content": f"TODO: write prompt content\n "
        }]

        response = f"TODO: call model"
        return response