package backend.entity;

import backend.enums.budget;
import backend.enums.gender;
import backend.enums.traveller;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.util.Date;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonFormat;

@Entity
@Table(name = "user")
public class User {
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(name="id")
  private Integer id;

  @Column(name="name")
  private String name;

  @Column(name="age")
  private Integer age;

  @Column(name="gender")
  private gender userGender;

  @Column(name="budget")
  private budget userBudget;

  @Column(name="traveler-type")
  private traveller travellerType;

  @Column(name="where-place")
  private String where;

  @Column(name="from-place")
  private String from;

  @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss.SSSXXX")
  @Column(name="start-date")
  private Date startDate;

  @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss.SSSXXX")
  @Column(name="end-date")
  private Date endDate;

  @Column(name="travel-vibe-tags")
  private List<String> travelVibeTags;

  @Column(name="accomodation")
  private List<String> accommodation;

  @Column(name="diningPreff")
  private List<String> diningPreff;

  @Column(name="travel-style")
  private Integer travelStyle = -1;

  @Column(name="time-of-day")
  private Integer timeOfDay = -1;

  @Column(name="social-criteria")
  private Integer socialCriteria = -1;

  @Column(name="activity-intensity")
  private Integer activityIntensity = -1;

  public User() {
  }

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Integer getAge() {
    return age;
  }

  public void setAge(Integer age) {
    this.age = age;
  }

  public gender getUserGender() {
    return userGender;
  }

  public budget getUserBudget(){
    return userBudget;
  }

  public void setUserBudget(budget userBudget){
    this.userBudget = userBudget;
  }

  public void setUserGender(gender userGender) {
    this.userGender = userGender;
  }

  public traveller getTravellerType() {
    return travellerType;
  }

  public void setTravellerType(traveller travellerType) {
    this.travellerType = travellerType;
  }

  public String getWhere() {
    return where;
  }

  public void setWhere(String where) {
    this.where = where;
  }

  public String getFrom() {
    return from;
  }

  public void setFrom(String from) {
    this.from = from;
  }

  public Date getStartDate() {
    return startDate;
  }

  public void setStartDate(Date startDate) {
    this.startDate = startDate;
  }

  public Date getEndDate() {
    return endDate;
  }

  public void setEndDate(Date endDate) {
    this.endDate = endDate;
  }

  public List<String> getTravelVibeTags() {
    return travelVibeTags;
  }

  public void setTravelVibeTags(List<String> travelVibeTags) {
    this.travelVibeTags = travelVibeTags;
  }

  public List<String> getAccommodation() {
    return accommodation;
  }

  public void setAccommodation(List<String> accommodation) {
    this.accommodation = accommodation;
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

  public List<String> getDiningPreff(){
    return diningPreff;
  }

  public void setDiningPreff(List<String> diningPreff){
    this.diningPreff = diningPreff;
  }
}
