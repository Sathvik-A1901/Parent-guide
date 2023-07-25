from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


llm = ChatOpenAI(openai_api_key="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",
        model_name="gpt-3.5-turbo",
        temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "The following is a friendly conversation between a human and an AI. The AI is talkative and "
            "provides lots of specific details from its context. If the AI does not know the answer to a "
            "question, it truthfully says it does not know."
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template('{input}')
    ])

    
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)
print("processing is done \n")

def convo(usertext):
    return conversation.predict(input=usertext)
