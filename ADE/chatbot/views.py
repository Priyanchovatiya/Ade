import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Rule-based chatbot logic
def get_bot_response(user_message):
    user_message = user_message.lower()

    responses = {
        "hello": "Hi there! How can I assist you?",
        "hi": "Hello! How can I help?",
        "services": "We provide dental lab services, including implants, cosmetic dentistry, and digital dentistry.",
        "pricing": "Our pricing varies based on services. Please visit our Pricing page or contact us for details.",
        "contact": "You can contact us at info@advancedentalexport.com or call +91 84888 88877.",
        "thanks": "You're welcome! Let me know if you need anything else.",
        "bye": "Goodbye! Have a great day!"
    }

    # Check if the user's message matches a predefined response
    for keyword, response in responses.items():
        if keyword in user_message:
            return response

    return "I'm sorry, I didn't understand that. Please try again with a different question."

@csrf_exempt  # Disable CSRF protection for API calls
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            bot_reply = get_bot_response(user_message)

            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"reply": "Error processing your request."}, status=500)

    return JsonResponse({"reply": "Invalid request"}, status=400)
