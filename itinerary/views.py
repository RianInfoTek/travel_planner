
# import os
# import google.generativeai as palm
# from django.http import JsonResponse
# from rest_framework.views import APIView
# import logging

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# class CrewAPIView(APIView):
#     def post(self, request):
#         city = request.data.get("city")
#         days = request.data.get("days", 3)  # Default to a 3-day itinerary
#         activity_type = request.data.get("activity_type", "general")  # Default to general itinerary
#         if not city:
#             return JsonResponse({"error": "City parameter is required"}, status=400)
        
#           # Normalize the city input
#         city = city.strip().title()

#         # Initialize Google Generative AI with your API key
#         palm.configure(api_key=os.getenv("GOOGLE_GENERATIVEAI_API_KEY"))

#         try:
#             # Log the input city
#             logger.debug(f"Request received to generate itinerary for city: {city}, Days: {days}, Activity Type: {activity_type}")
#             prompt = (
#                 f"Create a detailed {days}-day travel itinerary for {city} focusing on {activity_type} activities."
#             )

#             # Generate the response
#             response = palm.chat(
#                 model='models/chat-bison-001',
#                 messages=[prompt]
#             )

#              # Log the response for debugging
#             logger.debug(f"API response: {response}")

#             # Extract the content from the ChatResponse object
#             if hasattr(response, 'candidates') and isinstance(response.candidates, list):
#                 itinerary = response.candidates[0].get('content', 'No itinerary generated.')
#                 return JsonResponse({"itinerary": itinerary})
#             else:
#                 logger.error("Invalid response structure from the API.")
#                 return JsonResponse({"error": "Failed to generate itinerary"}, status=500)

#         except Exception as e:
#             logger.exception("An error occurred while generating the itinerary.")
#             return JsonResponse({"error": str(e)}, status=500)
# import os
# import google.generativeai as palm
# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework.views import APIView
# import logging

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# class CrewAPIView(APIView):
#     def get(self, request):
#         # Render the form page on GET request
#         return render(request, 'index.html')

#     def post(self, request):
#         city = request.POST.get("city")
#         days = request.POST.get("days", 3)  # Default to a 3-day itinerary
#         activity_type = request.POST.get("activity_type", "general")  # Default to general itinerary

#         if not city:
#             return render(request, 'index.html', {"error": "City parameter is required"})

#         # Normalize the city input
#         city = city.strip().title()

#         # Initialize Google Generative AI with your API key
#         palm.configure(api_key=os.getenv("GOOGLE_GENERATIVEAI_API_KEY"))

#         try:
#             # Log the input city
#             logger.debug(f"Request received to generate itinerary for city: {city}, Days: {days}, Activity Type: {activity_type}")
#             prompt = (
#                 f"Create a detailed {days}-day travel itinerary for {city} focusing on {activity_type} activities."
#             )

#             # Generate the response
#             response = palm.chat(
#                 model='models/chat-bison-001',
#                 messages=[prompt]
#             )

#             # Log the response for debugging
#             logger.debug(f"API response: {response}")

#             # Extract the content from the ChatResponse object
#             if hasattr(response, 'candidates') and isinstance(response.candidates, list):
#                 itinerary = response.candidates[0].get('content', 'No itinerary generated.')
#                 return render(request, 'index.html', {
#                     "itinerary": itinerary,
#                     "city": city
#                 })
#             else:
#                 logger.error("Invalid response structure from the API.")
#                 return render(request, 'index.html', {"error": "Failed to generate itinerary"})

#         except Exception as e:
#             logger.exception("An error occurred while generating the itinerary.")
#             return render(request, 'index.html', {"error": str(e)})

# import os
# import re
# import google.generativeai as palm
# from django.shortcuts import render
# from rest_framework.views import APIView
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# class CrewAPIView(APIView):
#     def get(self, request):
#         return render(request, 'index.html')

#     def post(self, request):
#         city = request.POST.get("city")
#         days = request.POST.get("days", 3)
#         activity_type = request.POST.get("activity_type", "general")

#         if not city:
#             return render(request, 'index.html', {"error": "City parameter is required"})

#         city = city.strip().title()

#         palm.configure(api_key=os.getenv("GOOGLE_GENERATIVEAI_API_KEY"))

