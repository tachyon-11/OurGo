package backend.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import backend.dto.userDetailDTO;
import backend.entity.User;
import backend.service.userService;

@RestController
@RequestMapping("/v1/planTrip/")
public class planATrip{
  private final userService uService;

  public planATrip(userService uService){
    this.uService = uService;
  }

  @GetMapping("/test")
  public ResponseEntity<Object> getUserDetails(@RequestBody userDetailDTO userDTO){
    User newUser = uService.saveUser(userDTO);
    return new ResponseEntity<>(newUser, HttpStatus.OK);
  }

}