from src.Algorithms import *

class Photo:
    H = 0
    V = 1

    def __init__(self, id, type, tags = []):
        self.id = id
        self.type = type
        self.tags = tags

class Slide:
    def __init__(self, photo1, photo2 = None):
        self.photo1 = photo1
        self.photo2 = photo2

    def getTags(self):
        return self.photo1.tags if self.photo2 is None else Utils.unionTags(self.photo1.tags, self.photo2.tags)


class SlideShow:
    def __init__(self, slides = []):
        self.slides = slides


    def addSlide(self, slide : Slide):
        self.slides.append(slide)

    def getStringToFile(self):
        output = str(len(self.slides))+"\n"
        for slide in self.slides:
            if slide.photo2 is None:
                output += str(slide.photo1.id) + "\n"
            else:
                output += str(slide.photo1.id) + str(slide.photo2.id) + "\n"

