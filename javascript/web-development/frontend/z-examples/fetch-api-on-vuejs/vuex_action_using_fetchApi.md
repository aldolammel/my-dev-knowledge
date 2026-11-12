HOW TO CREATE DATA WITH VUEX IN VUE.JS

---

This is used as example in: [/javascript/web-development/frontend/vue/3-component-libraries/vuex/1-overview-how-to-create-data](/javascript/web-development/frontend/vue/3-component-libraries/vuex/1-overview-how-to-create-data.md)

```js
export default createStore({
  //...
  actions: {
    actLoadProducts({ commit }) {
      // 'actLoadProducts' is the action!
      // This function calls an API that returns fake products to be displayed on the website.
      fetch("https://fakestoreapi.com/products")
        .then((response) => response.json())
        .then((data) => {
          commit("mutLoadProducts", data); // 'mutLoadProducts' is the mutation!
        });
    },
    //...
  },
  //...
});

```

