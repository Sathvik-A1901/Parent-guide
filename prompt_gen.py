from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)

class PromptGenerator:
    def __init__(self) -> None:
        #The actual System message or the declaratio of the role for the system
        self.template = "You are a helpful assistant that guides parents to take correct decisions on their children career"
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.template)

        #Examples
        self.example_human1 = HumanMessagePromptTemplate.from_template("Hi")
        self.example_ai1 = AIMessagePromptTemplate.from_template("Hi, How can I assist you with your childs career")
        self.example_human2=HumanMessagePromptTemplate.from_template("What should I feed my child?")
        self.example_ai2=AIMessagePromptTemplate.from_template("Firstly can I know your childs age?(if childs age is already known then) You should probably feed the child with:")
    
    def get_prompt(self):

        human_template = "{input}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [self.system_message_prompt, self.example_human1, self.example_ai1,self.example_human2,self.example_ai2, human_message_prompt,MessagesPlaceholder(variable_name="history")]
        )

        return chat_prompt


