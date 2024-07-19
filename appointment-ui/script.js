// script.js
document.addEventListener('DOMContentLoaded', function() {
  // Function to fetch doctor's availability from JSON
  function fetchDoctorAvailability() {
    return fetch('doctor.json') // Replace 'doctor.json' with your JSON file path
      .then(response => response.json())
      .catch(error => {
        console.error('Error fetching JSON:', error);
        return null;
      });
  }

  // Function to fetch booked slots from CSV
  function fetchBookedSlots() {
    return fetch('booked.csv') // Replace 'booked.csv' with your CSV file path
      .then(response => response.text())
      .then(csv => {
        const lines = csv.split('\n');
        const bookedSlots = lines.map(line => {
          if (!line.trim()) {
            return null; // Skip empty lines
          }
          const [name, day, time, contact] = line.split(',');
          return { name, day, time, contact };
        }).filter(slot => slot !== null); // Filter out null values
        return bookedSlots;
      })
      .catch(error => {
        console.error('Error fetching CSV:', error);
        return [];
      });
  }
  

  // Function to create slot HTML
  function createSlotHTML(slot, available, bookedInfo) {
    const slotDiv = document.createElement('div');
    slotDiv.classList.add('slot');
    if (available) {
      slotDiv.classList.add('available');
      slotDiv.innerHTML = `${slot} - Available`;
    } else {
      slotDiv.classList.add('booked');
      slotDiv.innerHTML = `${slot} - ${bookedInfo.name}`;
    }
    return slotDiv;
  }

  // Function to render slots for a day
  function renderSlots(dayElement, dayData, bookedSlots) {
    dayData.slots.forEach(slot => {
      const bookedSlot = bookedSlots.find(bSlot => bSlot.day.toLowerCase() === dayData.day.toLowerCase() && bSlot.time === slot);
      const slotHTML = createSlotHTML(slot, !bookedSlot, bookedSlot || {});
      dayElement.appendChild(slotHTML);
    });
  }

  // Fetch data and render slots
  Promise.all([fetchDoctorAvailability(), fetchBookedSlots()])
    .then(([doctorData, bookedSlots]) => {
      if (!doctorData) {
        console.error('Doctor data not available.');
        return;
      }

      const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
      const weekend = "Saturday";

      // Render weekdays
      weekdays.forEach(day => {
        const dayData = doctorData.availability.weekdays.find(d => d.day.toLowerCase() === day.toLowerCase());
        const dayElement = document.getElementById(day.toLowerCase());
        if (dayData && dayElement) {
          renderSlots(dayElement, dayData, bookedSlots);
        }
      });

      // Render weekend
      const weekendData = doctorData.availability.weekends.find(d => d.day.toLowerCase() === weekend.toLowerCase());
      const weekendElement = document.getElementById(weekend.toLowerCase());
      if (weekendData && weekendElement) {
        renderSlots(weekendElement, weekendData, bookedSlots);
      }
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});
