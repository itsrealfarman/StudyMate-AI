from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def get_llm():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    return llm