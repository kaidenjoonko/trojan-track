import json
import openai
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_parsed_data(file_path):
    """Load parsed data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def get_unmet_requirements(parsed_data):
    """Check class requirements and return unmet ones."""
    requirements = parsed_data.get("requirements", [])
    unmet_requirements = [req["name"] for req in requirements if not req["completed"]]
    return unmet_requirements

def create_schedule_with_openai(unmet_requirements, semesters):
    """Use OpenAI API to generate a shuffled and reasonable schedule."""
    random.shuffle(unmet_requirements)  # Shuffle unmet requirements for variety

    prompt = (
        f"The student has the following unmet class requirements: {', '.join(unmet_requirements)}.\n"
        f"They want to graduate in {semesters} semesters. Create a reasonable class schedule with 3-4 classes per semester."
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()

def main():
    """Main function to generate a schedule."""
    file_path = "data/parsed_output.json"
    parsed_data = load_parsed_data(file_path)
    unmet_requirements = get_unmet_requirements(parsed_data)

    semesters = int(input("Enter the number of semesters you want to graduate in: "))
    schedule = create_schedule_with_openai(unmet_requirements, semesters)

    print("Generated Schedule:")
    print(schedule)

if __name__ == "__main__":
    main()
