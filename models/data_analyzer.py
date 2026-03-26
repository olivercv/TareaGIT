

from models.strategy_model import AnalysisStrategy

class DataAnalyzer:
    def __init__(self, strategy: AnalysisStrategy):

        # Inicializa el DataAnalyzer con una estrategia de análisis.

        self._strategy = strategy
    
    def set_strategy(self, strategy: AnalysisStrategy):
        # Permite cambiar la estrategia de análisis en tiempo de ejecución.
        self._strategy = strategy
    
    def execute(self, data):
        # Ejecuta el análisis utilizando la estrategia actual.
        return self._strategy.analyze(data)