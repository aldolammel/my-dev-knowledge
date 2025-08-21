
/*
    HOW TO CREATE DATA WITH VUEX IN VUE.JS
    This file is used by example in:
        /Web-Development/frontend/Vue/3-component-libraries/vuex/1-overview-how-to-create-data.txt
*/

export default createStore({
    //...
    actions: {
        actLoadProducts({ commit }) {  // 'actLoadProducts' is the action!
            // This function calls an API that returns fake products to be displayed on the website.
            fetch('https://fakestoreapi.com/products')
                .then(response => response.json())
                .then(data => {
                    commit('mutLoadProducts', data)  // 'mutLoadProducts' is the mutation!
                })
        },
        //...
    },
    //...
})