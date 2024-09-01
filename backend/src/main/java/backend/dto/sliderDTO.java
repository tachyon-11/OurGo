package backend.dto;

public class sliderDTO {
    private Integer travelStyle;
    private Integer timeOfDay;
    private Integer socialCriteria;
    private Integer activityIntensity;

    public sliderDTO(){
      travelStyle = -1;
      timeOfDay = -1;
      socialCriteria = -1;
      activityIntensity = -1;
    }

    public Integer getTravelStyle() {
        return travelStyle;
    }

    public void setTravelStyle(Integer travelStyle) {
        this.travelStyle = travelStyle;
    }

    public Integer getTimeOfDay() {
        return timeOfDay;
    }

    public void setTimeOfDay(Integer timeOfDay) {
        this.timeOfDay = timeOfDay;
    }

    public Integer getSocialCriteria() {
        return socialCriteria;
    }

    public void setSocialCriteria(Integer socialCriteria) {
        this.socialCriteria = socialCriteria;
    }

    public Integer getActivityIntensity() {
        return activityIntensity;
    }

    public void setActivityIntensity(Integer activityIntensity) {
        this.activityIntensity = activityIntensity;
    }
}
