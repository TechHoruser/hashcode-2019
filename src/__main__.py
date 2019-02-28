from time import sleep
from src.ManagerFile import ManagerFile
from src.Algorithms import *
from src.Entities import *

examples = [
    # {'fileName': 'a_example', 'algorithm': 'basic', },
    {'fileName': 'b_lovely_landscapes', 'algorithm': 'basic', },
    # {'fileName': 'c_memorable_moments', 'algorithm': 'basic', },
    # {'fileName': 'd_pet_pictues', 'algorithm': 'basic', },
    # {'fileName': 'e_shiny_selfies', 'algorithm': 'basic', },
]

def transformInputArray(lines):
    photoList = {}
    for idx, val in enumerate(lines):
        if idx == 0:
            continue

        photoType = Photo.H if val[0] == 'H' else Photo.V
        photoList[int(idx)] = Photo(idx, photoType, val[2:])


    return photoList


for indx, example in enumerate(examples):
    print('Processing file:',example['fileName'],'('+str(indx+1)+'/'+str(len(examples))+')', flush=False)
    mf = ManagerFile(example['fileName'])
    inputArray = mf.simpleLoadFile()

    photoList = transformInputArray(inputArray)

    #TODO creamos slides
    slides = []
    for photo in photoList:
        #if photo.type == Photo.H:
        slides.append(Slide(photo))
        #else
        #    buscar

    #comenzamos en la primera y buscamos en bucle la proxima que daria ams puntuacion

    solucion = [slides[0]]
    slideActual = slides[0]

    while len(solucion) != len(slides):
        maxSlide = None
        maxPuntuacion = -1
        for slideComparando in slides:
            if Utils.calcScoreBetweenSlides(slideActual, slideComparando) > maxPuntuacion:
                maxSlide = slideComparando
                maxPuntuacion = Utils.calcScoreBetweenSlides(slideActual, slideComparando)
        solucion.append(maxSlide)
        slideActual = maxSlide
    slideShow = SlideShow(solucion)
    solution = eval('BaseAlgorithms.'+example['algorithm']+'(inputArray)')

    # outputArray = solution
    #
    # mf.saveFile(outputArray)

    sleep(0.5)
