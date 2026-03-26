from abc import ABC, abstractmethod

# ============================
# Strategy (Interfaz)
# ============================
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data):
        pass