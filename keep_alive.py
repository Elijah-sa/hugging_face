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
    # NOTE: All internal/private parameters (_request_timeout, _ignored_fn_index) are removed.
    result = client.predict(
        user_message="Automated keep-alive ping.",
        history=[],
        api_name=API_NAME
    )
    
    # Print the result to confirm activity
    print(f"✅ Success! Space responded.")
    
    # Attempt to extract the bot's response from the complex nested tuple structure
    # The structure is: result = (history, new_message_box_value)
    # The history part is usually result[0]. We check the last message in history.
    if isinstance(result, tuple) and len(result) > 0 and isinstance(result[0], list):
        # Last message in history is at result[0][-1], and the bot's response is the second element [1]
        last_response = result[0][-1][1] 
        print(f"Chatbot Output Snippet: {last_response[:100]}...")
    else:
        print("Chatbot returned an unexpected output format, but the call was successful.")
    
except Exception as e:
    print(f"❌ Keep-Alive Failed. Error: {e}")
    # This will fail the GitHub Action
    exit(1)
