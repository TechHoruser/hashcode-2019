from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages

class StructureCollection:
    def __init__(self, linkData):
        self.linkData = linkData
        self.dataArray =[]

    def addElements(self, *elements):
        for element in elements:
            self.dataArray.append(element)

class DataVisualizer:
    @classmethod
    def getPdf(cls, filename:str, collection:StructureCollection):
        pp = PdfPages('../data/'+filename+'.pdf')
        for link in collection.linkData:
            for linkElement in link['elements']:
                eval('DataVisualizer.plot'+link['plot']+'(linkElement,collection.dataArray)')
            pyplot.savefig(pp, format='pdf')
            pyplot.close()
        pp.close()

    @classmethod
    def plotbar(cls,link,dataArray):
        sumArray = {}
        for element in dataArray:
            if link['type'] not in element:
                continue

            if element[link['type']] in sumArray:
                sumArray[element[link['type']]] += 1 if 'numeric' not in link else element['numerics'][link['numeric']]
            else:
                sumArray[element[link['type']]] = 1

        pyplot.title(link['type'])
        pyplot.bar(sumArray.keys(), sumArray.values())

