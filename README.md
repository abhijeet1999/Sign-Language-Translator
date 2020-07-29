# Sign-Language-Translator

## Problem Description
The barrier of communication between deaf, mute and others who do not know sign language, as we generally need a translator for understanding their language.
We propose an app which can convert sign language in real time into voice or text

## Indian Sign Language Dataset
Due to unavailability of Indian Sign language dataset (ISL), We have created dataset of 5000 images. Data set contains 100 images each for 50 Indian signs. Improvements, suggestions and accuracy statistics on your algorithms are welcomed. Dataset can be downloaded from
https://drive.google.com/drive/folders/1mHmmmSaU5ZV8QKIUSCF0fabVv54HhxWq?usp=sharing

There are 3 type of Dataset 
- NoFilterModeDataSet
- AdaptiveThresholdModeDataSet
- SiftModeDataSet


### Classes ( 50 Signs )
**['Aboard', 'All_Gone', 'Baby', 'Beside', 'Book', 'Bowl', 'Bridge', 
'Camp','Cartridge', 'Eight', 'Five', 'Fond', 'Four', 
'Friend', 'Glove', 'Hang','High', 'House', 'How_Many',
 'IorMe', 'Man', 'Marry', 'Meat', 'Medal','Mid_Day', 'Middle',
 'Money', 'Moon', 'Mother', 'Nine', 'One', 'Opposite','Prisoner', 
'Ring', 'Rose', 'See', 'Seven', 'Short','Six', 'Superior',
 'Ten', 'Thick', 'Thin', 'Three', 'Tobacco', 'Two', 'Up', 'Watch', 'Write', 'You']**


## Model 
#### resnet50-transfer-learning

## How to Use System
### - Instal everything in Requirment.txt
### - Run **preprocessor.py** to extract the data classwise from Dataset
### - Run **sign_train.py** for Training the Data
# OUTPUT
## For NoFilterModeDataSet
   ### Training 
   Train loss: 0.0952325779944658 -- Acurracy: 97.0238095238095184%
   ### Testing
   Test Loss: 0.017252  -- Test Accuracy (Overall): 97% (991/1020)
## How to run:- demo.py
### demo.py 'imagepath' --mod 'model path'
 Default model path is NoFilter.pth
### eg:  demo.py img.png --mod model.pth
# Team Members
## [Abhijeet C](https://github.com/abhijeet1999)
## [Bharath T U](https://github.com/5hade5layer)

DOI : https://doi.org/10.1007/978-3-030-00665-5_72


