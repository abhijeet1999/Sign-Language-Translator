'''
Variable Comments
train_on_gpu  :  to check if device have  gpu or not
device        :  devioce we use (GPU/CPU)
classes       :  list of classes  
data_transform:  image transformation according to model
img           :  the argument that is passed
model         :  the model we used for transfer learning
img_loader    : to transform the img we get
prediction    : the prediction of class number
'''


import torchvision.models as models
from PIL import Image
from torch.autograd import Variable
import torch
import torch.nn as nn
import numpy 
from torchvision import  transforms
import argparse
import os
import copy
import cv2
""" 
    * Function Name: model()
    * Input: im,model_path="NoFilter.pth"
    * Output: classes[prediction]
    * Logic: this function helps to predict the the handsign 
    * Example Call: model(im,model_path="NoFilter.pth")
"""
def model(img,model_path="NoFilter.pth"):
	run_on_gpu =torch.cuda.is_available()
	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	classes = ['Aboard', 'All_Gone', 'Baby', 'Beside', 'Book', 'Bowl', 'Bridge', 'Camp', 'Cartridge', 'Eight', 'Five', 'Fond', 'Four', 'Friend', 'Glove', 'Hang', 'High', 'House', 'How_Many', 'IorMe', 'Man', 'Marry', 'Meat', 'Medal', 'Mid_Day', 'Middle', 'Money', 'Moon', 'Mother', 'Nine', 'One', 'Opposite', 'Prisoner', 'Ring', 'Rose', 'See', 'Seven', 'Short', 'Six', 'Superior', 'Ten', 'Thick', 'Thin', 'Three', 'Tobacco', 'Two', 'Up', 'Watch', 'Write', 'You']
	data_transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
	img=Image.fromarray(img)
	model=models.resnet50()
	n_inputs = model.fc.in_features
	model.fc = nn.Linear(n_inputs, len(classes))
	if run_on_gpu:
		model.cuda()
	checkpoint = torch.load(model_path,map_location=device)
	model.load_state_dict(checkpoint)
	model.eval()
	img_loader = data_transform(img).unsqueeze(0).to(device)
	img_loader= Variable(img_loader)
	prediction = model(img_loader).cpu()
	prediction = prediction.data.numpy().argmax()
	return	classes[prediction]
#The code below checks if the  command-line argument given is in  correct format or not    	
parser = argparse.ArgumentParser( usage="""python myscript.py {image}""",description='''Description.''',epilog="""Epilog.""")
parser.add_argument("image", help="input path")
parser.add_argument('--mod',help="animal model path")
args = parser.parse_args()
if(args.image==None):
	print("ERROR:no input path specified")
	exit()
input_location=args.image
m_path=False
if(args.mod!=None):
	mod_path=args.amod
	m_path=True

input_image = cv2.imread(input_location,cv2.COLOR_BGR2RGB)
if m_path:
	output=model(input_image,model_path=mod_path)
else:
	output=model(input_image)
print("the hand sign represents")
print(output)