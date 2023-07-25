from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from prompt_gen import PromptGenerator

llm = ChatOpenAI(openai_api_key="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",
        model_name="gpt-3.5-turbo",
        temperature=0.1)

p=PromptGenerator()
prompt=p.get_prompt()


memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)
print("processing is done \n")

def convo(usertext):
    return conversation.predict(input=usertext)
