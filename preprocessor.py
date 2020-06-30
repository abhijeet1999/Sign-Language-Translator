import os
import shutil

inputdir= 'NoFilterModeDataSet/'
outputdir='hand_dataset/'
listing = os.listdir(inputdir) 
listing.sort()
os.mkdir(outputdir)
l=['Aboard', 'All_Gone', 'Baby', 'Beside', 'Book', 'Bowl', 'Bridge', 'Camp', 'Cartridge', 'Eight', 'Five', 'Fond', 'Four', 'Friend', 'Glove', 'Hang', 'High', 'House', 'How_Many', 'IorMe', 'Man', 'Marry', 'Meat', 'Medal', 'Mid_Day', 'Middle', 'Money', 'Moon', 'Mother', 'Nine', 'One', 'Opposite', 'Prisoner', 'Ring', 'Rose', 'See', 'Seven', 'Short', 'Six', 'Superior', 'Ten', 'Thick', 'Thin', 'Three', 'Tobacco', 'Two', 'Up', 'Watch', 'Write', 'You']
for i in l:
    os.mkdir(outputdir+i)
    for j in listing:
        if i in j:
            shutil.copy(inputdir+j, outputdir+i)
        