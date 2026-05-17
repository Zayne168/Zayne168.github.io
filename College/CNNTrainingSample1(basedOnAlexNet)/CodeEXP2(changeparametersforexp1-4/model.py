import torch
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
#import matplotlib.pyplot as plt
import numpy as np



#based on(copied from) the AlexNet code provided in class :)
class Net(nn.Module):
    def math(w, f, s=1, p=0):
            return (w - f + (2*p))//s + 1
    def __init__(self):
        super().__init__()
        #4 in channels since 1 hot = 4 channels
        self.conv1 = nn.Conv1d(in_channels=4,out_channels=96,kernel_size=13)
        self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv1d(in_channels=96, out_channels=128, kernel_size=13, padding=6)
        self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv1d(in_channels=128, out_channels=256, kernel_size=13, padding=6)
        self.pool3 = nn.AdaptiveMaxPool1d(1)#adaptive since seq length is not explicitly known 
        self.fc1 = nn.Linear(in_features=256, out_features=250)
        self.dropout = nn.Dropout(p=0.12)
        self.fc2 = nn.Linear(250, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        #flatten for FCNN
        x = torch.flatten(x, 1)     
        x = self.fc1(x)
        x = self.dropout(x)
        x = torch.sigmoid(self.fc2(x))
        return x





