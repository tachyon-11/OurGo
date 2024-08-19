package backend.dto;

import java.util.List;

public class accomodationPreffDTO {
  private Integer id;
  private List<String> accomodationPreff;

  public accomodationPreffDTO() {
  }

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public List<String> getAccomodationPreff() {
    return accomodationPreff;
  }

  public void setAccomodationPreff(List<String> accomodationPreff) {
    this.accomodationPreff = accomodationPreff;
  }
}
