// Simulating a database or Json from an external service:
var tasks = [
    // { title: 'Aprender HTML, CSS e Javascript', isDone: true },
    // { title: 'Aprender o básico de Vue JS', isDone: false }
];

// Constant:
const ToDoList = {
    data() {
        return {
            tasks: window.tasks,
            newTask: {
                // Initially, all new tasks aren't done:
                isDone: false
            }
        }
    },
    methods: {
        taskAdding() {
            // This function adds a new task to the to-do-list.
            if (!this.newTask.title) {
                alert('Please, define a title for the new task.');
                return;
            }
            // Check other task titles and abort if it's duplicited:
            let isDuplicate = false;
            this.tasks.forEach((task) => {
                if (this.newTask.title.toLowerCase() === task.title.toLowerCase()) {
                    alert("This task is already on this list.");
                    isDuplicate = true;
                }
            });
            if (isDuplicate) return;

            // If everything's right, it adds the task:
            this.tasks.push(this.newTask);
            //this.newTask.isDone = false;  // Not needed 'coz newTask is already 'isDone: false'!

            // Reset form:
            this.newTask = {};
        },
        tasksClean() {
            // This function deletes all tasks, regardeless their status.
            // If no tasks available:
            if (this.tasks.length == 0) {
                alert("No task to delete.");
                return;
            }
            // Show confirmation dialog
            if (confirm("Are you sure you wanna delete all tasks?")) {
                // User clicked "OK" (Yes)
                this.tasks = [];
            }
        },
        storingTasks() {
            // This function saves the current tasks in the browser local storage.
            localStorage.setItem("tasks", JSON.stringify(this.tasks));  // converting object to string to make tasks readable!
            console.log('It was updated!');
        }
    },

    // Lifecycle-Hook: phase right after the object creation:
    created() {
        // Definitions:
        const storedTasks = localStorage.getItem("tasks");
        // Using Conditional-Ternary format:
        this.tasks = storedTasks ? JSON.parse(storedTasks) : this.tasks; // parse converts string to object back again.
    },

    // Lifecycle-Hook: phase right after the object's update (if applicable):
    updated() {

        // ONLY RECOMMENDED FOR SMALL APPLICATIONS!
        // Saving all current tasks locally (again):
        //localStorage.setItem("tasks", JSON.stringify(this.tasks));
        //console.log('It was updated!');

        // CRITICAL: this way, where you ask JS to save after an update, is too bad coz it's 
        // running each key you type in an input for example, overloading the browser in
        // more complex apps.

        // SOLUTION: create a method only to save throught the exactly moment you want,
        // calling it just when the Submit button is pressed or the task has its
        // status changed, or when the 'Delete all tasks' button is pressed.
    }
};

// I can call Vue here because the template.html is already using the VUE CDN:
Vue.createApp(ToDoList).mount('#app');  // This '#app' is the main tag id in template.html