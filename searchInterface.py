import streamlit as st
import json

st.title("Slack Knowledge Graph Explorer")

# Load the knowledge graph data
try:
    with open('knowledge_graph.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("Error: knowledge_graph.json file not found. Please make sure the file exists in the same directory.")
    st.stop()
except json.JSONDecodeError:
    st.error("Error: Invalid JSON format in knowledge_graph.json")
    st.stop()

st.write(f"Total entries in knowledge base: {len(data)}")

query = st.text_input("Search for any keyword (company, component, question, or answer)")

if query:
    query = query.lower()
    results = []
    
    for item in data:
        if 'messages' in item:
            try:
                # Handle string JSON content
                if isinstance(item['messages'], str):
                    json_str = item['messages'].strip('```json\n').strip('```')
                    message_data = json.loads(json_str)
                    # Convert all values to string and join them for searching
                    content = ' '.join(str(v) for v in message_data.values()).lower()
                    if query in content:
                        results.append(message_data)
                # Handle direct dictionary content
                elif isinstance(item['messages'], dict):
                    content = ' '.join(str(v) for v in item['messages'].values()).lower()
                    if query in content:
                        results.append(item['messages'])
            except (json.JSONDecodeError, AttributeError) as e:
                continue

    st.write(f"Found {len(results)} matching results")
    
    for item in results:
        with st.expander(f"{item.get('company', 'Unknown Company')} - {item.get('component', 'Unknown Component')}"):
            st.write(f"**Company:** {item.get('company', 'N/A')}")
            st.write(f"**Component:** {item.get('component', 'N/A')}")
            st.write(f"**Question:** {item.get('question', 'N/A')}")
            st.write(f"**Answer:** {item.get('answer', 'N/A')}")
