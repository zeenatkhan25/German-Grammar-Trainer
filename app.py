import gradio as gr
import random
import json

# Load grammar exercises
with open("data/grammar_data.json", "r") as f:
    exercises = json.load(f)

def check_answer(question, user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return "✅ Richtig! Well done!"
    else:
        return f"❌ Falsch! The correct answer is: **{correct_answer}**"

def get_question():
    exercise = random.choice(exercises)
    return exercise["question"], exercise["answer"]

with gr.Blocks(title="🇩🇪 German Grammar Trainer") as app:
    gr.Markdown("# 🇩🇪 German Grammar Trainer")
    gr.Markdown("Practice German grammar — for immigrants learning German in Germany!")
    
    question_box = gr.Textbox(label="Question", interactive=False)
    answer_input = gr.Textbox(label="Your Answer", placeholder="Type your answer here...")
    correct_answer = gr.State()
    
    with gr.Row():
        new_btn = gr.Button("New Question 🎲")
        submit_btn = gr.Button("Check Answer ✅", variant="primary")
    
    result_box = gr.Markdown()

    def load_question():
        q, a = get_question()
        return q, a, ""

    new_btn.click(load_question, outputs=[question_box, correct_answer, result_box])
    submit_btn.click(check_answer, inputs=[question_box, answer_input, correct_answer], outputs=result_box)

app.launch()
