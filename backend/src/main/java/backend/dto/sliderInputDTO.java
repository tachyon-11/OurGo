package backend.dto;

public class sliderInputDTO {
  private Integer id;
  private sliderDTO slider;

  public sliderInputDTO() {
  }

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public sliderDTO getSlider() {
    return slider;
  }

  public void setSlider(sliderDTO slider) {
    this.slider = slider;
  }
}
