from abc import ABC, abstractmethod

# ============================
# Strategy (Interfaz)
# ============================
class AnalysisStrategy(ABC):

    # Define la interfaz para las estrategias de análisis.
    
    @abstractmethod
    def analyze(self, data):
        pass