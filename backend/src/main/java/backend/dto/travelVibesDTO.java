package backend.dto;
import java.util.List;

public class travelVibesDTO {
  private Integer id;
  private List<String> travelVibeTags;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public List<String> getTravelVibeTags() {
    return travelVibeTags;
  }

  public void setTravelVibeTags(List<String> travelVibeTags) {
    this.travelVibeTags = travelVibeTags;
  }
}