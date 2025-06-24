

CALLING AN IMAGE URL DYNAMICALLY IN VUE:

        <img
            :src="https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg"
        >

    OR if in a "products" for-loop where each element has a 'image' (url) attribute:

        <img
            :src="product.image"
        >
    
    
    OR if the URL is inside a CSS-style:
    
        <div
            class="..."
            :style="{ backgroundImage: `url(${product.image})` }"
        />

    OR

        <div
            class="..."
            :style="{ backgroundImage: 'url(' + product.image + ')' }"
        />


