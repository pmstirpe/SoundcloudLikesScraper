# Reading an excel file using Python 
import xlrd
import LoadFiles 
import io

# List comparison  
def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

FILESBITCH = LoadFiles.init()

print("Comparing files")
print("NEW: " + FILESBITCH[1])
print("OLD: " + FILESBITCH[0])

# Give the location of the file 
locOLD = FILESBITCH[0]
locNEW = FILESBITCH[1]
  
# open both workbooks
wbOLD = xlrd.open_workbook(locOLD) 
wbNEW = xlrd.open_workbook(locNEW) 
sheetOLD = wbOLD.sheet_by_index(0) 
sheetNEW = wbNEW.sheet_by_index(0) 
  

# Load older version list 
songListOLD = []
for i in range(1,sheetOLD.nrows): 
    artist = sheetOLD.row_values(i)[0]
    song = sheetOLD.row_values(i)[1]
    songListOLD.append(artist + " " + song)

# Load newer version list
songListNEW = []
for i in range(1,sheetNEW.nrows): 
    artist = sheetNEW.row_values(i)[0]
    song = sheetNEW.row_values(i)[1]
    songListNEW.append(artist + " " + song)

differnce = Diff(songListOLD,songListNEW)
print("There are " + str(len(differnce)) + " differences between files")

with io.open("output.txt", "w", encoding="utf-8") as f:
    for line in differnce:
        f.write(line + "\n")