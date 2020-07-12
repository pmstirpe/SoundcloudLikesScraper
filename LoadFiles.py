import glob
import re
from datetime import datetime






# Load filenames into List
fileNames = glob.glob("../SoundcloudLikesScraper/output/*.csv")

 

# Updates locNEW to the most recent CSV and locOLD to the next most recent CSV
# Define variables to be loaded

def init():
    locOLD=""
    locNEW=""
    dateNEW = datetime(2018,5,12).date()

    for file in fileNames:
        date_unformatted_string = file.split("~")[1].split("-")[0]
        date_obj = datetime.strptime(date_unformatted_string, '%Y%m%d').date()
        if (date_obj > dateNEW):
            locOLD = locNEW
            locNEW = file
            dateNEW = date_obj
    return (locNEW,locOLD)
     

