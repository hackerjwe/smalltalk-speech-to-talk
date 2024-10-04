import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Instantiate the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Ensure your .env has OPENAI_API_KEY
)

def generate_smalltalk_code(user_input):
    try:
        # Adjust the model to GPT-4o-mini or other specified variant
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Upgraded model name (GPT-4o-mini)
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that translates natural language descriptions into Smalltalk code. "
                        "Provide only the Smalltalk code without any explanations."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.2,
            n=1
        )
        # Correct way to access the content
        code = response.choices[0].message.content.strip()
        return code
    except OpenAIError as e:
        return f"OpenAI API error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def main():
    print("Welcome to the Smalltalk Code Generator Chat Agent!")
    print("Type 'exit' or 'quit' to terminate the program.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        elif not user_input:
            print("Please enter a valid description.\n")
            continue
        
        print("\nGenerating Smalltalk code...\n")
        code = generate_smalltalk_code(user_input)
        print(f"Smalltalk Code:\n{code}\n")

if __name__ == "__main__":
    main()
