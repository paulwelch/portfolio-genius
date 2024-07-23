from flask import Flask, jsonify, request
from langgraph_workflow import AgentWorkflow

backend_app = Flask(__name__)


@backend_app.route('/health', methods=['GET'])
def index():
    return jsonify({"status": "Running"}), 200


@backend_app.route('/analyze_portfolio', methods=['POST'])
def analyze_portfolio():
    data = request.json
    workflow = AgentWorkflow()
    analysis = workflow.run(data["portfolio"])
    return jsonify({"path": analysis}), 200
