from dotenv import load_dotenv
from crewai import LLM

def main():
    load_dotenv()
    print("Hello from crewaiproject!")
    llm = LLM(model="google/gemini-2.5-flash-lite", temperature=0.1)
    response = llm.call("Who invented bulb")
    print(response)

if __name__ == "__main__":
    main()
