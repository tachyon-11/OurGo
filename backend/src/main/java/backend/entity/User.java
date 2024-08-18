package backend.entity;

import backend.enums.gender;
import backend.enums.traveller;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.util.Date;

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

  @Column(name="traveler-type")
  private traveller travellerType;

  @Column(name="where-place")
  private String where;

  @Column(name="from-place")
  private String from;

  @Column(name="start-date")
  private Date startDate;

  @Column(name="end-date")
  private Date endDate;

  public User(){
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

}
