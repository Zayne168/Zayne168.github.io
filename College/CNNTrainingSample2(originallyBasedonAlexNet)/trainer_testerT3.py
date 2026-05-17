import torch
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def train(model, device, train_loader, optimizer, epoch):
	model.train()
	loss_fn = torch.nn.BCELoss()
	trainLoss = 0
	correct = 0
	
	for batch_ids, (x, y) in enumerate(train_loader):
		#Batch, Sequence Length, Channels -> Batch, Channels, Sequence Length
		x = x.permute(0, 2, 1).to(device)
		y = y.float().unsqueeze(1).to(device)
		optimizer.zero_grad()
		output = model(x)
		loss = loss_fn(output, y)
		loss.backward()
		optimizer.step()

		trainLoss += loss.item() * x.size(0)
		prediction = (output >= 0.5).float()
		correct += (prediction == y).sum().item()
		#if (batch_ids + 1) % 2 == 0:
		#	print(
		#		f"Train Epoch: {epoch} [{batch_ids * len(x)}/{len(train_loader.dataset)} "
		#		f"({100. * batch_ids / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}"
		#	)
	trainLoss /= len(train_loader.dataset)
	accuracy = 100. * correct / len(train_loader.dataset)

	return trainLoss, accuracy

def test(model, device, test_loader):
	model.eval()
	loss_fn = torch.nn.BCELoss()
	testLoss = 0
	correct = 0
	all_preds = []
	all_labels = []
	
	with torch.no_grad():
		for x, y in test_loader:
			x = x.permute(0, 2, 1).to(device)
			y = y.float().unsqueeze(1).to(device)
			output = model(x)
			
			loss = loss_fn(output, y)
			testLoss += loss.item() * x.size(0)
			
			pred = (output >= 0.5).float()
			correct += (pred == y).sum().item()
			
			all_preds.extend(pred.cpu().numpy().flatten())
			all_labels.extend(y.cpu().numpy().flatten())
	
	testLoss /= len(test_loader.dataset)
	accuracy = 100. * correct / len(test_loader.dataset)
	
	all_preds = [int(p) for p in all_preds]
	all_labels = [int(l) for l in all_labels]
	
	cm = confusion_matrix(all_labels, all_preds)
	disp = ConfusionMatrixDisplay(confusion_matrix=cm)
	disp.plot()
	fig = plt.gcf()
	
	tn, fp, fn, tp = cm.ravel()
	precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
	recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
	
	print(
		f"\nTest set: Average loss: {testLoss:.6f}, Accuracy: {correct}/{len(test_loader.dataset)} "
		f"({accuracy:.2f}%), Precision: {precision:.4f}, Recall: {recall:.4f}\n{'='*30}"
	)
	
	return testLoss, accuracy, fig, precision, recall

def trainALEXNET(model,device,train_loader,optimizer,epochs):
    print("inside train")
    model.train()
    for batch_ids, (img, classes) in enumerate(train_loader):
        classes=classes.type(torch.LongTensor)
        img,classes=img.to(device),classes.to(device)
        torch.autograd.set_detect_anomaly(True)     
        optimizer.zero_grad()
        output=model(img)
        loss = loss_fn(output,classes)                
        
        loss.backward()
        optimizer.step()
    if(batch_ids +1) % 2 == 0:
        print("Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(
            epochs, batch_ids* len(img), len(train_loader.dataset),
            100.*batch_ids / len(train_loader),loss.item()))
		

def testALEXNET(model, device, test_loader):
    model.eval()
    test_loss=0
    correct=0
    with torch.no_grad():
        for img,classes in test_loader:
            img,classes=img.to(device), classes.to(device)
            y_hat=model(img)
            test_loss+=F.nll_loss(y_hat,classes,reduction='sum').item()
            _,y_pred=torch.max(y_hat,1)
            correct+=(y_pred==classes).sum().item()
        test_loss/=len(test_dataset)
        print("\n Test set: Avarage loss: {:.0f},Accuracy:{}/{} ({:.0f}%)\n".format(
            test_loss,correct,len(test_dataset),100.*correct/len(test_dataset)))
        print('='*30)
