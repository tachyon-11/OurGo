from flask import Flask, request, jsonify
import google.generativeai as genai
import json
import random
import time

genai.configure(api_key='')
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

def generateResponse(prompt, max_retries=1):
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
def process_user():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
