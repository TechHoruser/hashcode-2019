from scipy import spatial
from src.Entities import *
from collections import deque, namedtuple
import numpy as np

class BaseAlgorithms:

    @classmethod
    def basic(cls, input) -> SlideShow:
        # TODO
        output = ... # type: SlideShow

        return output


class Utils:
    @classmethod
    def diffTags(cls, tags1, tags2):
        return tags1 - tags2

    @classmethod
    def intersectTags(cls, tags1, tags2):
        return tags1 - tags2 + tags2 - tags1

    @classmethod
    def unionTags(cls, tags1, tags2):
        return tags1 + tags2 - tags1

    @classmethod
    def calcScoreBetweenSlides(cls, slide1, slide2):
        return min(
            len(Utils.diffTags(slide1.getTags(), slide2.getTags())),
            len(Utils.unionTags(slide1.getTags(), slide2.getTags())),
            len(Utils.diffTags(slide2.getTags(), slide1.getTags())),
        )

    @classmethod
    def calculateCost(cls, inputArray):
        return None

