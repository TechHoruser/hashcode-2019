from scipy import spatial
from src.Entities import *
from collections import deque, namedtuple
import numpy as np

class BaseAlgorithms:

    @classmethod
    def basic(cls, photoList) -> SlideShow:

        slides = []
        for idx, photo in photoList.items():
            #if photo.type == Photo.H:
            slides.append(Slide(photo))
            #else
            #    buscar

        #comenzamos en la primera y buscamos en bucle la proxima que daria ams puntuacion

        slideShow = SlideShow()
        slideShow.addSlide(slides[0])
        slideActual = slides[0]

        while len(slideShow.slides) != len(slides):
            maxSlide = None
            maxScore = -1
            for slideComparando in slides:
                score = Utils.calcScoreBetweenSlides(slideActual, slideComparando)
                if score > maxScore:
                    maxSlide = slideComparando
                    maxScore = score

            slideShow.addSlide(maxSlide)
            slideActual = maxSlide

        return slideShow


class Utils:
    @classmethod
    def diffTags(cls, tags1, tags2):
        return set(tags1) - set(tags2)

    @classmethod
    def intersectTags(cls, tags1, tags2):
        return (set(tags1) - set(tags2)) | (set(tags2) - set(tags1))

    @classmethod
    def unionTags(cls, tags1, tags2):
        return set(tags1) | (set(tags2) - set(tags1))

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

