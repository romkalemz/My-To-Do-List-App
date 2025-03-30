const checkImagePath = '/static/images/check.png';
const checkDeleteImagePath = '/static/images/check_delete.png';

function showSpinner() {
    const spinner = document.getElementById('loading-spinner');
    spinner.style.display = 'block'; // Show the spinner
}
function hideSpinner() {
    const spinner = document.getElementById('loading-spinner');
    spinner.style.display = 'none'; // Hide the spinner
}
// Function to get tasks from the API and render them
async function getTasks() {
    showSpinner();
    try { // Catch any network-level, or JavaScript runtime errors from fetch
        const response = await fetch('/tasks'); // Send a GET request to API (fetch default)
        if(response.ok) {
            // if response is OK, grab UL element and grab task object from API
            // and loop through task list and place one task at a time in LI element
            // and initializing the checkbox for each task
            const taskListElement = document.getElementById('task-list');
            taskListElement.innerHTML = ''; // Clear current list display (basically a refresh)
            const data = await response.json();
            data.tasks.forEach((item) => {
                const taskElement = document.createElement('li');
                taskElement.innerHTML = 
                `
                    <button onclick="updateTask(${item.id})" class="update-btn">
                        <img src="${checkImagePath}" alt="Check Icon" class="update-btn-img">
                    </button>
                    <span class="${item.status ? 'done' : ''}">
                        ${item.task}
                    </span>
                    <button onclick="deleteTask(${item.id})" class="delete-btn">
                        <img src="${checkDeleteImagePath}" alt="Delete Icon" class="delete-btn-img">
                    </button>
                `;
                taskListElement.appendChild(taskElement);
            });
        } else { // Catch any HTTP-level errors
            console.error('Failed to fetch tasks -- RESPONSE:', response.statusText);
        }
    } catch(error) {
        console.error('Failed to fetch tasks -- FETCH:', error);
    } finally {
        hideSpinner();
    }
}

// Function to add a task by sending a POST request to API and then reload page
async function addTask(event) {
    event.preventDefault();
    const taskInputElement = document.getElementById('task-input');
    // Trim leading and tracing white spaces
    // And using an external library to "sanitize" user input
    const taskString = DOMPurify.sanitize(taskInputElement.value.trim());
    // Check if valid input before sending request to API
    if(!taskString) { // Checking if string is empty
        alert('Task cannot be empty!');
        return;
    } else if(taskString.length > 100) { // Limiting size of user input
        alert('Task cannot exceed 100 characters!');
        return;
    } else {
        try {
            const response = await fetch('/tasks', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({task: taskString}), // Sending over in JSON format
            });
            if(response.ok) {
                taskInputElement.value = ''; // Clear user input
                getTasks(); // Reload tasks to display
            } else {
                console.error('Failed to add task -- RESPONSE:', response.statusText);
            }
        } catch(error) {
            console.error('Failed to add task -- FETCH:', error);
        }
    }

}

// Function to update the status of the task by sending a PUT request to API and then reload page
async function updateTask(taskId) {
    try {
        const response = await fetch(`/task/${taskId}`, {method: 'PUT'});
        if(response.ok) {
            getTasks();
        } else {
            console.error('Failed to update task -- RESPONSE:', response.statusText);
        }
    } catch(error) {
        console.error('Failed to update task -- FETCH:', error)
    }
}

// Function to delete a task by sending a DELETE request to API and then reload page
async function deleteTask(taskId) {
    try {
        const response = await fetch(`/task/${taskId}`, {method: 'DELETE'});
        if(response.ok) {
            getTasks();
        } else {
            console.error('Failed to delete task -- RESPONSE:', response.statusText);
        }
    } catch(error) {
        console.error('Failed to delete task -- FETCH:', error)
    } 
}

// GET tasks when the page loads
document.addEventListener('DOMContentLoaded', getTasks);
// POST tasks when the 'submit' button is pressed
document.getElementById('task-form').addEventListener('submit', addTask);