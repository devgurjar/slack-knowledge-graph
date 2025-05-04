# Slack Knowledge Graph Explorer

A Streamlit application that allows users to search through a knowledge graph of Slack conversations. The application provides an easy-to-use interface for searching through company information, components, questions, and answers.

## Features

- Full-text search across all fields
- Real-time search results
- Expandable result cards
- Clean and intuitive interface

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run searchInterface.py
```

## Data Structure

The application expects a `knowledge_graph.json` file in the same directory with the following structure:

```json
[
  {
    "channel_id": "...",
    "thread_id": "...",
    "source": "slack",
    "messages": "..."
  }
]
```

## Deployment

This application is deployed using [Streamlit Cloud](https://streamlit.io/cloud). 