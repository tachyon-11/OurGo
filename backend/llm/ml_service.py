from flask import Flask, request, jsonify
import google.generativeai as genai
import json
import random
import time

genai.configure(api_key='')
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

def generateResponse(prompt, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            response = model.generate_content(prompt)
            if response.text:
                return response
            else:
                print(f"Attempt {attempt}: No response.text found. Retrying...")
        except Exception as e:
            print(f"Attempt {attempt}: Error generating content: {e}")

        delay = random.uniform(0.5, 2) ** attempt 
        time.sleep(delay)

    print(f"All retries failed for prompt")
    return None

@app.route('/generateTags', methods=['POST'])
def generate_tags():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400

        try:
            age = user_data.get('age')
            user_gender = user_data.get('userGender')
            traveller_type = user_data.get('travellerType')
            where = user_data.get('where')
            from_location = user_data.get('from')
            start_date = user_data.get('startDate')
            end_date = user_data.get('endDate')

            if age is None or user_gender is None or traveller_type is None or \
               where is None or from_location is None or start_date is None or \
               end_date is None:
                return jsonify({"error": "Missing required fields"}), 400

            if traveller_type=="Solo":
                traveller_type = "Solo " + user_gender + " traveller"
            

            prompt = f"Describe {where} activities in 50-80 words, no bullet points, for tag creation which would help in creating personalized itenary using LLM."

            descriptionOfLocation = generateResponse(prompt)

            prompt = f"""
            Analyze the provided travel destination description and traveler profile to select the top 10 most relevant tags from the given list. Prioritize tags that accurately capture the destination's atmosphere, potential activities, and align with the traveler's interests and preferences. Consider factors like solo travel, group dynamics, and the destination's overall vibe. Traveler Profile: {traveller_type} Age of Traveller: {age} Destination: {where} Description of destination : {descriptionOfLocation} Tag Lists:- tag_list = ["Adventure Junkie", "Cultural Enthusiast", "Foodie Fiesta", "Luxury Traveler", "Nature Explorer", "History Buff", "Shutterbug", "Festival Goer", "Digital Nomad", "Spiritual Seeker", "Relax and Recharge", "City Nightlife Explorer", "Music Lover", "Shopping Enthusiast", "Language Learner", "Sports Fan", "Urban Explorer", "Beach Bum", "Road Tripper", "Art Addict", "Party animal", "Motor rider", "Ski Enthusiast", "Luxury Cruiser", "Island Hopper", "Scenic Train Traveler", "Wildlife Safari Adventurer", "Camping Enthusiast", "Mountain Climber", "Wine Connoisseur", "Hiking Enthusiast", "Water Baby", "Hot Air Balloon Rider", "Fishing Enthusiast", "Yoga retreat", "Gaming and Entertainment", "Bibliophile", "Romantic Retreat", "Honeymoon", "Do-together activities", "Meet new people", "Amusement parks", "Fun for kids"] Provide the output as a Python list with elements from tag_list and please use only from the given tags. Also ensure that Do-together activities is for only friends, couples and families
            I want the output to be in the following format which is a python array with 10 tags:-  
            ["tag1", "tag2", "tag3", "tag4"....."tag9", "tag10"]
            """

            response = generateResponse(prompt)
            
            if response:
                data_string = response.text
                tag_list = json.loads(data_string)
                return jsonify({
                    "status": "success",
                    "data": tag_list
                }), 200
            else:
                return jsonify({
                    "status": "success",
                    "data": []
                }), 200
                
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/getRestaurants', methods=['POST'])
def get_restaurants():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400

        try:
            age = user_data.get('age')
            origin = user_data.get("from")
            user_gender = user_data.get('userGender')
            traveller_type = user_data.get('travellerType')
            where = user_data.get('where')
            from_location = user_data.get('from')
            start_date = user_data.get('startDate')
            end_date = user_data.get('endDate')
            travel_tags = user_data.get('travelVibeTags')
            dining_preff = user_data.get('diningPreff')

            if age is None or user_gender is None or traveller_type is None or \
               where is None or from_location is None or start_date is None or \
               end_date is None or travel_tags is None or dining_preff is None:
                return jsonify({"error": "Missing required fields"}), 400

            if traveller_type=="Solo":
                traveller_type = "Solo " + user_gender + " traveller"

            travelVibePrompt = f"""Given the following list of travel vibe tags: {travel_tags}
            Create a coherent and flowing sentence or short paragraph that describes the traveler's style, preferences, and interests. The description should:
            1. Incorporate all the given tags naturally.
            2. Avoid simply listing the tags, but instead weave them into a narrative.
            3. Use varied language and synonyms to prevent repetition.
            4. Capture the essence of the traveler's personality and interests.
            5. Be concise yet comprehensive, ideally no more than 3-4 sentences.
            """

            travelVibe = generateResponse(travelVibePrompt)

            restaurantPrompt = f"""
            Create personalized dining recommendations for a traveler visiting {where} from {start_date} to {end_date}. The traveler's profile is as follows:

            Coming From: {origin}
            Age: {age}
            Gender: {user_gender}
            Traveler Type: {traveller_type}
            Dining Preferences: {dining_preff}

            Travel Style: {travelVibe}

            Please provide the following:

            1. Overview of {where}'s Culinary Scene:
            - Brief description of the local food culture and specialties
            - How it aligns with the traveler's preferences

            2. Specific Restaurant Recommendations:
            [For each dining preference in diningPreff, include:]
            Suggest for {dining_preff}:
            - 2 must-try establishments
            - 2 hidden gems or local favorites
            - 1 unique or trendy option

            For each recommendation, include:
            - Name and type of establishment
            - Brief description of ambiance and why it suits the traveler along with any special features

            [If travellerType is "Solo", include:]
            3. Solo Dining Location:
            - Recommend restaurants particularly suitable for solo diners
            - Suggest social dining experiences or communal tables

            [If age is under 30, include:]
            4. Youth-Friendly Options:
            - Suggest trendy, budget-friendly dining spots popular with younger travelers

            [If user tends to be culture, art explorer and want to explore local cuisines]
            5. Cultural Dining Experiences:
            - Recommend restaurants with historical significance or traditional local cuisine

            [If user wants to explore during night time and enjoy the location's nightlife, include:]
            6. Nightlife and Dining:
            - Suggest places that combine great food with a lively nightlife atmosphere

            7. Diverse Dining Experiences:
            - Suggest food markets, street food locations, or food tours that align with the traveler's interests

            [If user is early riser give some good places for breakfast]
            8. Breakfast 
            - Suggest some places with good breakfast, coffee and good views to feel fresh for whole day

            Present the recommendations in a clear, organized format, grouping suggestions by type and including a mix of options for different times of day and various locations around {where}. This will help the traveler plan diverse dining experiences throughout their trip.
            In addition to the restaurant recommendations, provide the following information in separate dictionaries:
            Include at least 3 recommendations for each dining preference specified in the traveler's profile. Ensure that the recommendations:
            1. Align with the traveler's age, traveler type, and travel style (based on travelVibeTags)
            2. Offer a mix of popular establishments and hidden gems
            3. Consider the traveler's origin for potentially interesting culinary contrasts
            4. Account for the duration of the trip ({start_date} to {end_date})

            I want you return simply a list of all the places with a short description.
            The list should be a python array with each item being a dictionary with three keys keys:- "name", "description"
            the output should be as shown:-
            Also the first item should be dictionary having field as a string which tells about overview of {where}'s Culinary Scene containing brief description of the local food culture and specialties and how it aligns with traveler's preferences. Also try to include practical dining tips like reservation recommendations and local dining customs or etiquette
            [dict0("name of place":{where}, "description":brief description), dict1("name":firstplace(that can be sesarched over maps), "description":somedesc), dict2()"name":firstplace, "description":somedesc)...]
            """

            response = generateResponse(restaurantPrompt)
            
           
            if response:
                data_string = response.text
                tag_list = json.loads(data_string)
                return jsonify({
                    "status": "success",
                    "data": tag_list
                }), 200
            else:
                return jsonify({
                    "status": "success",
                    "data": []
                }), 200
            
                
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/getAttractions', methods=['POST'])
def get_attractions():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400

        try:
            age = user_data.get('age')
            origin = user_data.get("from")
            user_gender = user_data.get('userGender')
            traveller_type = user_data.get('travellerType')
            where = user_data.get('where')
            from_location = user_data.get('from')
            start_date = user_data.get('startDate')
            end_date = user_data.get('endDate')
            travel_tags = user_data.get('travelVibeTags')
            dining_preff = user_data.get('diningPreff')
            time_of_day = user_data.get('timeOfDay')
            social_criteria = user_data.get('socialCriteria')
            activity_intensity = user_data.get('activityIntensity')
            travel_style = user_data.get('travelStyle')

            if age is None or user_gender is None or traveller_type is None or \
               where is None or from_location is None or start_date is None or \
               end_date is None or travel_tags is None or dining_preff is None or \
               time_of_day is None or social_criteria is None or activity_intensity is None or \
               travel_style is None:
                return jsonify({"error": "Missing required fields"}), 400

            if traveller_type=="Solo":
                traveller_type = "Solo " + user_gender + " traveller"

            travelVibePrompt = f"""Given the following list of travel vibe tags: {travel_tags}
            Create a coherent and flowing sentence or short paragraph that describes the traveler's style, preferences, and interests. The description should:
            1. Incorporate all the given tags naturally.
            2. Avoid simply listing the tags, but instead weave them into a narrative.
            3. Use varied language and synonyms to prevent repetition.
            4. Capture the essence of the traveler's personality and interests.
            5. Be concise yet comprehensive, ideally no more than 3-4 sentences.
            """

            travelVibe = generateResponse(travelVibePrompt)

            travelStyleprompt = f"""
            Given a value:- Travel_style = {travel_style} on scale of 1 to 5. 1 means wanting to explore only popular location and 5 means inclination towards off-beat locations.
            Create a coherent and flowing sentence that describes the traveler's style.
            Also dont mention travel style rating in response. Moreover the response should be such that it is easier for LLM Model to be able to use this to create list of place of attraction
            """

            travelStyle = generateResponse(travelStyleprompt)

            timePrompt = f"""Given a time_of_day value equal to {time_of_day} on scale of 1 to 5. Close to 1 means wanting to start seeing places from early in morning and being 4 or 5 means inclination towards staying up late and exploring till late night.
            Create a coherent and flowing sentence that describes time of day generally the traveller likes to start and mostly travel and see the places of intrest.
            Moreover the response should be such that it is easier for LLM Model to be able to use this to create and personally curate list of place of attraction
            """

            timeOfDay = generateResponse(timePrompt)

            attractionPrompt = f"""
            Create personalized places of attraction recommendations for a traveler visiting {where} from {start_date} to {end_date}. The traveler's profile is as follows:

            Coming From: {origin}
            Age: {age}
            Gender: {user_gender}
            Traveler Type: {traveller_type}
            Dining Preferences: {dining_preff}
            Time of Travel: {timeOfDay}
            Travel Style: {travelVibe}
            Tendency to explore offbeat locations: {travelStyle}


            Please provide the following:

            1. Overview of {where}'s places of attraction:
            - Brief description of the local food culture and specialties
            - How it aligns with the traveler's preferences

            2. Specific Restaurant Recommendations:
            [For each dining preference in diningPreff, include:]
            Suggest for {dining_preff}:
            - 2 must-try establishments
            - 1 hidden gems or local favorites
            - 1 unique or trendy option

            For each recommendation, include:
            - Name and type of establishment
            - Brief description of ambiance and why it suits the traveler

            [If travellerType is "Solo", include:]
            3. Solo Dining Tips:
            - Recommend restaurants particularly suitable for solo diners
            - Suggest social dining experiences or communal tables

            [If age is under 30, include:]
            4. Youth-Friendly Options:
            - Suggest trendy, budget-friendly dining spots popular with younger travelers

            [If user tends to be culture, art explorer and want to explore local cuisines]
            5. Cultural Dining Experiences:
            - Recommend restaurants with historical significance or traditional local cuisine

            [If user wants to explore during night time and enjoy the location's nightlife, include:]
            6. Nightlife and Dining:
            - Suggest places that combine great food with a lively nightlife atmosphere

            7. Practical Dining Tips:
            - Best times to visit popular restaurants
            - Reservation recommendations
            - Local dining customs or etiquette

            8. Diverse Dining Experiences:
            - Suggest food markets, street food locations, or food tours that align with the traveler's interests

            [If the trip duration is more than 5 days, include:]
            9. Neighborhood-Specific Recommendations:
            - Suggest 2-3 neighborhoods known for their food scene
            - For each, recommend options that match the traveler's dining preferences

            [If user is early riser give some good places for breakfast]
            10. Breakfast 
            - Suggest some places with good breakfast, coffee and good views to feel fresh for whole day

            Present the recommendations in a clear, organized format, grouping suggestions by type and including a mix of options for different times of day and various locations around {where}. This will help the traveler plan diverse dining experiences throughout their trip.
            In addition to the restaurant recommendations, provide the following information in separate dictionaries:
            Include at least 3 recommendations for each dining preference specified in the traveler's profile. Ensure that the recommendations:
            1. Align with the traveler's age, traveler type, and travel style (based on travelVibeTags)
            2. Offer a mix of popular establishments and hidden gems
            3. Consider the traveler's origin for potentially interesting culinary contrasts
            4. Account for the duration of the trip ({start_date} to {end_date})

            I want you return simply a list of all the places with a short description.
            The list should be a python array with each item being a dictionary with three keys keys:- "name", "description"
            the output should be as shown:-
            [dict1("name":firstplace, "description":somedesc), dict2()"name":firstplace, "description":somedesc)...]
            """

            response = generateResponse(attractionPrompt)
            
            if response:
                data_string = response.text
                tag_list = json.loads(data_string)
                return jsonify({
                    "status": "success",
                    "data": tag_list
                }), 200
            else:
                return jsonify({
                    "status": "success",
                    "data": []
                }), 200
            
                
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
