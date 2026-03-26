

from models.strategy_model import AnalysisStrategy

class DataAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: AnalysisStrategy):
        self._strategy = strategy
    
    def execute(self, data):
        return self._strategy.analyze(data)