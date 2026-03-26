
from models.strategy_model import AnalysisStrategy

class MeanStrategy(AnalysisStrategy):
    def analyze(self, data):
        result = sum(data) / len(data)
        return f"Media: {result}"
