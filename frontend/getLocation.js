import { userID } from "./getUser.js";
import { tagsForm } from "./getTags.js";
import { mainBar } from "./window.js";

var travellerTags;

const locationFrom = document.createElement("form");
locationFrom.id = "locationForm";

const whereLabel = document.createElement("label");
whereLabel.setAttribute("for", "where");
whereLabel.textContent = "Destination:";
const whereInput = document.createElement("input");
whereInput.type = "text";
whereInput.id = "where";
whereInput.name = "where";
whereInput.required = true;

const fromLabel = document.createElement("label");
fromLabel.setAttribute("for", "from");
fromLabel.textContent = "From:";
const fromInput = document.createElement("input");
fromInput.type = "text";
fromInput.id = "from";
fromInput.name = "from";
fromInput.required = true;

const startDateLabel = document.createElement("label");
startDateLabel.setAttribute("for", "startDate");
startDateLabel.textContent = "Start Date:";
const startDateInput = document.createElement("input");
startDateInput.type = "date";
startDateInput.id = "startDate";
startDateInput.name = "startDate";
startDateInput.required = true;

const endDateLabel = document.createElement("label");
endDateLabel.setAttribute("for", "endDate");
endDateLabel.textContent = "End Date:";
const endDateInput = document.createElement("input");
endDateInput.type = "date";
endDateInput.id = "endDate";
endDateInput.name = "endDate";
endDateInput.required = true;

const submitButton = document.createElement("button");
submitButton.type = "submit";
submitButton.textContent = "Next";

locationFrom.appendChild(whereLabel);
locationFrom.appendChild(whereInput);
locationFrom.appendChild(fromLabel);
locationFrom.appendChild(fromInput);
locationFrom.appendChild(startDateLabel);
locationFrom.appendChild(startDateInput);
locationFrom.appendChild(endDateLabel);
locationFrom.appendChild(endDateInput);
locationFrom.appendChild(submitButton);

locationFrom.addEventListener("submit", async function (event) {
  event.preventDefault();

  const locationData = {
    id: userID,
    locationDTO: {
      where: document.getElementById("where").value,
      from: document.getElementById("from").value,
      startDate: new Date(
        document.getElementById("startDate").value
      ).toISOString(),
      endDate: new Date(document.getElementById("endDate").value).toISOString(),
    },
  };

  try {
    const locationResponse = await fetch(
      "http://localhost:8080/v1/planTrip/locationInfo",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(locationData),
      }
    );

    if (!locationResponse.ok) {
      throw new Error("Network response was not ok for locationInfo");
    }

    const tagsResponse = await fetch(
      "http://localhost:8080/v1/planTrip/setTravelVibesTags",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userID),
      }
    );

    if (!tagsResponse.ok) {
      throw new Error("Network response was not ok for setTravelVibesTags");
    }

    const tagsData = await tagsResponse.json();
    console.log("Travel Vibes Tags Success:", tagsData);
    travellerTags = tagsData.data;

    updateTagsForm();

    console.log(travellerTags);
  } catch (error) {
    console.error("Error:", error);
  }

  mainBar.replaceChildren();
  mainBar.appendChild(tagsForm);
});

function updateTagsForm() {
  tagsForm.innerHTML = "";

  travellerTags.forEach((tag) => {
    const tagContainer = document.createElement("div");

    const tagInput = document.createElement("input");
    tagInput.type = "checkbox";
    tagInput.id = tag;
    tagInput.name = "tags";
    tagInput.value = tag;

    const tagLabel = document.createElement("label");
    tagLabel.setAttribute("for", tag);
    tagLabel.textContent = tag;

    tagContainer.appendChild(tagInput);
    tagContainer.appendChild(tagLabel);

    tagsForm.appendChild(tagContainer);
  });

  const submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.textContent = "Next";
  tagsForm.appendChild(submitButton);

  tagsForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const selectedTags = Array.from(
      document.querySelectorAll('input[name="tags"]:checked')
    ).map((input) => input.value);

    const data = {
      id: userID,
      travelVibeTags: selectedTags,
    };

    fetch("http://localhost:8080/v1/planTrip/getTravelVibesTags", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((responseData) => {
        console.log("Success:", responseData);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
}

export { locationFrom, travellerTags };
