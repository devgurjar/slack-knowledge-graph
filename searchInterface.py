import streamlit as st
import json

st.title("Slack Knowledge Graph Explorer")

with open('knowledge_graph.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

st.write(f"Total entries in knowledge base: {len(data)}")

query = st.text_input("Search for any keyword (company, component, question, or answer)")

if query:
    query = query.lower()
    results = []
    for item in data:
        # Get the messages field and check if it contains the search term
        if 'messages' in item:
            messages = item['messages'].lower()
            if query in messages:
                try:
                    # Extract the JSON string from the messages field
                    json_str = item['messages'].strip('```json\n').strip('```')
                    message_data = json.loads(json_str)
                    results.append(message_data)
                except:
                    continue
    
    st.write(f"Found {len(results)} matching results")
    
    for item in results:
        with st.expander(f"{item.get('company', 'Unknown Company')} - {item.get('component', 'Unknown Component')}"):
            st.write(f"**Company:** {item.get('company', 'N/A')}")
            st.write(f"**Component:** {item.get('component', 'N/A')}")
            st.write(f"**Question:** {item.get('question', 'N/A')}")
            st.write(f"**Answer:** {item.get('answer', 'N/A')}")
