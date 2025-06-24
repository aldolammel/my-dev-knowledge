<!--

    OPTIONS API: METHODS OPTION
    
    In Vue.js when used with 'Options API' approach, methods are functions defined inside a Vue
    instance's methods option. They are used to perform specific tasks, such as responding to
    user interactions (e.g., clicks), processing data, or executing any custom JavaScript logic.
    Methods can be called directly in your Vue templates or elsewhere in your component.

    Methods VS Computed:
        /33-Web-development/frontend/vue/vue-knowledge/4-computed-vs-methods.txt
        

    E.g. in a vue component file:
    
-->

<template>
    <div>
        {{ total() }}
    </div>
</template>

<script>
const MyProjectThing = {
    data() {
        return {
            //...
        }
    },
    // METHODS/FUNCTIONS:
    methods: {
        // Example:
        total: function() {
            var total = 0;
            // For looping:
            this.products.forEach(function(product){
                // Only those products actived:
                if (product.isActive) {
                    total += product.price * product.quantity;
                }
            });
            // Returning result rounded yet:
            return total.toFixed(2);
        }
    }
};
</script>

<style>
</style>

<!--

    >> Computed vs Methods:
        /33-Web-development/frontend/vue/vue-knowledge/computed-vs-methods.txt

    >> Example 2:
        /33-Web-development/frontend/vue/vue-knowledge/examples-using-options-api/products-selection-and-increase-amounts/

-->
