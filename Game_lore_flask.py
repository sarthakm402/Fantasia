import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from flask import Flask, render_template, request
import time
from datetime import datetime

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = GPT2LMHeadModel.from_pretrained("gpt2-fantasy-raw")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-fantasy-raw")
model = model.to(device)

def generate_text(prompt, model, tokenizer, device):
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
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

start_time = time.time()
model.eval()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index_game.html")

@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            output = generate_text(prompt, model, tokenizer, device)
            return render_template("index_game.html", prompt=prompt, output=output)
    return render_template("index_game.html")

@app.route("/status", methods=["GET"])
def status():
    uptime = time.time() - start_time
    status_info = {
        "model": "gpt2-fantasy-raw",
        "uptime": f"{uptime:.2f} seconds",
        "device": device.type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template("index_game_status.html", status=status_info)

if __name__ == "__main__":
    app.run(debug=True)
