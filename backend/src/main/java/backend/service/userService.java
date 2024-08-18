package backend.service;

import backend.dto.userDetailDTO;
import backend.entity.User;

public interface userService {
  User findByUser(Integer theId);
  User saveUser(userDetailDTO userDTO);
} 
