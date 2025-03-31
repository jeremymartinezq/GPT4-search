import openai
import sys

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

def gpt4_search(query):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=query,
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    query = sys.argv[1]
    result = gpt4_search(query)
    print(result)
