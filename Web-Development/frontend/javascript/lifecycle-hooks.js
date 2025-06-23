
/* 
    
    LIFECYCLE HOOKS
    It is a group of phases that the javascript has when some action if called.

    The cycle is:
    /33-Web-development/frontend/javascript/vuejs_lifecycle_hooks.png

*/

// Usage on Vue.Js, for example:
const AppName = {
    data() {
        //...
    },
    methods: {
        //...
    },
    
    // Lifecycle-Hook: phase before the object creation:
    beforeCreate() {
        // things to happen in this phase!
        console.log('Here is the beforeCreate() Lifecycle hook.');
    },

    // Lifecycle-Hook: phase right after the object creation:
    created() {
        // things to happen in this phase!
        console.log('Here is the created() Lifecycle hook.');
    },
    
    // Lifecycle-Hook: phase before the object's update (if appliable):
    beforeUpdate() {
        // things to happen in this phase!
        console.log('Here is the beforeUpdate() Lifecycle hook.');
    },

    // Lifecycle-Hook: phase right after the object's update (if appliable):
    updated() {
        // things to happen in this phase!
        console.log('Here is the updated() Lifecycle hook.')
    }
};