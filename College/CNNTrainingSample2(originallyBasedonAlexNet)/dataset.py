import torch
from torch.utils.data import Dataset, DataLoader



class MyDataset(Dataset):
    def __init__(self, sequences, labels):
        self.labels = torch.tensor(labels, dtype=torch.long)
        self.features = [self.Encoder(sequence) for sequence in sequences]
        self.features = torch.stack(self.features)
    def __len__ (self):
        return len(self.features)
    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]
    def Encoder(self, sequence):
        mapping = {'a': [1,0,0,0], 'c': [0,1,0,0], 'g': [0,0,1,0], 't': [0,0,0,1]}
        oneHot = []

        #oneHot Mapping/Encoding
        for i in sequence.lower():
            if i in mapping:
                oneHot.append(mapping[i])
            else:
                oneHot.append([0,0,0,0]) 
        
        return torch.tensor(oneHot, dtype=torch.float32)
        