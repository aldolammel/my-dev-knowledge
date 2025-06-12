<template>
  <div class="cart">
    <div class="items">
      <template v-if="cart.length">
        <!-- EACH CART PRODUCT - START -->
        <div
          v-for="(prod, idx) in cart"
          :key="idx"
          class="item"
        >
          <div 
            class="remove"
            @click="btCartDelProd(prod.id)"
          >
            Remove item
          </div>
          <div class="photo">
            <img
              :src="prod.image"
              :alt="prod.title"
            >
          </div>
          <div class="description">
            {{ prod.title }}
          </div>
          <div class="price">
            <span class="quantity-area">
              <button
                :disabled="prod.quantity <= 1"
                type="button"
                @click="prod.quantity--"
              >
                -
              </button>
              <span class="quantity">{{ prod.quantity }}</span>
              <button
                type="button"
                @click="prod.quantity++"
              >
                +
              </button>
            </span>
            <span class="amount">US$ {{ (prod.price * prod.quantity).toFixed(2) }}</span>
          </div>
        </div>
        <!-- EACH CART PRODUCT - END -->
        <div class="grand-total">
          Total: US$ {{ calcCartTotal() }}
        </div>
      </template>
      <template v-else>
        <h4>No products in your shopping cart yet.</h4>
      </template>
    </div>
  </div>
</template>
  
<script>
// Things to import:
import { mapState } from 'vuex'

export default {
  name: 'Cart',

  // Computed properties:
  // /33-Web-development/frontend/vuejs/3-component-libraries/vuex/computed-properties.txt
  // /33-Web-development/frontend/vuejs/3-component-libraries/vuex/vuex-helpers.txt
  computed: mapState([  // Using the a 'Vuex Helper' to generate automatically the getter fncs!
    'cart'  // It's a state property (data)!
  ]),

  // Lifecycle hooks:
  // Reserved space...

  // Methods/functions:
  methods: {
    btCartDelProd(prodID) {
      // This function is called if a user click over the 'Remove item' link.
      const isConfirmed = confirm("Remove the product from your cart?")
      if (isConfirmed) {
        this.$store.dispatch('actCartDelProd', prodID);
      }
    },
    calcCartTotal() {
      // This function calculate each product (item) price and multiplicate it based on its quantity,
      // returning the total of the shopping cart.
      var total = 0;
      this.cart.forEach(item => {
        total += item.price * item.quantity;
      })
      return total.toFixed(2);
    }
  },
  
}
</script>

<style lang="scss">

.cart {
  padding: 60px 0;  
  .items {
    max-width: 800px;
    margin: auto;
    .item {
      display: flex;
      justify-content: space-between;
      padding: 40px 0;
      border-bottom: 1px solid lightgrey;
      position: relative;

      .remove {
        position: absolute;
        top: 8px;
        right: 0;
        font-size: 11px;
        text-decoration: underline;
        cursor: pointer;
      }

      .quantity-area {
        margin: 8px auto;
        height: 14px;

        button {
          width: 16px;
          height: 16px;
          display: inline-flex;
          justify-content: center;
          align-items: center;
          cursor: pointer;
        }

        .quantity {

            margin: 0 4px;
        }
      }

      .photo {
        img {
          max-width: 80px;
        }
      }

      .description {
        padding-left: 30px;
        box-sizing: border-box;
        max-width: 50%;

      }

      .price {
        .amount {
          font-size: 16px;
          margin-left: 8px;
          vertical-align: middle;

        }
      }
    }
      .grand-total {
          font-size: 24px;
          font-weight: bold;
          text-align: right;
          margin-top: 8px;
      }

  }

}

</style>
  