#         try:
#             logger.debug(f"Request received to generate itinerary for city: {city}, Days: {days}, Activity Type: {activity_type}")
#             prompt = (
#                 f"Create a detailed {days}-day travel itinerary for {city} focusing on {activity_type} activities. "
#                 f"For each day, provide a schedule with times and descriptions for at least 4 activities. "
#                 f"Format each day as 'Day X:' followed by the activities, each on a new line with the time."
#             )

#             response = palm.chat(
#                 model='models/chat-bison-001',
#                 messages=[prompt]
#             )

#             logger.debug(f"API response: {response}")

#             if hasattr(response, 'candidates') and isinstance(response.candidates, list):
#                 itinerary_text = response.candidates[0].get('content', 'No itinerary generated.')
#                 structured_itinerary = self.parse_itinerary(itinerary_text)
#                 return render(request, 'index.html', {
#                     "itinerary": structured_itinerary,
#                     "city": city
#                 })
#             else:
#                 logger.error("Invalid response structure from the API.")
#                 return render(request, 'index.html', {"error": "Failed to generate itinerary"})

#         except Exception as e:
#             logger.exception("An error occurred while generating the itinerary.")
#             return render(request, 'index.html', {"error": str(e)})

#     def parse_itinerary(self, itinerary_text):
#         days = re.split(r'Day \d+:', itinerary_text)[1:]  # Split by "Day X:" and remove the empty first element
#         structured_itinerary = []

#         for day in days:
#             activities = []
#             for line in day.strip().split('\n'):
#                 match = re.match(r'(\d{1,2}:\d{2}\s*(?:AM|PM))\s*-\s*(.*)', line.strip())
#                 if match:
#                     time, description = match.groups()
#                     activities.append({'time': time.strip(), 'description': description.strip()})
#             structured_itinerary.append({'activities': activities})

#         return structured_itinerary

import os
import re
import google.generativeai as palm
from django.shortcuts import render
from rest_framework.views import APIView
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CrewAPIView(APIView):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        city = request.POST.get("city")
        days = request.POST.get("days", 3)
        activity_type = request.POST.get("activity_type", "general")

        if not city:
            return render(request, 'index.html', {"error": "City parameter is required"})

        city = city.strip().title()

        # Initialize Google Generative AI with your API key
        palm.configure(api_key=os.getenv("GOOGLE_GENERATIVEAI_API_KEY"))

        try:
            logger.debug(f"Request received to generate itinerary for city: {city}, Days: {days}, Activity Type: {activity_type}")
            prompt = (
                f"Create a detailed {days}-day travel itinerary for {city} focusing on {activity_type} activities. "
                f"For each day, provide a schedule with times and descriptions for at least 4 activities. "
                f"Format each day as 'Day X:' followed by the activities, each on a new line with the time."
            )

            # Generate the response
            response = palm.chat(
                model='models/chat-bison-001',
                messages=[prompt]
            )

            logger.debug(f"API response: {response}")

            if hasattr(response, 'candidates') and isinstance(response.candidates, list):
                itinerary_text = response.candidates[0].get('content', 'No itinerary generated.')
                structured_itinerary = self.parse_itinerary(itinerary_text)
                return render(request, 'index.html', {
                    "itinerary": structured_itinerary,
                    "city": city
                })
            else:
                logger.error("Invalid response structure from the API.")
                return render(request, 'index.html', {"error": "Failed to generate itinerary"})

        except Exception as e:
            logger.exception("An error occurred while generating the itinerary.")
            return render(request, 'index.html', {"error": str(e)})

    def parse_itinerary(self, itinerary_text):
        # Split the itinerary by days using a more general approach
        days = re.split(r'\bDay \d+\b', itinerary_text)[1:]  # Split by "Day X", ignoring the first empty split
        structured_itinerary = []

        for day in days:
            activities = []
            for line in day.strip().split('\n'):
                # Improved regex pattern to match lines with or without time prefixes
                match = re.match(r'(?:(\d{1,2}:\d{2}(?:\s*(?:AM|PM))?)\s*-\s*)?(.*)', line.strip())
                if match:
                    time, description = match.groups()
                    # Only use "Anytime" if no time information is found
                    time = time.strip() if time else ""
                    description = description.strip() if description else "No details provided"
                    activities.append({'time': time, 'description': description})
            structured_itinerary.append({'activities': activities})

        return structured_itinerary