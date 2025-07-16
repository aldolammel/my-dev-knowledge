// Simulating a database or JSON from an external service:
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

// Import ref from Vue for reactivity
const { ref, createApp } = Vue;

// Composition API approach using setup() function, instead of <script setup> in a .vue file:
const handlingForms = {
    setup() {
        // Reactive data - equivalent to data() in Options API
        // Convert properties to reactive references using ref()
        const membersRef = ref(window.members);
            // If you want to call members attributes through the templates,
            // you can use {{ members[0].role }} to take the first member role, e.g.
        const newMember = ref({}); // Vue.js understands you want to use the same fields from the form!
        
        // Methods (custom functions) to use through the templates:
        const addMember = () => {
            // This function includes a new member to the musician's list.
            // Validate fields - access reactive values using .value
            if (!newMember.value.fname || !newMember.value.lname || !newMember.value.role) {
                alert('Please fill all fields');
                return;
            }
            // Add new member to the reactive array:
            membersRef.value.push(newMember.value); // '.push' adds something in the array's end.
            // Reset form by assigning new empty object:
            newMember.value = {};
        };
        
        const removeMember = (idx) => {
            // This function removes a member from the musician's list.
            // Remove 1 element at the specific index using splice:
            membersRef.value.splice(idx, 1);
        };
        
        // Return all reactive data and methods to make them available in template
        return {
            members: membersRef,  // Expose as 'members' for template usage
            newMember,
            addMember,
            removeMember
        };
    }
};

// I can call Vue here because the template.html is already using the VUE CDN:
Vue.createApp(handlingForms).mount('#app');  // This '#app' is the main tag id in template.html