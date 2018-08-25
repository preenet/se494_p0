# Course: SE494 Data Mining for SE
# Author: Pree Thiengburanathum
# Email: pree.t@cmu.ac.th
"""
 Description:
 This program is for demonstrating how to read a simple data file and do basic matrix calculation
 and simple segmentation using Python v3
 Note: Student are not allowed to use numpy to construct the matrix
"""
import nltk
from nltk.tokenize import word_tokenize
numOfMonthPerSeason = 3

def itemGetter(a):
        return a[1]

print('Read data file...')
# Read data line from the given text file
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
for i in range (numCol):
    tmpAvg = 0
    for j in range (numRow):
        tmpAvg += matrix[j][i] 
    monthTempAvgList.append(tmpAvg/numRow)

# Generate end of season 
x = [i for i in range(numOfMonthPerSeason-1, numCol+1, numOfMonthPerSeason)]

seasonTempAvgList = []
tmpAvg = 0
seasonNum = 1

# Caculate for each season
for i in range( numCol ):
    tmpAvg += monthTempAvgList[i]
    if(i in x):
        seasonTempAvgList.append( ('Season ' + str(seasonNum), tmpAvg/numOfMonthPerSeason )) 
        tmpAvg = 0
        seasonNum += 1

seasonTempAvgList = sorted(seasonTempAvgList, key=itemGetter)   

# Display results

for i in range(len(cityTempAvgList)):
    print('City:', i+1,'Temp AVG =  ', round(cityTempAvgList[i], 2), '\u00B0C', end ='\n')

print('\nMin = ' + str(seasonTempAvgList[0][0]), '= ', round(seasonTempAvgList[0][1], 2), '\u00B0C')
print('Max = ' + str(seasonTempAvgList[-1][0]), '= ', round(seasonTempAvgList[-1][1], 2), end = '\u00B0C\n\n')

desc = sorted(seasonTempAvgList, key=itemGetter, reverse = True)

print('Average Temperture of seasons from high to low:')
seq = []
for i in range(len(desc)):
    seq.append( str(desc[i][0]) + "= " + str(round(desc[i][1], 2)) +'\u00B0C' ) 
joined = ' > '.join(seq)
print (joined)    

print('Program terminated properly!')
