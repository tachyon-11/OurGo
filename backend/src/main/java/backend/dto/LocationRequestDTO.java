package backend.dto;

public class LocationRequestDTO {
  private Integer id;
  private locationDetailDTO locationDTO;

  public Integer getId() {
      return id;
  }

  public void setId(Integer id) {
      this.id = id;
  }

  public locationDetailDTO getLocationDTO() {
      return locationDTO;
  }

  public void setLocationDTO(locationDetailDTO locationDTO) {
      this.locationDTO = locationDTO;
  }
}

