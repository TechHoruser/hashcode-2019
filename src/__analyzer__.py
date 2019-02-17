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
])

collection.addElements(
    {"typeA": 1},
    {"coordinateA": Entities.Coordinate(1,1), "typeA": 2},
    {"coordinateA": Entities.Coordinate(3,3), "typeA": 1},
    {"coordinateA": Entities.Coordinate(1,3), "typeA": 2},
    {"coordinateA": Entities.Coordinate(3,1), "typeA": 3},
    {"coordinateA": Entities.Coordinate(1,2), "typeA": 5,"typeB": 0,},
    {"coordinateA": Entities.Coordinate(2,1), "coordinateB": Entities.Coordinate(2,2), "typeA": 1},
    {"coordinateB": Entities.Coordinate(2,3), "typeA": 1},
    {"coordinateB": Entities.Coordinate(3,2), "typeA": 2},
    {"typeA": 1},
    {"typeA": 2},
    {"typeA": 1},
    {"typeA": 3},
)

DataVisualizer.DataVisualizer.getPdf('example',collection)