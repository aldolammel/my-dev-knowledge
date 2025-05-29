
/*
    HOW TO CREATE DATA WITH VUEX IN VUE.JS
    This file is used by example in:
        /33-Web-development/frontend/vuejs/3-component-libraries/vuex/1-overview-how-to-create-data.txt
*/

export default createStore({
    //...
    actions: {
        loadProducts({ commit }) {
            // This function read an API (json) and set the response to a mutation (updateProducts).
            fetch('https://fakestoreapi.com/products')
                .then(response => response.json())
                .then(data => {
                    commit('updateProducts', data)  // 'updateProducts' is the mutation to call, and 'data' is the products to change!
                })
        }
    },
    //...
})