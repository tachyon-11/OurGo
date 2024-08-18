package backend.service;

import backend.dto.locationDetailDTO;
import backend.dto.userDetailDTO;
import backend.entity.User;

public interface userService {
  User findByUser(Integer theId);
  User saveUser(userDetailDTO userDTO);
  public User saveLocation(Integer id, locationDetailDTO locationDTO);
} 
