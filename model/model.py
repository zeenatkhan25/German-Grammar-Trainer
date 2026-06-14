import torch
import torch.nn as nn

class GrammarModel(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, hidden_dim=128, output_dim=2):
        super(GrammarModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        _, (hidden, _) = self.lstm(embedded)
        output = self.fc(hidden[-1])
        return output
