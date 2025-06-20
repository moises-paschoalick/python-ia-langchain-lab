# python-ai-langchain-lab

**An experimental playground for learning and building with LangChain using Python and OpenAI's GPT-4o-mini model.**

---

## Project Description

This repository is a hands-on lab environment to explore the capabilities of the LangChain framework integrated with OpenAI's GPT models. The primary focus is to build practical applications using conversational AI, managing session-based chat histories, and creating interactive assistants.

The current example is a **Travel Assistant** chatbot that helps users plan trips by suggesting destinations, itineraries, and practical travel tips. The assistant maintains the conversation history for each user session to provide contextual responses.

---

## Features

- Uses LangChain's `ChatPromptTemplate` and `RunnableWithMessageHistory` to handle dynamic prompts with conversation history.
- Integrates OpenAI's GPT-4o-mini model for natural language understanding and generation.
- Session-based chat history management allowing multi-turn conversations.
- Simple command-line interface for interaction.
- Environment variable configuration with `.env` file for OpenAI API key management.

---

## Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API Key (set in `.env` file as `OPENAI_API_KEY`)
- `pip` for installing dependencies

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/moises-paschoalick/python-ai-langchain-lab.git
    cd python-ai-langchain-lab
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file (copy from `.env_example`) and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Running the Travel Assistant

Run the application with:

```bash
python app.py
