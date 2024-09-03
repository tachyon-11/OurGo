import { locationFrom } from "./getLocation.js";
import { mainBar } from "./window.js";

let userID;

const userForm = document.createElement("form");
userForm.id = "getUser";

const nameLabel = document.createElement("label");
nameLabel.textContent = "Name: ";
const nameInput = document.createElement("input");
nameInput.type = "text";
nameInput.name = "name";
nameInput.id = "name";
nameInput.placeholder = "Enter your name";
userForm.appendChild(nameLabel);
userForm.appendChild(nameInput);
userForm.appendChild(document.createElement("br"));

const ageLabel = document.createElement("label");
ageLabel.textContent = "Age: ";
const ageInput = document.createElement("input");
ageInput.type = "number";
ageInput.name = "age";
ageInput.id = "age";
ageInput.placeholder = "Enter your age";
userForm.appendChild(ageLabel);
userForm.appendChild(ageInput);
userForm.appendChild(document.createElement("br"));

const genderLabel = document.createElement("label");
genderLabel.textContent = "Gender: ";
const genderSelect = document.createElement("select");
genderSelect.name = "userGender";
genderSelect.id = "userGender";
["Male", "Female", "Other"].forEach(gender => {
  const option = document.createElement("option");
  option.value = gender;
  option.textContent = gender;
  genderSelect.appendChild(option);
});
userForm.appendChild(genderLabel);
userForm.appendChild(genderSelect);
userForm.appendChild(document.createElement("br"));

const travellerLabel = document.createElement("label");
travellerLabel.textContent = "Type of Traveller: ";
const travellerSelect = document.createElement("select");
travellerSelect.name = "typeOfTraveller";
travellerSelect.id = "typeOfTraveller";
["Solo", "Couple", "Family", "Group"].forEach(type => {
  const option = document.createElement("option");
  option.value = type;
  option.textContent = type;
  travellerSelect.appendChild(option);
});
userForm.appendChild(travellerLabel);
userForm.appendChild(travellerSelect);
userForm.appendChild(document.createElement("br"));

const budgetLabel = document.createElement("label");
budgetLabel.textContent = "Budget: ";
const budgetSelect = document.createElement("select");
budgetSelect.name = "userBudget";
budgetSelect.id = "userBudget";
["Low", "Medium", "High", "Flexible"].forEach(budget => {
  const option = document.createElement("option");
  option.value = budget;
  option.textContent = budget;
  budgetSelect.appendChild(option);
});
userForm.appendChild(budgetLabel);
userForm.appendChild(budgetSelect);
userForm.appendChild(document.createElement("br"));

const submitButton = document.createElement("button");
submitButton.type = "submit";
submitButton.textContent = "Next";
userForm.appendChild(submitButton);

userForm.addEventListener('submit', function(event) {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;
  const userGender = document.getElementById('userGender').value;
  const typeOfTraveller = document.getElementById('typeOfTraveller').value;
  const userBudget = document.getElementById('userBudget').value;

  const data = {
    name: name,
    age: parseInt(age),
    userGender: userGender,
    typeOfTraveller: typeOfTraveller,
    userBudget: userBudget
  };

  fetch('http://localhost:8080/v1/planTrip/userInfo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Success:', data);
    userID = data.id;
  })
  .catch((error) => {
    console.error("Error:", error);
  });

  mainBar.replaceChildren();
  mainBar.appendChild(locationFrom);
});


export {userForm, userID}