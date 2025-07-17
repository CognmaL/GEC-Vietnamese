"""
main.py - Vietnamese Grammatical Error Correction Web Demo

This script launches a Gradio web interface for correcting Vietnamese sentences using a pre-trained sequence-to-sequence model (e.g., BARTpho, ViT5).

Example usage (command line):
    python main.py

A web UI will open in your browser. Enter a Vietnamese sentence with errors and click 'Correct' to see the corrected output.

---

main.py - Demo sửa lỗi ngữ pháp tiếng Việt qua giao diện web Gradio.

Chạy lệnh:
    python main.py

Giao diện web sẽ mở trên trình duyệt. Nhập câu tiếng Việt có lỗi, nhấn 'Correct' để nhận kết quả đã sửa.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os
import gradio as gr

# Đường dẫn tương đối tới mô hình
model_dir = os.path.join(os.path.dirname(__file__), "models")

# Load tokenizer và model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Hàm sửa câu
def correct_text(text, max_length=512):
    """
    Correct a Vietnamese sentence using the pre-trained model.

    Args:
        text (str): Input sentence with grammatical/spelling errors.
        max_length (int): Maximum sequence length for the model.

    Returns:
        str: Corrected sentence.

    Ví dụ / Example:
        >>> correct_text("Toi di hoc ve nha.")
        'Tôi đi học về nhà.'
    """
    encoded = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
    input_ids = encoded["input_ids"].to(device)
    attention_mask = encoded["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            num_beams=4,
            early_stopping=True
        )
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text

# Giao diện Gradio
interface = gr.Interface(
    fn=correct_text,
    inputs=gr.Textbox(lines=3, label="Câu cần sửa lỗi"),
    outputs=gr.Textbox(label="Câu đã sửa"),
    title="Chỉnh sửa lỗi chính tả / ngữ pháp",
    description="Nhập một câu tiếng Việt có lỗi và mô hình sẽ tự động sửa lại.",
    allow_flagging="never"
)

if __name__ == "__main__":
    interface.launch()
