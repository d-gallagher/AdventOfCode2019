def calcFuel(mass):
    return (mass // 3) - 2


infile = open("Day1/input.txt", "r")
totalmass = 0
for line in infile.readlines():
    modulemass = calcFuel(int(line.strip()))
    totalmass += modulemass
    while calcFuel(modulemass) > 0:
        modulemass = calcFuel(modulemass)
        totalmass += modulemass


print(totalmass)
