# Wordsmith

I am building a rag-based llm application with langchain, bytewax, qdrant, and comet.

## Intro to Large Language Models

## Retrieval Augmented Generation(RAG)

## Emerging LLM stack

![image](https://github.com/aniket-mish/llms-playground/assets/71699313/8155b0f6-8e63-42ea-8a19-4be7526008cc)

## Dataset



## Training Pipeline

- Load a QnA dataset
- Fine-tune an open-source LLM using QLoRA
- Log experiments in an experiment tracker
- Monitor inference results on a dashboard
- Store the best model in the model registry
- Deploy this pipeline to train the LLM

## Streaming Pipeline

- Ingest data
- Transform the docs into embeddings
- Store the embeddings
- CICD pipeline to deploy this pipeline

## Inference Pipeline

- Downloads the model
- Takes queries
- Goes to vector db
- Calls the LLM using the query and context from the vector db
- Logs the prompt and answer
- Build a streamlit UI

## References

[1] [stats00/ml-engineering](https://github.com/stas00/ml-engineering?tab=readme-ov-file)

[2] [Made With ML](https://madewithml.com)

[3] [Building RAG-based LLM Applications for Production](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)

[4] [LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/)

[5] [AI Canon](https://a16z.com/ai-canon/)

[6] [Best Practices for LLM Evaluation of RAG Applications](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG)

[7] [What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)

[8] [Open AI Cookbook](https://cookbook.openai.com)

