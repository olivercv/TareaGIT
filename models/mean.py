
from models.strategy_model import AnalysisStrategy

class MeanStrategy(AnalysisStrategy):
    '''Estrategia concreta para calcular la media de un conjunto de datos.'''
    def analyze(self, data):
        result = sum(data) / len(data)
        return f"Media: {result}"
