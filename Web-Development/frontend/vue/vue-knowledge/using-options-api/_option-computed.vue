<!--
    OPTIONS API: COMPUTED PROPERTIES

    They are functions that return a value based on other reactive data. They're defined in the
    computed section of a Vue component and are accessed like regular data properties in
    the template.
    
    They are part of Vue's reactivity system and are available in every Vue component by default.

    Methods VS Computed:
        /Web-Development/frontend/vue/vue-knowledge/4-computed-vs-methods.txt


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
    }
}
</script>

<!--
           
    >> Using Computed Properties to acess VueX store:
        /Web-Development/frontend/vue/3-component-libraries/vuex/computed-properties.txt

-->