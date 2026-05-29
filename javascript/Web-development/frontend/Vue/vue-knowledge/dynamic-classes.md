

DYNAMIC CSS CLASSES IN AN HTML FILE:

    If you want to make a link on a menu to change when that link is clicked/active, you can use
    the 'v-bind directive' to call another style-class:

        A) Using Vue-Router as a facilitator;
        B) Or vanilla method checking boolean value (demands store/db data);

        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        
        A) Using Vue-Router as a facilitator:

            xxxx



        B) Vanilla method checking boolean value (demands store/db data):
            
            Static html of a selected div:
                
                <div class="selected">

            Now, using dynamic class with v-bind:
                
                <div 
                    <!-- class attribute empty or not -->
                    class=""

                    <!-- If the 'active' is true, the div-class will get the 'selected' class too -->
                    :class="{ selected : product.active }"

                    <!-- If the div's clicked, the 'active' value is changed to its opposite value -->
                    @click="product.active = !product.active"
                >


            >> Another example: using a custom function and argument on the conditional:

                    <div 
                        v-for="(product, idx) in products"
                        :key="idx"
                        class="product"
                        :class="{ inCart : isInCart(product) }"
                    >

                    PS: this 'inCart' is the css-style-class to be added if the conditional returns true.



