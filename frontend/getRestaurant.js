// Google Maps API initialization
(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})
  ({key: "AIzaSyBKZEr-WcBuV7OE3LGebFmRBAUYtONhTGs", v: "weekly"});
  
function createElement(tag, attributes = {}, textContent = '') {
  const element = document.createElement(tag);
  Object.entries(attributes).forEach(([key, value]) => {
    element.setAttribute(key, value);
  });
  if (textContent) element.textContent = textContent;
  return element;
}

function createUI() {
  const window = document.querySelector('.window');
  
  const form = createElement('form', { id: 'userIdForm' });
  const input = createElement('input', { type: 'number', id: 'userId', placeholder: 'Enter User ID', required: 'required' });
  const button = createElement('button', { type: 'submit' }, 'Fetch Restaurants');
  
  form.appendChild(input);
  form.appendChild(button);
  window.appendChild(form);
  
  const resultDiv = createElement('div', { id: 'result' });
  window.appendChild(resultDiv);
}

async function findRestaurant(placeName) {
  const { Place } = await google.maps.importLibrary("places");
  const request = {
    textQuery: placeName,
    fields: ["displayName", "location"],
    language: "en-US",
    maxResultCount: 8
  };

  const { places } = await Place.searchByText(request);
  let placeValue = JSON.stringify(places[0]);
  console.log(placeValue);
  return placeValue;
}

async function fetchAndDisplayRestaurants(userId) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = 'Fetching restaurants...';
  console.log(`Fetching restaurants for user ID: ${userId}`);

  try {
    const response = await fetch('http://localhost:8080/v1/planTrip/getRestaurants', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userId),
    });

    const data = await response.json();
    console.log('API Response:', data);

    if (data.status === 'success') {
      console.log('Successfully fetched restaurants');
      console.log('Restaurant List:');
      data.data.forEach((restaurant, index) => {
        console.log(findRestaurant(restaurant.name));
      });

      resultDiv.textContent = `Found ${data.data.length} restaurants. Check console for the list.`;
    } else {
      console.error('Failed to fetch restaurants:', data);
      resultDiv.textContent = 'Failed to fetch restaurants';
    }
  } catch (error) {
    console.error('Error fetching restaurants:', error);
    resultDiv.textContent = `Error: ${error.message}`;
  }
}

function setupEventListeners() {
  const form = document.getElementById('userIdForm');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userId = document.getElementById('userId').value;
    await fetchAndDisplayRestaurants(userId);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  createUI();
  setupEventListeners();
});