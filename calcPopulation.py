startPopulation = int(input("Start size: "))

while startPopulation < 9:
    startPopulation = int(input("Start size: "))

endSize = int(input("End Size: "))

while endSize < startPopulation:
    endSize = int(input("End Size: "))


# Calculation
bornPop = int(startPopulation / 3)
dPop = int(startPopulation / 4)
endYearPop = startPopulation + bornPop - dPop
# secondYear = oneYear + int((oneYear/3)) - int((oneYear/4))
# reqGoal = int(endSize % oneYear)
yearPassed = 0

while endYearPop < endSize:
    endYearPop = endYearPop + int(endYearPop/3) - int(endYearPop/4)
    yearPassed = yearPassed + 1


print(startPopulation, endSize, bornPop, dPop, endYearPop, yearPassed)
