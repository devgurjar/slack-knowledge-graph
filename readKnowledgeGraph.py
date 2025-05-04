import pickle
import json
# Load the knowledge graph
with open('knowledge_graph.pkl', 'rb') as f:
    graph = pickle.load(f)

# Extract Question-Answer pairs
qa_pairs = []

for node, data in graph.nodes(data=True):
    if data.get('type') == 'question':
        question_text = data.get('text')

        # Find all connected answer nodes
        for neighbor in graph.neighbors(node):
            neighbor_data = graph.nodes[neighbor]
            if neighbor_data.get('type') == 'answer':
                answer_text = neighbor_data.get('text')
                qa_pairs.append({
                    "question": question_text,
                    "answer": answer_text
                })

# Save the QA pairs
with open('qa_pairs.json', 'w', encoding='utf-8') as f:
    json.dump(qa_pairs, f, indent=2, ensure_ascii=False)

print(f"✅ Extracted {len(qa_pairs)} question-answer pairs.")
