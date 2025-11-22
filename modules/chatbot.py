from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def get_chat_response(db, user_prompt):
    retriever = db.as_retriever(search_kwargs={"k": 3})

    model_name = "google/flan-t5-small"  # smaller, lighter
    pipe = pipeline(
        "text2text-generation",
        model=model_name,
        tokenizer=model_name,
        max_length=256
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa.run(user_prompt)
    return response
