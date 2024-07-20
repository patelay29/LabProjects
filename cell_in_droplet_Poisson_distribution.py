# 2023-07-18 Poisson distribution for cell encapsulation

import matplotlib.pyplot as plt
import numpy as np
import math

# this class takes in cell conentration of the solution entering the microfluidics device 
# and the desired diameter of the microgel produced by the microfluidics device, 
# and outputs the stastical value of important lambda, whic is, in this case, avg cells per droplet
class Lambda:
    def __init__(self, cellConcentration, diameter):
        self.cellConcentration = cellConcentration
        self.diameter = diameter
        self.nmCellConcentration = cellConcentration / 1000
        self.volume = ((4 / 3) * (math.pi) * (diameter / 2) ** 3) / 1000000
        self.Lam = self.nmCellConcentration * self.volume


    def setCellConcentration(self, cellConcentration):
        self.cellConcentration = cellConcentration

    def setDiameter(self, diameter):
        self.diameter = diameter

    def printCurrentUnits(self):
        print("lambda has cell concentration: {} cells/uL and diameter: {} um" \
              .format(self.cellConcentration, self.diameter))

    def printLambdaParameters(self):
        print("lambda has cell concentration: {} cells/nL and volume: {} nL" \
              .format(self.nmCellConcentration, self.volume))

    def printLambda(self):
        print("lambda: {} avg cells per droplet" \
              .format(self.Lam))





# list lambda is able to plot probability distributions that correspond with various lambdas, which 
# could be determined by the characteristics of the experiment, or necessary characteristics could be determined 
# by a desired lambda using solveLambda definition
class listLambda:
    def __init__(self):
        self.listRawLambda = []
        self.listLambda = []

    def addLambda(self, Lambda):
        if Lambda not in self.listLambda:
            self.listRawLambda.append(Lambda)
            self.listLambda.append(Lambda.Lam)

    def printLambda(self):
        for i in self.listRawLambda:
            i.printLambda()

    def printLambdaDetails(self):
        for i in self.listRawLambda:
            i.printLambda()
            i.printLambdaParameters()
            i.printCurrentUnits()
            print("--")

    def printLambdaList(self):
        for i in self.listLambda:
            print("{}" \
                  .format(i))
            print("--")
    def solveLambda(self, wantedLambda, diameter):
        volume = ((4 / 3) * (math.pi) * (diameter / 2) ** 3) / 1000000
        nmcellConcentration = wantedLambda/volume
        cellConcentration = nmcellConcentration*1000
        var = Lambda(cellConcentration, diameter)
        var.printCurrentUnits()
        var.printLambdaParameters()
        answer = input("Do you want to add this to List of Lambda's being plotted?")
        if answer == "yes":
            self.listRawLambda.append(var)
            self.listLambda.append(var.Lam)


    def plot(self,x1,x2):
        x = np.arange(x1,x2+1,0.01).tolist()
        y = []
        yIn = []
        legend = []
        for j in self.listLambda:
            for i in x:
                prob = (math.exp(-j))*((j**i)/(math.gamma(i+1)))
                yIn.append(prob)
            y.append(yIn)
            yIn = []
        for i in self.listRawLambda:
            legend.append("{} cells/\u03BCL, d = {} \u03BCm, \u03BB = {} avg cells per droplet".format(round(i.cellConcentration,2), round(i.diameter,2), round(i.Lam, 2)))
        for i in y:
            plt.plot(x,i)
        plt.legend(legend,fontsize='large')
        plt.xlabel("Cells per Droplet",fontsize='large')
        plt.xlim(x1,x2)
        plt.title("Poisson Distribution: Automated Microgel Production",fontweight='bold', fontsize='large')
        plt.ylabel("Probability",fontsize='large')
        save = input("Do you want to save plot?")
        if save == "yes":
            file = input("file name: ")
            aspect_ratio = 16/9
            fig = plt.gcf()
            fig.set_size_inches(fig.get_size_inches() * aspect_ratio)
            plt.savefig(file, dpi=300)
            plt.show()
        else:
            plt.show()












cells=listLambda()
# add in lambdas that correspond with experimental setup
cells.addLambda(Lambda(300,500))
cells.addLambda(Lambda(500,400))
cells.addLambda(Lambda(480,380))
cells.addLambda(Lambda(200,700))
cells.addLambda(Lambda(1000,400))
# plots between 0 to 70 avg cells/droplet
cells.plot(0,70)

cellsSmall = listLambda()
# add in desired lambda values (1, 2, 3, 4 avg cells/droplet) with the droplet diameter
# desired in this experiment, the code will then output the cell concentrations needed to achieve this, 
# and ask if you want to add this to the list of lambdas that will each create its respective poisson curves
cellsSmall.solveLambda(1,400)
cellsSmall.solveLambda(2,400)
cellsSmall.solveLambda(3,400)
cellsSmall.solveLambda(4,400)
cellsSmall.plot(0,8)

