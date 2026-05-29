

DIRECTIVE: V-BIND


    >> It's accepted for: any (with arg), obj (without arg).

    >> It's shorter caller: ':' (colon)

        >> You can apply v-bind using 'v-bind:' or just ':' before an attribute for example:

            >> Calling URL:
            
                <img :src="p.image" /> so its the same of <img src="https://somedomain.com/image.png" />
        

        >> Using v-bind in hyperlink:

            Template literals:
                <a :href="`${post.slug}`">...
                <a :href="`/user/${userId}/posts`">...

            Concatenating strings:
                <a :href="'/user/' + userId">...
            
            With conditional:
                <a :href="isExternal ? externalUrl : internalUrl">Dynamic Link</a>

                    In other words:
                        if isExternal is true:
                            use externalUrl
                        otherwise:
                            use internalUrl

            >> Don't use v-bind if you front-end project uses Vue-Router:
                
                .../Vue/3-component-libraries/vue-router/_vue-router.txt

                    Instead, you use <router-link>:
                        E.g.
                            From this:
                                <a :href="`/t/${tag.slug}`">...
                            To this:
                                <router-link :to="`/t/${tag.slug}`">...
        
        
        >> Using v-bind to deactivate a button:

            <button
              :disabled="product.quantity <= 1"
              ...
            >
                Remove
            </button>

        
        >> Including a css-class dynamically:

            <div
                class="menu-link"
                :class="{ selected : product.active }"
            >

                # Output if menu-link is selected: 
                    class="menu-link selected"

    
    
    >> HOW TO XXXXXXXXXXXXXXXXXXXXXXXXX:

        xxxxxxxxxxxxxxxxxxxxxxx