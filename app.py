# streamlit run app.py --server.port 8089
import time
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬 ")
    st.write("⚠️ Attention: Use of confidential PDFs is prohibited!⚠️")

    # upload file
    pdf = st.file_uploader("Upload PDF", type="pdf")

    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=2000, chunk_overlap=400, length_function=len
        )
        chunks = text_splitter.split_text(text)

        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # show user input
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            with st.spinner("Waiting for response..."):
                start_time = time.time()
                docs = knowledge_base.similarity_search(user_question)

                llm = ChatOpenAI(model_name="gpt-4", temperature=0.6)
                chain = load_qa_chain(llm, chain_type="refine")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)
                    print(cb)

                response_time = time.time() - start_time
                time_output = "<div style='color:green;'>Response Time: {:.1f} Seconds</div>".format(
                    response_time
                )

                st.write(response)
                st.markdown(time_output, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
