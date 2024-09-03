class UserProfile:
    
    def __init__(self, user_data):
        self.age = user_data.get('age')
        self.user_gender = user_data.get('userGender')
        self.traveller_type = user_data.get('travellerType')
        self.where = user_data.get('where')
        self.from_location = user_data.get('from')
        self.start_date = user_data.get('startDate')
        self.end_date = user_data.get('endDate')
        self.travel_tags = user_data.get('travelVibeTags')
        self.dining_preff = user_data.get('diningPreff')
        self.time_of_day = user_data.get('timeOfDay')
        self.social_criteria = user_data.get('socialCriteria')
        self.activity_intensity = user_data.get('activityIntensity')
        self.travel_style = user_data.get('travelStyle')
        self.user_budget = user_data.get('userBudget')
