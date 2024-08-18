package backend.dto;

import backend.enums.gender;
import backend.enums.traveller;

public class userDetailDTO {
  private String name;
  private int age;
  private gender userGender;
  private traveller typeOfTraveller; 

  public userDetailDTO(){
    
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public gender getUserGender() {
    return userGender;
  }

  public void setUserGender(gender userGender) {
    this.userGender = userGender;
  }

  public traveller getTypeOfTraveller() {
    return typeOfTraveller;
  }

  public void setTypeOfTraveller(traveller typeOfTraveller) {
    this.typeOfTraveller = typeOfTraveller;
  }
}
