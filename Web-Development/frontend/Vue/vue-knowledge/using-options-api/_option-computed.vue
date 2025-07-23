<!--
    OPTIONS API: COMPUTED PROPERTIES

    They are functions that return a value based on other reactive data. They're defined in the
    computed section of a Vue component and are accessed like regular data properties in
    the template.
    
    They are part of Vue's reactivity system and are available in every Vue component by default.

    Methods VS Computed:
        /Web-Development/frontend/Vue/vue-knowledge/4-computed-vs-methods.txt


    E.g. in a vue component file:
-->

<script>
export default {
    data() {
        return {
            firstName: 'Aldo',
            lastName: 'Lammel'
        }
    },
    computed: {
        fullName() {
            return this.firstName + ' ' + this.lastName;
        }
    },
    methods: {
        // /Web-Development/frontend/Vue/vue-knowledge/using-options-api/_option-methods.vue
    }
}
</script>

<!--
           
    >> Using Computed Properties to acess VueX store:
        /Web-Development/frontend/Vue/3-component-libraries/vuex/computed-properties.txt

-->