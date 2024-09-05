from flask import Flask, request, jsonify
import google.generativeai as genai
import json
import random
import time
from prompts import *
from userProfile import UserProfile

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
            user = UserProfile(user_data)

            if user.age is None or user.user_gender is None or user.traveller_type is None or \
               user.where is None or user.from_location is None or user.start_date is None or \
               user.end_date is None:
                return jsonify({"error": "Missing required fields"}), 400

            if user.traveller_type=="Solo":
                user.traveller_type = "Solo " + user.user_gender + " traveller"
            
            descriptionOfLocation = generateResponse(wherePrompt(user.where))
            response = generateResponse(tagPrompt(user.traveller_type, user.age, user.where, descriptionOfLocation))
            
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
            user = UserProfile(user_data)

            if user.age is None or user.user_gender is None or user.traveller_type is None or \
               user.where is None or user.from_location is None or user.start_date is None or \
               user.end_date is None or user.travel_tags is None or user.dining_preff is None:
                return jsonify({"error": "Missing required fields"}), 400

            if user.traveller_type=="Solo":
                user.traveller_type = "Solo " + user.user_gender + " traveller"

            travelVibe = generateResponse(travelVibePrompt(user))

            prompt = restaurantPrompt(user, travelVibe.text)

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

@app.route('/getAttractions', methods=['POST'])
def get_attractions():
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400

        try:
            user = UserProfile(user_data)

            if user.age is None or user.user_gender is None or user.traveller_type is None or \
               user.where is None or user.from_location is None or user.start_date is None or \
               user.end_date is None or user.travel_tags is None or user.dining_preff is None:
                return jsonify({"error": "Missing required fields"}), 400

            if user.traveller_type=="Solo":
                user.traveller_type = "Solo " + user.user_gender + " traveller"

            travelVibe = generateResponse(travelVibePrompt(user))

            travelStyle = generateResponse(travelStylePrompt(user))

            timeOfDay = generateResponse(timePrompt(user))

            response = generateResponse(attractionPrompt(user, travelVibe.text, timeOfDay.text, travelStyle.text))
            
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
