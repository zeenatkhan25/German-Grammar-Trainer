import torch
import torch.nn as nn
from model import GrammarModel
from utils import load_exercises

def train():
    exercises = load_exercises()
    print(f"Loaded {len(exercises)} exercises")
    
    # Model setup
    model = GrammarModel(vocab_size=1000)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    
    print("Model ready for training!")
    print("Training will be implemented with Hugging Face datasets.")

if __name__ == "__main__":
    train()
