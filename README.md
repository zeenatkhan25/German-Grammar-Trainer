# 🇩🇪 German Grammar Trainer

An AI-powered app that helps immigrants and language learners master German grammar through interactive exercises — built with PyTorch and Hugging Face.

---

## 💡 Why I Built This

Moving to a new country means learning a new language — fast. As an immigrant living in Berlin, I know how challenging German grammar can be: der, die, das, cases, verb conjugations… it never ends.

This project is my solution: a personalized, AI-driven grammar trainer that gives instant feedback and adapts to your level.

---

## ✨ Features

- 🧠 **AI-generated exercises** — grammar questions generated dynamically using a fine-tuned language model
- ✅ **Instant feedback** — know immediately if your answer is correct and why
- 📈 **Progressive difficulty** — starts simple, gets harder as you improve
- 🗣️ **Covers key topics** — articles (der/die/das), cases (Nominativ, Akkusativ, Dativ), verb conjugation, sentence structure
- 🌐 **Web app** — runs directly in the browser via Hugging Face Spaces

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Model | PyTorch, Hugging Face Transformers |
| UI | Gradio |
| Hosting | Hugging Face Spaces |
| Data | Custom German grammar dataset |
| Language | Python 3.10+ |

---

## 📁 Project Structure

```
German-Grammar-Trainer/
├── app.py                  # Gradio UI for Hugging Face Spaces
├── model/
│   ├── train.py            # PyTorch training script
│   ├── model.py            # Model architecture
│   └── utils.py            # Helper functions
├── data/
│   └── grammar_data.json   # Training sentences and exercises
├── notebooks/
│   └── exploration.ipynb   # Experiments in Google Colab
├── requirements.txt        # Dependencies
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/zeenatkhan25/German-Grammar-Trainer.git
cd German-Grammar-Trainer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app locally
```bash
python app.py
```

---

## 🌍 Live Demo

> 🔗 Coming soon on Hugging Face Spaces

---

## 📊 Model Details

- **Architecture:** Transformer-based sequence classification (Hugging Face)
- **Training data:** Custom German grammar exercise dataset
- **Framework:** PyTorch
- **Task:** Grammar correction and exercise generation

---

## 👩‍💻 Author

**Zeenat Khan**  
MSc Data Analytics Student @ BSBI Berlin  
🔗 [LinkedIn](https://linkedin.com/in/zeenat-khan25) | 🐙 [GitHub](https://github.com/zeenatkhan25) | 📊 [Tableau](https://public.tableau.com/app/profile/zeenat.khan1885/vizzes)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
