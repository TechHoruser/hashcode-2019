from scipy import spatial
from src.Entities import *
from collections import deque, namedtuple
import numpy as np
import random

class BaseAlgorithms:

    @classmethod
    def basic(cls, photoList) -> SlideShow:

        slides = []
        verticalPhotos = []

        for idx, photo in photoList.items():
            if photo.type == Photo.H:
                slides.append(Slide(photo))
            else:
                verticalPhotos.append(photo)

        if len(verticalPhotos) > 0:
            minTags = float('inf')
            bestVPhoto = None
            photoActual = verticalPhotos[0]
            verticalPhotos.remove(verticalPhotos[0])
            for vPhoto in verticalPhotos:
                score = len(Utils.intersectTags(photoActual.tags, vPhoto.tags))
                if score < minTags:
                    bestVPhoto = vPhoto
                    minTags = score

            verticalPhotos.remove(bestVPhoto)
            slides.append(Slide(photoActual, bestVPhoto))

        slideShow = SlideShow([])
        slideShow.addSlide(slides[0])
        slideActual = slides[0]
        slides.remove(slides[0])

        while len(slides)>0:
            print(len(slides))
            maxSlide = None
            maxScore = -1
            numeroRandom = 1000
            if len(slides)<numeroRandom:
                numeroRandom=len(slides)
            for slideComparando in random.sample(slides, numeroRandom):
            #for slideComparando in slides:
                score = Utils.calcScoreBetweenSlides(slideActual, slideComparando)
                if score > maxScore:
                    maxSlide = slideComparando
                    maxScore = score

            slides.remove(maxSlide)
            slideShow.addSlide(maxSlide)
            slideActual = maxSlide

        return slideShow


class Utils:

    @classmethod
    def diffTags(cls, tags1, tags2):
        return tags1 - tags2

    @classmethod
    def intersectTags(cls, tags1, tags2):
        return (tags1 - tags2) | (tags2 - tags1)

    @classmethod
    def unionTags(cls, tags1, tags2):
        return tags1 | (tags2 - tags1)

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

