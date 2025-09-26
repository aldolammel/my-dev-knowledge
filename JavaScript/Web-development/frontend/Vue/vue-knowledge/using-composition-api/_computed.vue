<!--

    COMPOSITION API: COMPUTED PROPERTIES

    They are functions that return a value based on other reactive data. They're defined in the
    computed section of a Vue component and are accessed like regular data properties in
    the template.
        
    They are part of Vue's reactivity system and are available in every Vue component by default.

    Methods VS Computed:
        /JavaScript/Web-development/frontend/Vue/vue-knowledge/4-computed-vs-methods.txt

    
    E.g. in a vue component file:

-->


<!--
    RECOMMENDED APPROACH!
    Composition-API (being coded with syntactic sugar, SMARTHER 'coz it's much more direct
    and flexible):
-->
<script setup>
import { ref, computed } from 'vue';

const count = ref(0)
const doubleCount = computed(() => count.value * 2)

function increment() {
    count.value++
}
</script>


<!--
    Composition-API (using Options-API structure, but with setup() that replace all options
    sections (data, computed, methods, lifecycle hooks, etc), making to be need the ref() usage:
-->
<script>
    import { ref, computed } from 'vue'

    export default {
        setup() {
            const count = ref(0)
            const doubleCount = computed(() => count.value * 2)
            
            function increment() {
                count.value++
            }
            
            return {
                count,
                doubleCount,
                increment
            }
        }
    }
</script>


<!--
    
    >> Using Computed Properties to acess VueX store:
        /JavaScript/Web-development/frontend/Vue/3-component-libraries/vuex/computed-properties.txt

-->