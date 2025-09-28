Agent-as-Coder challenge.
The goal was to build an autonomous coding agent that can write its own parser for bank-statement PDFs.

My Approach
Clone and Setup
did git clone git clone https://github.com/sathvika0031/ai-agent-challenge.git cd ai-agent-challenge

Create and activate virtual environment
python -m venv venv venv\Scripts\activate

.env used for API key
used .env for API keys Groq API key using (GROQ_API_KEY=yourAPIkey)

Install dependencies
pip install -r requirements.txt

Run the Agent
for icici python agent.py --target icici python -m pytest -q tests/test_icici_parser.py

for sbi python agent.py --target sbi python -m pytest -q tests/test_sbi_parser.py

Code run test
tested for icici bank statement pdf

Agent Design
https://drive.google.com/file/d/19giKeQVMkqWE5Ot8gcLEwwLPDW4gtaDw/view?usp=sharing  




