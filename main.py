
from models.data_analyzer import DataAnalyzer
from models.mean import MeanStrategy
from models.median import MedianStrategy
from models.lianeal_regresion import LinearRegressionStrategy

def mostrar_menu():
    print("\n=== MENÚ DE ESTRATEGIAS DE ANÁLISIS ===")
    print("1. Media (MeanStrategy)")
    print("2. Mediana (MedianStrategy)")
    print("3. Regresión Lineal (LinearRegressionStrategy)")
    print("4. Salir")
    return input("Seleccione una estrategia: ")

def main():
    data = [10, 20, 30, 40, 50]
    analyzer = DataAnalyzer(MeanStrategy())
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            analyzer.set_strategy(MeanStrategy())
            print(f"\nResultado: {analyzer.execute(data)}")
            
        elif opcion == "2":
            analyzer.set_strategy(MedianStrategy())
            print(f"\nResultado: {analyzer.execute(data)}")
            
        elif opcion == "3":
            analyzer.set_strategy(LinearRegressionStrategy())
            print(f"\nResultado: {analyzer.execute(data)}")
            
        elif opcion == "4":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()