import os
from dotenv import load_dotenv

load_dotenv()


from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.tools.drive_search import search_drive


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_drive_query(user_input):
    prompt = f"""
Convert this user request into ONLY a valid Google Drive API q query condition.

Rules:
- Return ONLY query text
- No explanation
- No markdown

Examples:
Find pdf files:
mimeType='application/pdf'

Find report files:
name contains 'report'

Find files after April 1:
modifiedTime > '2026-04-01T00:00:00'

User request:
{user_input}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content.strip()


def handle_chat(user_input):
    try:
        query = generate_drive_query(user_input)

        print("Generated query:", query)

        results = search_drive(query)

        if not results:
            return "No matching files found."

        formatted_results = []

        for file in results:
            formatted_results.append(
                f"""
Name: {file['name']}
Type: {file['mimeType']}
Modified: {file['modifiedTime']}
Link: {file['webViewLink']}
"""
            )

        return "\n".join(formatted_results)

    except Exception as e:
        return f"Error: {str(e)}"
