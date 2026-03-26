

from models.strategy_model import AnalysisStrategy


class MedianStrategy(AnalysisStrategy):
    def analyze(self, data):
        shorted_data = sorted(data)
        n = len(shorted_data)
        if n % 2 == 0:
            median = (shorted_data[n//2 - 1] + shorted_data[n//2]) / 2
        else:
            median = shorted_data[n//2]
        return f"Mediana: {median}"
    
