import torch
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
import torch.optim as optim
import torch.nn as nn
from model import Net
from dataset import MyDataset
from trainer_tester import train, test


def run_grid_search():
	device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
	print('device:', device)

	learning_rates = [1e-4, 1e-3]
	batch_sizes = [32, 64]
	dropouts = [0.1, 0.25]
	epochs = 1
	seed = 800756759
	num_workers = 3

	with open('dataOUT/positive.txt') as f:
		pos = [line.strip() for line in f]
	with open('dataOUT/negative.txt') as f:
		neg = [line.strip() for line in f]

	sequences = pos + neg
	labels = [1] * len(pos) + [0] * len(neg)

	entire_dataset = MyDataset(sequences, labels)
	train_len = int(0.7 * len(entire_dataset))
	val_len = int(0.15 * len(entire_dataset))
	test_len = len(entire_dataset) - train_len - val_len
	train_dataset, val_dataset, test_dataset = random_split(
		entire_dataset,
		[train_len, val_len, test_len],
		generator=torch.Generator().manual_seed(seed),
	)

	best_accuracy = -1.0
	best_config = None

	for lr in learning_rates:
		for batch_size in batch_sizes:
			for dropout in dropouts:
				log_dir = f'../runs/lr_{lr}_bs_{batch_size}_dp_{dropout}'
				writer = SummaryWriter(log_dir=log_dir)

				train_loader = DataLoader(
					train_dataset,
					batch_size=batch_size,
					shuffle=True,
					num_workers=num_workers,
				)
				val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True)
				test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

				model = Net(dropout_p=dropout).to(device)

				optimizer = optim.Adam(model.parameters(), lr=lr)
				loss_fn = nn.BCELoss()

				for epoch in range(1, epochs + 1):
					train_loss, train_acc = train(model, device, train_loader, optimizer, epoch)
					val_loss, val_acc = test(model, device, val_loader)

				test_loss, test_acc = test(model, device, test_loader)
				writer.add_hparams(
					{'lr': lr, 'batch_size': batch_size, 'dropout': dropout},
					{'Test/Loss': test_loss, 'Test/Accuracy': test_acc},
				)
				writer.close()
				if test_acc > best_accuracy:
					best_accuracy = test_acc
					best_config = (lr, batch_size, dropout)

				print(
					f"config lr={lr}, bs={batch_size}, dropout={dropout} -> "
					f"test_acc={test_acc:.2f}%"
				)


	print(f"best_config={best_config}, best_accuracy={best_accuracy:.2f}%")


if __name__ == '__main__':
	run_grid_search()
