from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_question_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "Given a conversation history and the most recent user query, rewrite the query as a standalone question "
        "that makes sense without relying on the previous context. Do not provide an answer—only reformulate the "
        "question if necessary; otherwise, return it unchanged."
    )),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# Prompt for answering based on context
context_qa_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        """
    You are an assistant designed to answer questions using the provided context. Use the retrieved information as the primary source for your response, but you may use reasonable inference to make the answer more natural and helpful.

    If the answer is directly supported by the context, provide it clearly. If the context only partially contains the answer, explain what can be inferred from the available information without inventing unsupported facts.

    If the answer cannot be found in the context, avoid responding with only "I don't know." Instead, say something like:

    * "The provided context does not contain enough information to answer this fully."
    * "Based on the available context..."
    * "I could not find a direct answer in the retrieved information."

    Keep your answer concise and no longer than three sentences.

    {context}

        """
    )),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# Central dictionary to register prompts
PROMPT_REGISTRY = {
    "contextualize_question": contextualize_question_prompt,
    "context_qa": context_qa_prompt,
}


## 1. Hello thier i want to study about RAG
## 2. what is the full form of it