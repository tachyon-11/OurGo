package backend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.MediaType;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.RuntimeJsonMappingException;

import backend.dto.LocationRequestDTO;
import backend.dto.accomodationPreffDTO;
import backend.dto.diningPreffDetailsDTO;
import backend.dto.sliderInputDTO;
import backend.dto.travelVibesDTO;
import backend.dto.userDetailDTO;
import backend.entity.User;
import backend.service.userService;

@RestController
@RequestMapping("/v1/planTrip/")
public class planATrip {
    private final userService uService;
    private final RestTemplate restTemplate = new RestTemplate();

    @Autowired
    public planATrip(userService uService) {
        this.uService = uService;
    }

    @PostMapping("/userInfo")
    public ResponseEntity<User> getUserDetails(@RequestBody userDetailDTO userDTO) {
        User newUser = uService.saveUser(userDTO);
        return new ResponseEntity<>(newUser, HttpStatus.CREATED);
    }

    @PostMapping("/locationInfo")
    public ResponseEntity<User> getLocationDetails(@RequestBody LocationRequestDTO locationRequestDTO) {
        User updatedUser = uService.saveLocation(locationRequestDTO.getId(), locationRequestDTO.getLocationDTO());
        return new ResponseEntity<>(updatedUser, HttpStatus.OK);
    }

    @PostMapping("/setTravelVibesTags")
    public ResponseEntity<String> setTravelVibeTags(@RequestBody Integer theId) {
        User user = uService.findByUser(theId);
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String userJson = objectMapper.writeValueAsString(user);
        
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> entity = new HttpEntity<>(userJson, headers);
        
            try {
                ResponseEntity<String> response = restTemplate.exchange(
                    "http://localhost:6000//generateTags",
                    HttpMethod.POST,
                    entity,
                    String.class
                );
        
                return response;
        
            } catch (HttpClientErrorException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
        
            } catch (RestClientException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
            }
        
        } catch (Exception e) {
            throw new RuntimeJsonMappingException("Error converting User to JSON: " + e.getMessage());
        }
    }

    @PostMapping("/getTravelVibesTags")
    public ResponseEntity<User> getTravelVibeTags(@RequestBody travelVibesDTO travelVibesTags){
        User updatedUser = uService.saveTravelVibeTags(travelVibesTags.getId(), travelVibesTags.getTravelVibeTags());
        return new ResponseEntity<>(updatedUser, HttpStatus.OK);
    }

    @PostMapping("/setDiningPrefference")
    public ResponseEntity<User> getDiningPrefference(@RequestBody diningPreffDetailsDTO diningPreffDTO){
        User updatedUser = uService.saveDiningPreff(diningPreffDTO.getId(), diningPreffDTO.getDiningPreff());
        return new ResponseEntity<>(updatedUser, HttpStatus.OK);
    }

    @PostMapping("/setAccomodationPrefference")
    public ResponseEntity<User> getAccomodationPrefference(@RequestBody accomodationPreffDTO accomodationDTO){
        User updatedUser = uService.saveAccomodationPreff(accomodationDTO.getId(), accomodationDTO.getAccomodationPreff());
        return new ResponseEntity<>(updatedUser, HttpStatus.OK);
    }

    @PostMapping("/setTravelSliders")
    public ResponseEntity<User> getTravelSliders(@RequestBody sliderInputDTO sliderInput){
        User updatedUser = uService.saveSliderInfo(sliderInput.getId(), sliderInput.getSlider());
        return new ResponseEntity<>(updatedUser, HttpStatus.OK);
    }

    @PostMapping("/getRestaurants")
    public ResponseEntity<String> getRestaurants(@RequestBody Integer theId) {
        User user = uService.findByUser(theId);
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String userJson = objectMapper.writeValueAsString(user);
        
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> entity = new HttpEntity<>(userJson, headers);
        
            try {
                ResponseEntity<String> response = restTemplate.exchange(
                    "http://localhost:6000/getRestaurants",
                    HttpMethod.POST,
                    entity,
                    String.class
                );
        
                return response;
        
            } catch (HttpClientErrorException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
        
            } catch (RestClientException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
            }
        
        } catch (Exception e) {
            throw new RuntimeJsonMappingException("Error converting User to JSON: " + e.getMessage());
        }
    }

    @PostMapping("/getAttraction")
    public ResponseEntity<String> getAttractions(@RequestBody Integer theId) {
        User user = uService.findByUser(theId);
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String userJson = objectMapper.writeValueAsString(user);
        
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            HttpEntity<String> entity = new HttpEntity<>(userJson, headers);
        
            try {
                ResponseEntity<String> response = restTemplate.exchange(
                    "http://localhost:6000/getAttractions",
                    HttpMethod.POST,
                    entity,
                    String.class
                );
        
                return response;
        
            } catch (HttpClientErrorException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
        
            } catch (RestClientException e) {
                throw new RuntimeJsonMappingException("Error calling Python service: " + e.getMessage());
            }
        
        } catch (Exception e) {
            throw new RuntimeJsonMappingException("Error converting User to JSON: " + e.getMessage());
        }
    }

    
}
