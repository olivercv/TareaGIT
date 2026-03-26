
from models.strategy_model import AnalysisStrategy

class LinearRegressionStrategy(AnalysisStrategy):
    def analyze(self, data):
        n = len(data)
        x = [i for i in range(n)]
        y = data
        
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
        
        if denominator == 0:
            return "No se puede calcular la regresión lineal"

        m = numerator / denominator
        b = mean_y - m * mean_x
        
        return f"Regresión lineal: y = {m:.2f}x + {b:.2f}"

