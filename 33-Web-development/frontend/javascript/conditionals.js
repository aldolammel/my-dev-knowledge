

// CONDITIONALS:

// Traditional:
if (localStorage.getItem("tasks")) {
    this.tasks = JSON.parse(localStorage.getItem("tasks"));
} else {
    this.tasks = this.tasks; // Fallback to existing value
}




// Ternary:
this.tasks = localStorage.getItem("tasks") ? JSON.parse(localStorage.getItem("tasks")) : this.tasks;