// Using OptionsApi approach!
// More about: /Web-Development/frontend/vue/vue-knowledge/3-approaches-to-code.txt

// Constant:
const ConstantSomeName = {
    // Property as function:
    data() {
        // Object:
        // Returning an object (everything inside this will be accessable through the app)!
        return {
            // Property:
            products: window.products,
            // If you want to call products attributes through the templates,
            // you can use {{ products[0].price }} to take the first product price, e.g.
        }
    },
    // Methods (custom code) to use through the templates:
    methods: {
        my_function_name() {
            // Declarations:
            var total = 0;
            // For looping:
            this.products.forEach(function (product) {
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

// I could call Vue here only if my index.html (for example) is using in its header the VUE CDN:
Vue.createApp(ConstantSomeName).mount('#app');  // This '#app' is the main tag id in template.html