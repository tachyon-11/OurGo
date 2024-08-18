package backend.dao;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;
import backend.entity.User;

@Repository
public interface userDAO extends CrudRepository<User, Integer>{
  User save(User newUser);
  Optional<User> findById(Integer id);
}
