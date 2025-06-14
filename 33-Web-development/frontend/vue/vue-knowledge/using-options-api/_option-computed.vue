<!--
    OPTIONS API: COMPUTED PROPERTIES

    >> They are functions that return a value based on other reactive data. They're defined in the
    computed section of a Vue component and are accessed like regular data properties in
    the template.
    
    >> They are part of Vue's reactivity system and are available in every Vue component by default.

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
    
    >> Computed vs Methods:
        /33-Web-development/frontend/vue/vue-knowledge/computed-vs-methods.txt
        
    >> Using Computed Properties to acess VueX store:
        /33-Web-development/frontend/vue/3-component-libraries/vuex/computed-properties.txt

-->