from app.services.llm_service import handle_chat

response = handle_chat("find all pdf reports")

print(response)
