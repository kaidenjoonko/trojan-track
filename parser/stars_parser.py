import os
import json
import pdfplumber
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("PARSER_OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def load_requirements(json_path):
    with open(json_path, "r") as f:
        return json.load(f)

def parse_stars_report(text, requirements):
    system_message = (
        "You are an assistant that analyzes a student's course completion based on degree requirements.\n"
        "You will be given the degree requirements JSON structure and a student's USC STARS report text.\n"
        "For each course listed in the requirements, mark it as completed or not based on the STARS report.\n"
        "Return a JSON object matching the degree requirements structure, with each course containing a new boolean field 'completed' (true/false).\n"
        "Do not add any extra text or commentary — only return valid JSON."
    )
    user_message = (
        f"Degree requirements JSON:\n{json.dumps(requirements)}\n\n"
        f"STARS report text:\n{text}\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"]

def main():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pdf_path = os.path.join(project_dir, "parser", "sample_stars.pdf")
    requirements_path = os.path.join(project_dir, "requirements", "csba.json")
    output_path = os.path.join(project_dir, "data", "parsed_output.json")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    if not os.path.exists(requirements_path):
        raise FileNotFoundError(f"Requirements JSON not found: {requirements_path}")

    stars_text = extract_text_from_pdf(pdf_path)
    requirements_json = load_requirements(requirements_path)

    parsed_json_str = parse_stars_report(stars_text, requirements_json)
    parsed_json = json.loads(parsed_json_str)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(parsed_json, f, indent=2)

if __name__ == "__main__":
    main()
