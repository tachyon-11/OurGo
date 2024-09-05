import json

def load_prompt(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data['prompt']

def wherePrompt(where):
    prompt = load_prompt('backend/llm/prompts/where_prompt.json')
    return prompt.format(where=where)

def tagPrompt(traveller_type, age, where, descriptionOfLocation):
    prompt = load_prompt('backend/llm/prompts/tag_prompt.json')
    return prompt.format(
        traveller_type=traveller_type,
        age=age,
        where=where,
        descriptionOfLocation=descriptionOfLocation
    )

def travelVibePrompt(user):
    prompt = load_prompt('backend/llm/prompts/travel_vibe_prompt.json')
    return prompt.format(user_travel_tags=user.travel_tags)

def restaurantPrompt(user, travelVibe):
  prompt = f"""
            Create personalized dining recommendations for a traveler visiting {user.where} from {user.start_date} to {user.end_date}. The traveler's profile is as follows:

            Coming From: {user.from_location}
            Age: {user.age}
            Gender: {user.user_gender}
            Traveler Type: {user.traveller_type}
            Dining Preferences: {user.dining_preff}
            User Budget: {user.user_budget}

            Travel Style: {travelVibe}

            Please provide the following:

            1. Overview of {user.where}'s Culinary Scene:
            - Brief description of the local food culture and specialties
            - How it aligns with the traveler's preferences

            2. Specific Restaurant Recommendations:
            [For each dining preference in diningPreff, include:]
            Suggest for {user.dining_preff}:
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

            Present the recommendations in a clear, organized format, grouping suggestions by type and including a mix of options for different times of day and various locations around {user.where}. This will help the traveler plan diverse dining experiences throughout their trip.
            In addition to the restaurant recommendations, provide the following information in separate dictionaries:
            Include at least 3 recommendations for each dining preference specified in the traveler's profile. Ensure that the recommendations:
            1. Align with the traveler's age, traveler type, and travel style (based on travelVibeTags)
            2. Offer a mix of popular establishments and hidden gems
            3. Consider the traveler's origin for potentially interesting culinary contrasts
            4. Account for the duration of the trip ({user.start_date} to {user.end_date})

            I want you return simply a list of all the places with a short description.
            The list should be a python array with each item being a dictionary with three keys keys:- "name", "description"
            the output should be as shown:-
            Also the first item should be dictionary having field as a string which tells about overview of {user.where}'s Culinary Scene containing brief description of the local food culture and specialties and how it aligns with traveler's preferences. Also try to include practical dining tips like reservation recommendations and local dining customs or etiquette
            [dict0("name of place":{user.where}, "description":brief description in not more than 2-3 line explaining culinary experience, type of cusines at {user.where}), dict1("name":Name of the place, "description":Short description about the place), dict2()"name":Name of the place, "description":Short description about the place)...]
            """
  return prompt

def travelStylePrompt(user):
    prompt = load_prompt('backend/llm/prompts/travel_style_prompt.json')
    return prompt.format(user_travel_style=user.travel_style)

def timePrompt(user):
    prompt = load_prompt('backend/llm/prompts/time_prompt.json')
    return prompt.format(user_time_of_day=user.time_of_day)

def attractionPrompt(user, travelVibe, timeOfDay, travelStyle):
  prompt = f"""
            Generate personalized travel recommendations for a visitor to {user.where}. Use the following traveler information to tailor your suggestions. Make sure that places you suggest are well curated for user's needs making it easier for them easily choose some or aall places form the listed places so that they can easily plan their trip accordingly:

            Age: {user.age}
            Gender applicable specificallyt if traveller type is solo: {user.user_gender}
            Travel Dates: {user.start_date} to {user.end_date}
            Travel Style describing tendency of user to visit popular places or explore off-beat locations: {travelStyle}
            Travel vibes describing general way user likes to travel: {travelVibe}
            Group Type: {user.traveller_type}
            Budget of User: {user.user_budget}
            Time User likes to travel: {timeOfDay}

            Based on this information, provide the following:

            1. Brief overview of {user.where} and why it might appeal to this traveler.

            2. Top 5 attractions or places to visit, considering the traveler's interests and style. For each, include:
            - Name of the attraction
            - Brief description (2-3 sentences)

            3.Some off-the-beaten-path or unique experiences depending on user's travel style that align with the traveler's interests.

            4. A suggested activity or place that caters specifically to the traveler's age group.

            5. Ensure that the places you suggest are align with user's budget limit as well.

            6. If the group type includes children or is a family, include 1-2 family-friendly attractions or activities.

            7. If the group consist of girls also ensure to that places suggested are specifically safe 

            I want you return simply a list of all the places with a short description.
            The list should be a python array with each item being a dictionary with three keys keys:- "name", "description"
            the output should be as shown:-
            [
                "name": "Name of first place", "description": "Some description of that place",
                "name": "Name of second Place", "description": "Some description of that place",
                # ... more dictionaries ...
            ]
            """
  return prompt

