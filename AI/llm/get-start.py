"""
https://python.langchain.com/en/latest/getting_started/getting_started.html

pip install langchain
pip install openai


# طريقة عمل بيئة البايثون الخاصة بالمشروع
# How to make a virtual python env for your project.

> python -m venv venv

>
On Windows: venv\Scripts\activate.bat
On Unix or Linux: source venv/bin/activate

> pip install mylibrary

# ممكن إخراج هذه المكتبات فى ملف
# export lib name as requirements file
> pip freeze > requirements.txt

# Stop virtual env
deactivate
"""
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


llm = OpenAI(temperature=0.9)
prompt = "What the main language for GPT?"
print(llm(prompt))
# The main language used by GPT (Generative Pre-trained Transformer) is Python.
