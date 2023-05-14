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

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


llm = OpenAI(temperature=0.9)

loader = UnstructuredFileLoader("/Users/khaledlela/Downloads/test.txt")
document = loader.load()

char_text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = char_text_splitter.split_documents(document)

model = load_summarize_chain(llm=llm, chain_type="refine")
model.run(docs)

print(len(docs))

for doc in docs:
    print(doc)
prompt = "What the main language for GPT?"
print(llm(prompt))
# The main language used by GPT (Generative Pre-trained Transformer) is Python.
