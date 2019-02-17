from src import DataVisualizer

collection = DataVisualizer.StructureCollection([
    {
        "plot": "bars",
        "elements": [
            {"type": "typeA"},
        ],
    },
    {
        "plot": "bars",
        "elements": [
            {"type": "typeB"},
        ],
    },
    {
        "plot": "bars",
        "elements": [
            {"type": "typeA"},
            {"type": "typeB"},
        ],
    },
])

collection.addElements(
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 3},
    {"typeA": 5,"typeB": 0,},
    {"typeA": 1},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 3},
)

DataVisualizer.DataVisualizer.getPdf('example',collection)