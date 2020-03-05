# Reading an excel file using Python 
import xlrd 

# List comparison  
def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

# Give the location of the file 
locOLD = "SoundcloudLikes~23-2-2020.xls"
locNEW = "SoundcloudLikes~3-4-2020.xls"
  
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

for line in differnce:
    print (line)