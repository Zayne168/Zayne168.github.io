import torch
from torch.utils.data import DataLoader, random_split
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from trainer_tester import train,test
from model import Net
from dataset import MyDataset


#torch.cuda.is_available()
#torch.cuda.get_device_name(0)
#torch.cuda.mem_get_info()
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)


if __name__ == "__main__":
	CLASSES=2
	BATCH_SIZE=64
	EPOCHS=9
	LEARNING_RATE=0.0001
	SEED=800756759
	NUM_WORKERS=3

	trainLosses, valLosses = [], []
	trainAccs, valAccs = [], []


	with open("dataOUT/positive.txt") as f:
		pos = [line.strip() for line in f]

	with open("dataOUT/negative.txt") as f:
		neg = [line.strip() for line in f]
	sequences = pos + neg
	labels = [1]*len(pos) + [0]*len(neg)

		#dataset defined
	entireDataset = MyDataset(sequences, labels)

	trainLen = int(0.7*(len(entireDataset)))
	valLen = int(0.15*(len(entireDataset)))
	testLen = int(len(entireDataset) - trainLen - valLen)
	trainDataset, valDataset, testDataset = random_split(entireDataset, [trainLen, valLen, testLen], generator=torch.Generator().manual_seed(SEED))

	train_loader=torch.utils.data.DataLoader(trainDataset,batch_size=BATCH_SIZE, num_workers = NUM_WORKERS, shuffle=True)
	val_loader=torch.utils.data.DataLoader(valDataset,batch_size=BATCH_SIZE,shuffle=True)
	test_loader=torch.utils.data.DataLoader(testDataset,batch_size=BATCH_SIZE,shuffle=True)

	model=Net().to(device)
	optimizer=optim.Adam(params=model.parameters(),lr=LEARNING_RATE)
	loss_fn = nn.BCELoss()
	#We use BCE since 2 classes. CE wont work :(

	for epoch in range(1,EPOCHS+1):
		trainLoss, trainAcc = train(model, device, train_loader, optimizer, epoch)
		print(f"Epoch {epoch} Validation:")
		valLoss, valAcc = test(model, device, val_loader)

		trainLosses.append(trainLoss)
		valLosses.append(valLoss)
		trainAccs.append(trainAcc)
		valAccs.append(valAcc)


	print("Testing:")
	test(model,device,test_loader)

	#Loss plot
	plt.figure()
	plt.plot(trainLosses, label="Train Loss")
	plt.plot(valLosses, label="Validation Loss")
	plt.legend()
	plt.title("Loss vs Epoch")
	plt.xlabel("Epoch")
	plt.ylabel("Loss")
	plt.show()
	plt.savefig("2loss.png")

	#Accuracy plot
	plt.figure()
	plt.plot(trainAccs, label="Train Accuracy")
	plt.plot(valAccs, label="Validation Accuracy")
	plt.legend()
	plt.title("Accuracy vs Epoch")
	plt.xlabel("Epoch")
	plt.ylabel("Accuracy")
	plt.show()
	plt.savefig("2accuracy.png")




	allPreds = []
	allLabels = []

	model.eval()
	with torch.no_grad():
		for x, y in test_loader:
			x = x.permute(0, 2, 1).to(device)
			y = y.to(device)

			output = model(x)
			predictions = (output >= 0.5).float()

			allPreds.extend(predictions.cpu().numpy().flatten())
			allLabels.extend(y.cpu().numpy().flatten())

	cm = confusion_matrix(allLabels, allPreds)
	disp = ConfusionMatrixDisplay(confusion_matrix=cm)
	disp.plot()

	plt.title("Confusion Matrix")
	plt.show()
	plt.savefig("2confusionMatrix.png")