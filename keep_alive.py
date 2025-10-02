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
    # NOTE: Removed the invalid '_ignored_fn_index' parameter.
    # NOTE: Set a longer timeout in case of a cold start.
    result = client.predict(
        user_message="Automated keep-alive ping.",
        history=[],
        api_name=API_NAME,
        _request_timeout=120  
    )
    
    # Print the result to confirm activity
    print(f"✅ Success! Space responded.")
    # Assuming the first output element is the chat history, and the last item is the bot's response
    # This line attempts to parse the nested output structure for a snippet.
    if isinstance(result, tuple) and len(result) > 0 and isinstance(result[0], list) and len(result[0]) > 0:
        last_response = result[0][-1][1] 
        print(f"Chatbot Output Snippet: {last_response[:100]}...")
    else:
        print("Chatbot returned an unexpected output format, but the call was successful.")
    
except Exception as e:
    print(f"❌ Keep-Alive Failed. Error: {e}")
    # This will fail the GitHub Action, which is what we want on an error
    exit(1)
