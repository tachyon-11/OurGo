package backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.RuntimeJsonMappingException;

import java.util.List;
import java.util.Optional;
import backend.dao.userDAO;
import backend.dto.locationDetailDTO;
import backend.dto.sliderDTO;
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
    user.setUserBudget(userDTO.getUserBudget());
    user = userRepositoryDao.save(user);
    return user;
  }

  @Override
  public User saveLocation(Integer id, locationDetailDTO locationDTO){
    Optional<User> fetchedUser = userRepositoryDao.findById(id);
    User user = fetchedUser.get();
    user.setWhere(locationDTO.getWhere());
    user.setFrom(locationDTO.getFrom());
    user.setStartDate(locationDTO.getStartDate());
    user.setEndDate(locationDTO.getEndDate());
    user = userRepositoryDao.save(user);
    return user;
  }

  @Override
  public User saveDiningPreff(Integer id, List<String> diningPreff) {
    Optional<User> fetchedUser = userRepositoryDao.findById(id);
    User user = fetchedUser.get();
    user.setDiningPreff(diningPreff);
    user = userRepositoryDao.save(user);
    return user;
  }

  @Override
  public User saveAccomodationPreff(Integer id, List<String> accomodationPreff) {
    Optional<User> fetchedUser = userRepositoryDao.findById(id);
    User user = fetchedUser.get();
    user.setAccommodation(accomodationPreff);
    user = userRepositoryDao.save(user);
    return user;
  }

  @Override
  public User saveSliderInfo(Integer id, sliderDTO slider) {
    Optional<User> fetchedUser = userRepositoryDao.findById(id);
    User user = fetchedUser.get();
    user.setActivityIntensity(slider.getActivityIntensity());
    user.setSocialCriteria(slider.getSocialCriteria());
    user.setTimeOfDay(slider.getTimeOfDay());
    user.setTravelStyle(slider.getTravelStyle());
    user = userRepositoryDao.save(user);
    return user;
  }

  @Override
  public User saveTravelVibeTags(Integer id, List<String> travelVibeTags) {
    Optional<User> fetchedUser = userRepositoryDao.findById(id);
    User user = fetchedUser.get();
    user.setTravelVibeTags(travelVibeTags);
    user = userRepositoryDao.save(user);
    return user;
  }
}
