// Simulating a database or Json from an external service:
var members = [
    {
        fname: 'John',
        lname: 'Lennon',
        role: 'Acoustic Guitar'
    },
    {
        fname: 'George',
        lname: 'Harrison',
        role: 'Guitar'
    }
];

// Constant:
const handlingForms = {
    // Property as function:
    data() {
        // Object:
        // Returning an object (everything inside this will be accessable through the app)!
        return {
            // Property:
            members: window.members,
                // If you want to call members attributes through the templates,
                // you can use {{ members[0].role }} to take the first member role, e.g.
            newMember: {}  // Vue.js understands you want to use the same fields from the form!
        }
    },
    // Methods (custom code) to use through the templates:
    methods: {
        addMember() {
            // This function includes a new member to the musician's list.
            // Validate fields
            if (!this.newMember.fname || !this.newMember.lname || !this.newMember.role) {
                alert('Please fill all fields');
                return;
            }
            // Add new member:
            this.members.push(this.newMember); // '.push' adds something in the array's end.
            // Reset form:
            this.newMember = {};
        },
        removeMember(idx) {
            // This function removes a member to the musician's list.
            // Remove 1 element at the specific index: 
            this.members.splice(idx, 1);
        }
    }
};

// I can call Vue here because the template.html is already using the VUE CDN:
Vue.createApp(handlingForms).mount('#app');  // This '#app' is the main tag id in template.html
