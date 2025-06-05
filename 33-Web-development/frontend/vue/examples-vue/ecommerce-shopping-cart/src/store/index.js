import { createStore } from 'vuex'

export default createStore({

  // STEP 1/4:
  // Declaring all types of front-end data (state property) should be stored!
  state: {  // "state" means data!
    products: [],
    cart: [],
  },

  // STEP 2/4:
  // In a .vue file (in this case, 'Home.vue') where data is needed, dispatch what action will be used!

  // STEP 3/4:
  actions: {
    // Creating an action that will execute a mutation to update a specific state/data when called!
    // Be aware: it's NOT possible to load/add/update a state without mutation.

    actLoadProducts({ commit }) {  // 'actLoadProducts' is the action!
      // This function calls an API that returns fake products to be displayed on the website.
      fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(data => {
          commit('mutLoadProducts', data)  // 'mutLoadProducts' is the mutation!
        })
    },
    actLoadCart({ commit }) {
      // This function calls the entire cart to avoid the issue if the user to open the cart in
      // a new tab/window (losing the cart data).
      // About JS method localStorage: /33-Web-development/frontend/javascript/localStorage.js
      if (localStorage.getItem("cart")) {
        commit('mutLoadCart', JSON.parse(localStorage.getItem("cart")));  // JSON.parse exchanges the data in an obj JS.
      }
    },
    actCartAddProd({ commit }, prod) {
      // This function calls the mutation responsable to add the product to the shopping cart.
      commit('mutAddProd', prod);
    },
    actCartDelProd({ commit }, prodID) {
      // This function calls the mutation responsable to remove the product to the shopping cart.
      commit('mutDelProd', prodID);
    }
  },

  // STEP 4/4:
  mutations: {
    // Finally, it 'sends' all products to Vue components that request its action!
    mutLoadProducts(state, products) {
      state.products = products;
    },
    mutLoadCart(state, cart) {
      state.cart = cart;
    },
    // 'mutAddProd' is the mutation, and 'prod' arg is the data itself defined from the action step:
    mutAddProd(state, prod) {
      state.cart.push(prod);
      localStorage.setItem('cart', JSON.stringify(state.cart))  // JSON.stringify exchanges the obj to string.
    },
    mutDelProd(state, prodID) {
      // 'filter' method keeps those array elements that the conditional's return is true:
      var updatedCart = state.cart.filter(item => prodID !== item.id);
      state.cart = updatedCart;
      localStorage.setItem('cart', JSON.stringify(state.cart))  // JSON.stringify exchanges the obj to string.
    }
  },

  modules: {
  }
})
