# 🤖 Multi-Tool AI Agent for Personal Productivity

Tool-Augmented LLM System using n8n + Streamlit

📌 Overview

This project implements a tool-augmented AI agent capable of performing real-world productivity tasks by dynamically selecting and invoking external APIs.

The system integrates a large language model with structured tools including Google Calendar, Gmail, Google Docs, Google Tasks, Google Sheets, web search, and a calculator.

Unlike a basic chatbot, this assistant operates as an orchestrated agent system, combining reasoning, memory, and API execution through a workflow automation layer (n8n).

🧠 Core Design Principle

The assistant follows the LLM + Tools paradigm:

1. User query is sent to an AI Agent.

2. The agent interprets intent.

3. The agent selects the appropriate tool.

4. The selected API is executed.

5. Results are returned to the user.

🏗 Architecture



<img width="2991" height="1900" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/8ca041f2-d629-47f6-8bae-56bc332e6c31" />




🔄 Execution Flow

1. User enters prompt in Streamlit.

2. Message is sent via webhook to n8n.

3. AI Agent:

  - Performs reasoning

 - Maintains conversation memory

 - Selects tool

4. Tool executes external API call.

5. Result is returned to Streamlit.

⚙️ Implemented Capabilities

💬 General Intelligence

- Question answering

- Web search

- Numerical reasoning via calculator

📅 Google Calendar

- Create events

- Retrieve events

- List upcoming events

📧 Gmail

- Retrieve emails

- Get specific messages

- Send email replies

- Summarize messages

✅ Google Tasks

- Create tasks

- Retrieve tasks

- List tasks

- Delete tasks

📝 Google Docs

- Create documents

- Update documents

- Retrieve documents

💰 Expense Tracking (Google Sheets)

- Append expense entries

- Retrieve expense history

🛠 Technical Stack

| Component     | Technology                                        |
| ------------- | ------------------------------------------------- |
| Frontend      | Streamlit                                         |
| Orchestration | n8n                                               |
| AI Model      | OpenAI Chat Model                                 |
| Agent Memory  | n8n Simple Memory                                 |
| APIs          | Gmail, Google Calendar, Google Docs, Google Tasks |
| Data Storage  | Google Sheets                                     |
| Communication | Webhook (HTTP)                                    |
| Language      | Python                                            |

-----------------------------------------------------------------------------------------------------------------
🚀 Running Locally

1.Prerequisites

- Make sure you have:

- Python 3.9+

- n8n installed and running locally

- Google API credentials configured in n8n

- OpenAI API key configured inside n8n

- Git installed (optional, for cloning)

2.Clone the Repository

git clone https://github.com/YOUR_USERNAME/n8n-personal-assistant.git
cd n8n-personal-assistant

3.Create a Virtual Environment

python -m venv .venv

4.Activate the Virtual Environment

for windows: 
.\.venv\Scripts\activate

for macOS / Linux:
source .venv/bin/activate

5.Install Dependencies:
pip install -r requirements.txt

6.Configure Webhook URL:
Inside app.py, ensure the webhook URL matches your n8n workflow:

"http://localhost:5678/webhook/YOUR_WEBHOOK_ID"

Make sure:

- n8n is running

- The workflow is activated

- The webhook is set to POST

7.Start the Streamlit App:
python -m streamlit run app.py

8.Start n8n (If Not Already Running)

If installed globally: n8n start

Or if running via Docker: docker start <your-container-name>

9.Test the System

- Open the Streamlit UI

- Send a test prompt (e.g., “Create a task to buy groceries”)

- Verify that: 

  - The AI Agent selects the correct tool

  - The action executes in Google Tasks

  - A response is returned in Streamlit
