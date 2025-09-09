<template>
  <div class="home">
    <div class="products">
      <div 
        v-for="(prod, idx) in products"
        :key="idx"
        class="product"
        :class="{ inBag : isInCart(prod) }"
      >
        <div
          class="product-image"
          :style="{ backgroundImage: `url(${prod.image})` }"
        />
        <h4>{{ prod.title }}</h4>
        <p class="price">
          US$ {{ prod.price.toFixed(2) }}
        </p>
        <button
          v-if="!isInCart(prod)"  
          type="button"
          @click="btCartAddProd(prod)"
        >
          Add to Cart
        </button>
        <button 
          v-else
          class="remove"
          @click="btCartDelProd(prod.id)"
        >
          Remove from cart
        </button>
      </div>
    </div> 
  </div>
</template>
  
<script>
  // Things to import:
  import { mapState } from 'vuex'

  export default {
    name: 'Home',
    // Component state/data
    data() {
      return {
        // state proprieties:
        // Reserved space...
      }
    },
    // Computed properties:
    // /JavaScript/Web-development/frontend/Vue/3-component-libraries/vuex/computed-properties.txt
    // /JavaScript/Web-development/frontend/Vue/3-component-libraries/vuex/vuex-helpers.txt
    computed: mapState([  // Using the a 'Vuex Helper' to generate automatically the getter fncs!
      'products',  // It's a state property (data)!
      'cart'  // It's a state property (data)!
    ]),
    
    // Lifecycle hooks:
    // Reserved space...
    
    // STEP 2/4:
    // Addressing/Dispatching actions responsable to request data updates:
    // Methods/functions
    methods: {
      btCartAddProd(prod) {
        // This function is called if a user click over the 'Add to Cart' button.
        prod.quantity = 1;
        this.$store.dispatch('actCartAddProd', prod);  // 'actCartAddProd' is the action to call!
      },
      isInCart(prod) {
        // This function checks whether the product is in shopping cart.
        // Returns bool: If true, the product is in cart.
        return this.cart.find(item => item.id === prod.id);
      },
      btCartDelProd(prodID) {
        // This function is called if a user click over the 'Remove from Cart' button.
        const isConfirmed = confirm("Remove the product from your cart?")
        if (isConfirmed) {
          this.$store.dispatch('actCartDelProd', prodID);
        }
      }
    }
  }
</script>

<style lang="scss">
  .home {

    .products {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;


      .product {
        flex: 0 0 30%;
        box-sizing: border-box;  
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        padding: 16px;
        margin: 8px;
        height: 360px;

        @media only screen and (max-width: 769px) {
          flex: 0 0 40%;
        }

        @media only screen and (max-width: 640px) {
          flex: 0 0 90%;
        }

        &.inBag {
          border: 1px solid #007bff;
        }
        
        .product-image {
          margin: 20px auto;
          width: 160px;
          height: 140px;
          background-size: contain;
          background-position: center;
          background-repeat: no-repeat;
        }
        h4 {
          margin: 22px auto;
          font-size: 12px;
          max-width: 60%;
          font-weight: normal;
        }

        p.price {
          font-size: 20px;
          font-weight: bold;
        }

        button {
          color: #fff;
          background-color: #007bff;
          border: 1px solid #007bff;
          border-radius: 100px;
          font-weight: 400;
          text-align: center;
          padding: 8px 16px;
          cursor: pointer;

          &:hover {
            opacity: 0.8;
          }

          &.remove {
            background-color: transparent;
            border: none;
            color: black;
            text-decoration: underline;
          }
        }
      }
    }
  }
</style>
