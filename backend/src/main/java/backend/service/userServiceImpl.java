package backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.RuntimeJsonMappingException;

import java.util.Optional;
import backend.dao.userDAO;
import backend.dto.userDetailDTO;
import backend.entity.User;

@Service
public class userServiceImpl implements userService{
  @Autowired
  public userDAO userRepositoryDao;

  @Override
  public User findByUser(Integer theId) {
    Optional<User> fetchedUser = userRepositoryDao.findById(theId);
    if(fetchedUser.isPresent()){
      return fetchedUser.get();
    } else{
      throw new RuntimeJsonMappingException("No id");
    }
  }

  @Override
  public User saveUser(userDetailDTO userDTO) {
    
    User user = new User();
    user.setName(userDTO.getName());
    user.setAge(userDTO.getAge());
    user.setTravellerType(userDTO.getTypeOfTraveller());
    user.setUserGender(userDTO.getUserGender());

    user = userRepositoryDao.save(user);

    return user;
  }
  
  
}
