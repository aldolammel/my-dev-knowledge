export default createStore({
    //...
    actions: {
        loadProducts({ commit }) {
            fetch('https://fakestoreapi.com/products')
                .then(response => response.json())
                .then(data => {
                    commit('setProducts', data)  // setProducts = mutation that the action will call!
                })
        }
    },
    //...
})