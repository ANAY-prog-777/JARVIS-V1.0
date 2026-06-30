from google import genai


apikey = 'AQ.Ab8RN6IgjFYUDvFXBMaNqdW8B4lJfqqXCM8kPUQlpbxU8O0Svw'
client = genai.Client(api_key=apikey)

def generate_response(query):
    try:
        
        response = client.models.generate_content(



            model="gemini-2.5-flash",

            contents=f"You are Jarvis, a helpful desktop assistant. Keep your response conversational and under two sentences. Question: {query}"
        )
        return response.text
    except Exception as e:
        return f"I encountered an error managing my brain systems, im errorful, sir. Details: {e}"