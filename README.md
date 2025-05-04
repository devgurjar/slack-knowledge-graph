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

2. Set up your environment variables:

   There are two ways to set up your secrets:

   a. Using a `.env` file (for local development):
   ```bash
   SLACK_API_TOKEN=your-slack-token
   OPENAI_API_KEY=your-openai-key
   AZURE_ENDPOINT=your-azure-endpoint
   AZURE_API_VERSION=your-api-version
   AZURE_DEPLOYMENT_NAME=your-deployment-name
   ```

   b. Using Streamlit secrets (for deployment):
   Create `.streamlit/secrets.toml`:
   ```toml
   SLACK_API_TOKEN = "your-slack-token"
   OPENAI_API_KEY = "your-openai-key"
   AZURE_ENDPOINT = "your-azure-endpoint"
   AZURE_API_VERSION = "your-api-version"
   AZURE_DEPLOYMENT_NAME = "your-deployment-name"
   ```

3. Run the application:
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

### Setting up Streamlit Cloud Deployment

1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. In Streamlit Cloud settings, add your secrets:
   - Go to your app's settings
   - Find the "Secrets" section
   - Add each secret key-value pair
   - The secrets should match the format in `.streamlit/secrets.toml`

Note: Never commit your actual API keys or tokens to the repository. The example files (.env.example and secrets.toml) contain only placeholder values. 