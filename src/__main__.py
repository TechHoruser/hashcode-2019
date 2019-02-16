from time import sleep
from src.ManagerFile import ManagerFile
from src.Algorithms import BaseAlgorithms


examples = [
    {'fileName': 'a_example', 'algorithm': 'basic', },
    {'fileName': 'b_should_be_easy', 'algorithm': 'basic', },
    {'fileName': 'd_metropolis', 'algorithm': 'basic', },
    {'fileName': 'e_high_bonus', 'algorithm': 'basic', },
]

for indx, example in enumerate(examples):
    print('Processing file:',example['fileName'],'('+str(indx+1)+'/'+str(len(examples))+')', flush=False)
    mf = ManagerFile(example['fileName'])
    inputArray = mf.loadFile()

    solution = eval('BaseAlgorithms.'+example['algorithm']+'(inputArray)')

    outputArray = solution

    mf.saveFile(outputArray)

    sleep(0.5)

