import json
import torch
import random
import numpy as np
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW
from tqdm import tqdm

# Set seed for reproducibility
def set_seed(seed=42):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True

set_seed(42)

# Load tokenizer and set pad token
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Custom Dataset
class FantasyDataset(Dataset):
    def __init__(self, path, tokenizer, max_len=512):
        super().__init__()
        self.data = []
        self.tokenizer = tokenizer
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                example = json.loads(line)
                text = f"{example['input']}\n{example['output']}"
                encoded = tokenizer(
                    text,
                    max_length=max_len,
                    padding="max_length",
                    truncation=True,
                    return_tensors="pt"
                )
                self.data.append({
                    "input_ids": encoded["input_ids"].squeeze(0),
                    "attention_mask": encoded["attention_mask"].squeeze(0),
                    "labels": encoded["input_ids"].squeeze(0)
                })

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Load dataset and model
dataset = FantasyDataset("fantasy_quests.jsonl", tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))
model = model.to(device)

optimizer = AdamW(model.parameters(), lr=5e-5)

# Training loop
def train(model, dataloader, epochs):
    model.train()
    for epoch in range(epochs):
        loop = tqdm(dataloader, leave=True, desc=f"Epoch {epoch+1}")
        epoch_loss = 0
        for batch in loop:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            loop.set_postfix(loss=loss.item())
            epoch_loss += loss.item()

        print(f"Epoch {epoch+1} Loss: {epoch_loss / len(dataloader):.4f}")

# Train the model
train(model, dataloader, epochs=3)

# Save model and tokenizer
model.save_pretrained("gpt2-fantasy-raw")
tokenizer.save_pretrained("gpt2-fantasy-raw")

# Inference
model.eval()
prompt = "Goal: Defeat the lich king\nSetting: Castle of Shadows"
inputs = tokenizer(prompt, return_tensors="pt").to(device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=150,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
