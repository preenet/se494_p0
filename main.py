# Course: SE494 Data Mining for SE
# Author: Pree Thiengburanathum
# Email: pree.t@cmu.ac.th
"""
 Description:
 This program is for demonstrating how to read a simple data file and do basic matrix calculation
 using python programming languauge v3
 Note: Student are not allowed to use numpy to construct the matrix
"""
import nltk
from nltk.tokenize import word_tokenize
numOfMonthPerSeason = 3

def itemGetter(a):
        return a[1]

print('Read data file...')
# Reading data line from the given text file
dataFileLine = []
try:
    fileOBJ = open('data.txt', 'r')
    while True:
        dataLine = fileOBJ.readline()
        dataLine = dataLine.rstrip('\r\n')

        if dataLine == '':
            break
        dataFileLine.append( dataLine )
except IOError as e:
    print ('ERROR: could not read file:', e)
    exit(1)

numCol = len( word_tokenize(dataFileLine[0]) )
numRow = len( dataFileLine )

# Check for equal distribuite of months per season
numOfSeason = numCol/numOfMonthPerSeason
if (numCol % numOfSeason) > 0:
    print('season errror')
    exit(1)


# Calculate city temperature average
matrix = [[0 for x in range(numCol)] for y in range(numRow)]
cityTempAvgList = []
tempAvg = 0

for i in range (numRow):
    tmp = word_tokenize(dataFileLine[i])
    for j in range (numCol):
        matrix[i][j] = int(tmp[j])
        tempAvg += matrix[i][j]
    cityTempAvgList.append(tempAvg/numCol)
    tempAvg = 0


# Calculate average temperature for each month
monthTempAvgList = []
tmpAvg = 0

print()

for i in range (numCol):
    for j in range (numRow):
        tmpAvg += matrix[j][i] 
    monthTempAvgList.append(tmpAvg/numRow)
    tmpAvg = 0

x = [i for i in range(numOfMonthPerSeason, 12+1, numOfMonthPerSeason)]

seasonTempAvgList = []
tmpAvg = 0
seasonNum = 0
for i in range( len(monthTempAvgList) ):
    if i in x:
        tmpAvg += monthTempAvgList[i]
        seasonNum = seasonNum + 1
        s = ('Season '+ str(seasonNum), tmpAvg/numOfMonthPerSeason)
        seasonTempAvgList.append(s)
        tmpAvg = 0
    else:
        tmpAvg += monthTempAvgList[i]

seasonTempAvgList = sorted(seasonTempAvgList, key=itemGetter)



# display results
for i in range(len(cityTempAvgList)):
    print('City:', i+1,'Temp AVG = ', round(cityTempAvgList[i], 2))

for i in range(len(monthTempAvgList)):
    print('Month', i+1,'Temp AVG = ', round(monthTempAvgList[i], 2))

print()
print('Min = ', seasonTempAvgList[1])
print('Max = ', seasonTempAvgList[-1])

desc = sorted(seasonTempAvgList, key=itemGetter, reverse = True)

print (desc)
