# AI Icebreaker Bot

An AI-powered tool that generates personalized icebreakers and conversation starters from LinkedIn profiles, built with LlamaIndex and IBM watsonx (Granite).

## Overview

Imagine you're heading to a big networking event, surrounded by potential employers and industry leaders. You want to make a great first impression, but you're struggling to come up with more than the usual, "What do you do?"

This project solves that problem with an AI-powered tool that does the research for you. You input a name, and within seconds, the bot — powered by LlamaIndex and IBM watsonx — searches a LinkedIn profile and generates personalized icebreakers based on someone's career highlights, interests, and even fun facts. Instead of generic questions, you start with something unique and meaningful.

The bot uses natural language processing to build a retrieval-augmented generation (RAG) pipeline: profile data is chunked and embedded, stored in a vector index, and queried with an IBM Granite LLM to surface tailored conversation starters. It's useful for networking events, job interviews, or any social setting where a more personal opening line helps.

## Features

- Extract LinkedIn profile data via the ProxyCurl API, or use the bundled mock profile
- Process and index profile data using LlamaIndex and IBM watsonx embeddings
- Generate interesting facts about a person's career or education
- Answer follow-up questions about the profile through a chat interface
- Command-line interface and a Gradio web UI

**Note on data sources:** A mock profile (`data/mock_profile.json`) is bundled with the repo so the full RAG pipeline — chunking, embedding, indexing, and querying — works end to end without needing a ProxyCurl API key. The ProxyCurl integration code is kept in place for anyone who wants to plug in a live LinkedIn data provider.

## Project Structure

```
icebreaker/
├── requirements.txt           # Dependencies
├── config.py                  # Configuration settings (reads secrets from env vars)
├── data/
│   └── mock_profile.json      # Bundled sample LinkedIn profile
├── modules/
│   ├── __init__.py
│   ├── data_extraction.py     # LinkedIn profile data extraction
│   ├── data_processing.py     # Data splitting and indexing
│   ├── llm_interface.py       # LLM setup and interaction
│   └── query_engine.py        # Query processing and response generation
├── app.py                     # Gradio interface
└── main.py                    # CLI entry point
```

## Getting Started

### Prerequisites

- Python 3.11+
- An IBM watsonx.ai project and API key (for live embeddings/LLM calls)
- A ProxyCurl API key (optional — only needed for live LinkedIn extraction; mock data works out of the box)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abankar1/Icebreaker.git
cd Icebreaker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your credentials as environment variables (never committed to git — `.env` and any real keys are excluded via `.gitignore`):
```bash
export WATSONX_APIKEY="your-watsonx-api-key"
export WATSONX_PROJECT_ID="your-watsonx-project-id"
export PROXYCURL_API_KEY="your-proxycurl-api-key"  # optional
```

### Usage

#### Command Line Interface

```bash
python main.py --mock  # Use the bundled mock profile
# OR
python main.py --url "https://www.linkedin.com/in/username/" --api-key "your-api-key"
```

#### Web Interface

```bash
python app.py
```

Then open your browser to the URL shown in the terminal (typically http://127.0.0.1:7860).

## Tech Stack

LlamaIndex, IBM watsonx.ai (Granite LLM + embeddings), LangChain, ChromaDB, Gradio

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- IBM watsonx.ai for the Granite LLM and embedding models
- LlamaIndex for the data indexing and retrieval framework
- ProxyCurl for LinkedIn profile data extraction
