const checkImagePath = '/static/images/check.png';
// Function to get tasks from the API and render them
async function getTasks() {
    try { // Catch any network-level, or JavaScript runtime errors from fetch
        const response = await fetch('/tasks', ['GET']);
        if (response.ok) {
            // if response is OK, grab UL element and grab task object from API
            // and loop through task list and place one task at a time in LI element
            // and initializing the checkbox for each task
            const taskListElement = document.getElementById('task-list');
            taskListElement.innerHTML = ''; // Clear current list display (basically a refresh)
            const data = await response.json();
            data.tasks.forEach((item, index) => {
                const taskElement = document.createElement('li');
                taskElement.innerHTML = `
                    <button onclick="updateTask({${index})" class="update-btn">
                        <img src="${checkImagePath}" alt="Check Icon" class="update-btn-img">
                    </button>
                    <span class="$item.status ? 'done' : ''}">${item.task}</span>
                `;
                taskListElement.appendChild(taskElement);
            });
        } else { // Catch any HTTP-level errors
            console.error('Failed to fetch tasks -- RESPONSE:', response.statusText);
        }
    } catch (error) {
        console.error('Failed to fetch tasks -- FETCH:', error);
    }
}

// Function to add a task by sending a POST request to API and then reload page


// Function to update the status of the task by sending a PUT request to API and then reload page


// GET tasks when the page loads
document.addEventListener('DOMContentLoaded', getTasks);
// POST tasks when the 'submit' button is pressed
//document.getElementById('task-form').addEventListener('submit', addTask);