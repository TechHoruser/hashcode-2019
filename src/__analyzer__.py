from src import DataVisualizer
from src import Entities

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
    {
        "plot": "coordinates",
        "elements": [
            {"coordinate": "coordinateA"},
        ],
    },
    {
        "plot": "coordinates",
        "elements": [
            {"coordinate": "coordinateB"},
        ],
    },
    {
        "plot": "coordinates",
        "elements": [
            {"coordinate": "coordinateA"},
            {"coordinate": "coordinateB"},
        ],
    },
    {
        "plot": "boxes",
        "elements": [
            {"numeric": "number1"},
        ],
    },
    {
        "plot": "boxes",
        "elements": [
            {"numeric": "number2"},
        ],
    },
    {
        "plot": "box",
        "elements": [
            {"numeric": "number1"},
            {"numeric": "number2"},
        ],
    },
    {
        "plot": "boxes",
        "elements": [
            {"numeric": "number1"},
            {"numeric": "number2"},
        ],
    },
])

collection.addElements(
    {"number1": 1, "typeA": 1},
    {"number1": 2, "coordinateA": Entities.Coordinate(1,1), "typeA": 2},
    {"number1": 3, "coordinateA": Entities.Coordinate(3,3), "typeA": 1},
    {"number1": 3, "coordinateA": Entities.Coordinate(1,3), "typeA": 2},
    {"number2": 2, "number1": 2, "coordinateA": Entities.Coordinate(3,1), "typeA": 3},
    {"number2": 3, "number1": 6, "coordinateA": Entities.Coordinate(1,2), "typeA": 5,"typeB": 0,},
    {"number2": 5, "coordinateA": Entities.Coordinate(2,1), "coordinateB": Entities.Coordinate(2,2), "typeA": 1},
    {"coordinateB": Entities.Coordinate(2,3), "typeA": 1},
    {"coordinateB": Entities.Coordinate(3,2), "typeA": 2},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 3},
)

DataVisualizer.DataVisualizer.getPdf('example',collection)