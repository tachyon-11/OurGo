package backend.dto;

import java.util.List;

public class diningPreffDetailsDTO {
  private Integer id;
  private List<String> diningPreff;

  public diningPreffDetailsDTO() {
  }

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public List<String> getDiningPreff() {
    return diningPreff;
  }

  public void setDiningPreff(List<String> diningPreff) {
    this.diningPreff = diningPreff;
  }
}