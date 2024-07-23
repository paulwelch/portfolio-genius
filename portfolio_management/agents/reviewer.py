
class Reviewer:
    def __init__(self):
        pass

    def review(self, query: str, sources: list):
        print(f'********* REVIEWER QUERY: {query} SOURCES: {sources}')

        prompt = [{
            "role": "system",
            "content": "You are a senior stock market analyst responsible for review the analyst team recommendations. "
                       "Your sole purpose is to analyze the recommendations from the analyst team and provide an "
                       "approval or recommendations on how the recommendations could be better.\n "
        }, {
            "role": "user",
            "content": f"TODO: write prompt content\n "
        }]

        response = f"TODO: call model"
        return response