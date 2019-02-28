class Photo:
    H = 0
    V = 1

    def __init__(self, id, type, tags = []):
        self.id = id
        self.type = type
        self.tags = tags

class Slide:
    def __init__(self, photo1, photo2):
        self.photo1 = photo1
        self.photo2 = photo2

class SlideShow:
    def __init__(self, slides = []):
        self.slides = slides


    def addSlide(self, slide : Slide):
        self.slides.append(slide)

    def getStringToFile(self):
        output = str(len(self.slides));
        for slide in self.slides:
            output

