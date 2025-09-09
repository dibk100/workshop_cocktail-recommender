from langgraph import Pipeline, Node
from llm_task_classifier import classify_task
from llm_response_generator import generate_response
from graph_rag import GraphRAG

def response_node_fn(output: str):
    print("최종 결과:\n", output)

def build_pipeline():
    user_input_node = Node("UserInput")
    llm1_node = Node("LLM1_TaskClassifier", func=classify_task)
    graph_node = Node("GraphQuery", func=query_cocktails)
    llm2_node = Node("LLM2_Response", func=generate_response)
    response_node = Node("Response", func=response_node_fn)

    pipeline = Pipeline()
    pipeline.add_nodes([user_input_node, llm1_node, graph_node, llm2_node, response_node])
    pipeline.add_edges([
        ("UserInput", "LLM1_TaskClassifier"),
        ("LLM1_TaskClassifier", "GraphQuery"),
        ("GraphQuery", "LLM2_Response"),
        ("LLM2_Response", "Response")
    ])
    return pipeline

if __name__ == "__main__":
    pipeline = build_pipeline()
    user_query = {"text": "This is a drink called a mojito. Can you recommend something similar?"}
    pipeline.run(inputs={"UserInput": user_query})
