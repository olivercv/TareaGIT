# Diagrama de Clases - Patrón Strategy (Formato Texto Mejorado)

```
                    ╔═══════════════════════════════════════╗
                    ║          AnalysisStrategy             ║
                    ║           <<abstract>>                ║
                    ║                                       ║
                    ║  + analyze(data: list): string        ║
                    ╚═══════════════════════════════════════╝
                                   ▲
                                   │
                                   │ Herencia
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            │                      │                      │
╔═══════════════════╗  ╔═══════════════════╗  ╔═════════════════════════=╗
║   MeanStrategy    ║  ║  MedianStrategy   ║  ║ LinearRegressionStrategy ║
║                   ║  ║                   ║  ║                          ║
║ + analyze(data):  ║  ║ + analyze(data):  ║  ║ + analyze(data):         ║
║   string          ║  ║   string          ║  ║   string                 ║
╚═══════════════════╝  ╚═══════════════════╝  ╚═════════════════════════=╝

╔═════════════════════════════════════════════════════════════════════════╗
║                           DataAnalyzer                                  ║
║                                                                         ║
║  Atributos:                                                             ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  - _strategy: AnalysisStrategy                                          ║
║                                                                         ║
║  Métodos:                                                               ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  + __init__(strategy: AnalysisStrategy)                                 ║
║  + set_strategy(strategy: AnalysisStrategy)                             ║
║  + execute(data: list): string                                          ║
╚═════════════════════════════════════════════════════════════════════════╝
                                   │
                                   │ Usa (Composición)
                                   │ 1..1
                                   ▼
                    ╔═══════════════════════════════════════╗
                    ║          AnalysisStrategy             ║
                    ║         (Polimorfismo)                ║
                    ╚═══════════════════════════════════════╝
```

## Descripción del Modelo

### Clase Abstracta: AnalysisStrategy
```
┌─────────────────────────────────────┐
│        AnalysisStrategy             │
│         <<abstract>>                │
│                                     │
│  + analyze(data): string            │
└─────────────────────────────────────┘
```
- **Propósito**: Define la interfaz común para todas las estrategias
- **Método**: `analyze(data)` - método abstracto que deben implementar todas las estrategias

### Contexto: DataAnalyzer
```
┌─────────────────────────────────────┐
│         DataAnalyzer                │
│                                     │
│  - _strategy: AnalysisStrategy      │
│                                     │
│  + __init__(strategy: AnalysisStrategy)│
│  + set_strategy(strategy: AnalysisStrategy)│
│  + execute(data): string            │
└─────────────────────────────────────┘
```
- **Atributo privado**: `_strategy` - referencia a la estrategia actual
- **Constructor**: inicializa con una estrategia específica
- **set_strategy()**: permite cambiar la estrategia en tiempo de ejecución
- **execute()**: delega el análisis a la estrategia actual

### Estrategias Concretas

#### MeanStrategy
```
┌─────────────────────────────────────┐
│         MeanStrategy                │
│                                     │
│  + analyze(data): string            │
└─────────────────────────────────────┘
```
- **Función**: Calcula la media aritmética de los datos

#### MedianStrategy
```
┌─────────────────────────────────────┐
│        MedianStrategy               │
│                                     │
│  + analyze(data): string            │
└─────────────────────────────────────┘
```
- **Función**: Calcula la mediana de los datos

#### LinearRegressionStrategy
```
┌─────────────────────────────────────┐
│   LinearRegressionStrategy          │
│                                     │
│  + analyze(data): string            │
└─────────────────────────────────────┘
```
- **Función**: Calcula la regresión lineal de los datos

## Relaciones y Flujo

1. **Herencia** (▲): MeanStrategy, MedianStrategy y LinearRegressionStrategy heredan de AnalysisStrategy
2. **Composición** (│ Usa): DataAnalyzer contiene una referencia a AnalysisStrategy
3. **Polimorfismo**: DataAnalyzer puede trabajar con cualquier estrategia concreta a través de la interfaz común

## Flujo de Ejecución

```
Cliente → DataAnalyzer.execute(data) → Strategy.analyze(data) → Resultado
```

El cliente interactúa siempre con DataAnalyzer, que delega el trabajo específico a la estrategia activa.
