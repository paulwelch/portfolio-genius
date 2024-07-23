import os
import time
from concurrent.futures import ThreadPoolExecutor
from langgraph.graph import Graph

from .agents import PortfolioManager, Reviewer, TechnicalAnalyst, FundamentalAnalyst


class AgentWorkflow:
    def __init__(self):
        self.output_dir = f"outputs/run_{int(time.time())}"
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, queries: list, layout: str):
        portfolio_manager_agent = PortfolioManager()
        reviewer = Reviewer()
        technical_analyst_agent = TechnicalAnalyst()
        fundamental_analyst_agent = FundamentalAnalyst()

        workflow = Graph()

        workflow.add_node("portfolio_manager", portfolio_manager_agent.run)
        workflow.add_node("reviewer", reviewer.run)
        workflow.add_node("technical_analyst", technical_analyst_agent.run)
        workflow.add_node("fundamental_analyst", fundamental_analyst_agent.run)

        workflow.add_edge('manage', 'analyze_technicals')
        workflow.add_edge('manage', 'analyze_fundamentals')
        # TODO: analyze news, events
        workflow.add_edge('analyze_technicals', 'review')
        workflow.add_edge('analyze_fundamentals', 'review')
        # TODO: fan-in and wait for all results
        workflow.add_conditional_edges(source='review',
                                       path=(lambda x: "accept" if x['review'] is None else "revise"),
                                       path_map={"accept": "recommend", "revise": "manage"})

        workflow.set_entry_point("manage")
        workflow.set_finish_point("recommend")

        chain = workflow.compile()

        with ThreadPoolExecutor() as executor:
            parallel_results = list(executor.map(lambda q: chain.invoke({"query": q}), queries))

        portfolio_recommendation = reviewer_agent.run(parallel_results)

        return portfolio_recommendation
