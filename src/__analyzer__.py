from src import DataVisualizer

collection = DataVisualizer.StructureCollection([
    {
        "plot": "bar",
        "elements": [
            {"type": "typeA"},
        ],
    },
    {
        "plot": "bar",
        "elements": [
            {"type": "typeB"},
        ],
    },
    {
        "plot": "bar",
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
    {"typeB": 0},
    {"typeA": 1},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 3},
)

DataVisualizer.DataVisualizer.getPdf('example',collection)