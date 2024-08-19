package backend.service;

import backend.dto.locationDetailDTO;
import backend.dto.userDetailDTO;
import backend.entity.User;

import java.util.List;

public interface userService {
  User findByUser(Integer theId);
  User saveUser(userDetailDTO userDTO);
  User saveLocation(Integer id, locationDetailDTO locationDTO);
  User saveDiningPreff(Integer id, List<String> diningPreff);
  User saveAccomodationPreff(Integer id, List<String> accomodationPreff);
} 
