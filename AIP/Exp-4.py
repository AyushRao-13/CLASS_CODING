pip install -q transformers torch sentencepiece
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from difflib import SequenceMatcher
print("Initializing...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.to(device)
print("Model Loaded Successfully!\n")
text = """
Artificial Intelligence (AI) is transforming industries by enabling machines
to perform tasks that typically require human intelligence. These include
decision-making, language translation, image recognition, and predictive analytics.
AI systems rely on machine learning algorithms trained on large datasets.
"""

question = "What does AI rely on?"

# Prompt Styles
instruction_prompt = "Summarize the following text:\n" + text
conversation_prompt = "Hi, can you give me a short summary of this text?\n" + text

# Function to Generate Text
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
    outputs = model.generate(
        **inputs,
        max_length=60,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Generate Summaries
summary_instruction = generate_text(instruction_prompt)
summary_conversation = generate_text(conversation_prompt)

print("===== Instructional Prompt Summary =====\n")
print(summary_instruction)
print("\n===== Conversational Prompt Summary =====\n")
print(summary_conversation)
# Simple QA Using Same Model
qa_prompt = "Answer the question based on the text:\n\nText:\n" + text + "\n\nQuestion:\n" + question
qa_answer = generate_text(qa_prompt)
print("\n===== Question Answering =====\n")
print("Question:", question)
print("Answer:", qa_answer)
# Evaluation Metrics
len_instruction = len(summary_instruction.split())
len_conversation = len(summary_conversation.split())

similarity = SequenceMatcher(
    None,
    summary_instruction,
    summary_conversation
).ratio()

print("\n===== Pattern Testing Evaluation =====\n")
print("Instruction Summary Length:", len_instruction)
print("Conversation Summary Length:", len_conversation)
print("Similarity Score:", round(similarity, 3))
print("\nPattern Testing Completed Successfully!")

