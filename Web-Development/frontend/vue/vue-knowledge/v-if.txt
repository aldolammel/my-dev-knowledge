

DIRECTIVE: V-IF


    >> It's accepted for: any.

    >> Examples:


        >> Using no parameter/argument:
            <h1 v-if="awesome">It's awesome!</h1>


        >> Using parameter/argument:
            <button
                v-if="!isInCart(product)"  
                ...
            >
                Add to Cart
            </button>
            <small v-else>
                Added in your cart.
            </small>


        >> Avoiding v-if and v-else:
            <span>
                {{ book.isReady ? "I'm ready" : "NOT READY YET" }}
            </span>


        >> Important: it's NOT recommended to use v-if and v-for on the same element due to
            implicit precedence.


        