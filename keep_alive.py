from gradio_client import Client
import os
import time

# --- Configuration using the exact snippet you provided ---
SPACE_ID = "Elijah-Indarjit/Chatbotv4"
API_NAME = "/chat_wrapper"

# --- Keep-Alive Logic ---
try:
    print(f"Connecting to Space: {SPACE_ID}")
    
    # The client handles the correct API URL discovery internally
    client = Client(SPACE_ID)
    
    # Send a simple query using the exact parameter names from your docs
    result = client.predict(
        user_message="Hello.",
        history=[],
        api_name=API_NAME,
        # Increase timeout for cold starts on the free tier
        _ignored_fn_index=0, 
        _request_timeout=120 
    )
    
    # Print the result to confirm activity
    print(f"✅ Success! Space responded.")
    print(f"Chatbot Output Snippet: {result[0][0][1][:100]}...")
    
except Exception as e:
    print(f"❌ Keep-Alive Failed. Error: {e}")
    # This will fail the GitHub Action, which is what we want on an error
    exit(1)
