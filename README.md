# Smalltalk Code Generator Chat Agent

This is a Python-based Smalltalk code generator, powered by OpenAI's GPT-4o-mini model. The program takes natural language input from the user and returns Smalltalk code.

## Features

- Interactive chat interface
- Translates natural language descriptions into Smalltalk code
- Leverages OpenAI's GPT-4o-mini model for code generation

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or later
- An OpenAI account with API access

## Installation

### 1. Clone the Repository

\```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
\```

### 2. Create a Virtual Environment (optional but recommended)

\```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
\```

### 3. Install Dependencies

\```bash
pip install -r requirements.txt
\```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

\```plaintext
OPENAI_API_KEY=your-api-key
\```

### 5. Run the Program

Start the Smalltalk Code Generator Chat Agent:

\```bash
python smalltalk_code_generator.py
\```

### 6. Usage

Interact with the chat interface to generate Smalltalk code. Type `exit` or `quit` to terminate the program.

## Error Handling

In case of an API error or an unexpected exception, the program will output an appropriate message to assist with troubleshooting.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
