// Simulating a database or Json from an external service:
var products = [
    {
        "photo": "img/big-mac.png",
        "name": "Big Mac",
        "price": 5.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/mc-chicken.png",
        "name": "Mc Chicken",
        "price": 4.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/double-cb.png",
        "name": "Double Cheese Burger",
        "price": 2.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/fries.png",
        "name": "Batata frita",
        "price": 2.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/nuggets.png",
        "name": "Mc Nuggets",
        "price": 3.49,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/salad.png",
        "name": "Salada",
        "price": 2.79,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/cola.png",
        "name": "Coca Cola",
        "price": 1.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/lipton.png",
        "name": "Ice Tea",
        "price": 1.99,
        "isActive": false,
        "quantity": 1
    },
    {
        "photo": "img/water.png",
        "name": "Água",
        "price": 1.49,
        "isActive": false,
        "quantity": 1
    }
];
 
// Constant:
const SelfServiceMachine = {
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
        total() {
            // Declarations:
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

// I can call Vue here because the template.html is already using the VUE CDN:
Vue.createApp(SelfServiceMachine).mount('#app');  // This '#app' is the main tag id in template.html