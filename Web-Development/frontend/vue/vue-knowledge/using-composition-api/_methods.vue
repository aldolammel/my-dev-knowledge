<!--

    COMPOSITION API: METHODS OPTION
    
    Unlike in Options API approach, here there isn't a dedicated "methods option." Instead, you
    simply declare regular JavaScript functions within the setup() function or <script setup>.
    That said, methods are functions defined inside <scrip>. They are used to perform specific tasks,
    such as responding to user interactions (e.g., clicks), processing data, or executing any custom
    JavaScript logic. Methods can be called directly in your Vue templates or elsewhere in your
    component.

    Methods VS Computed:
        /33-Web-development/frontend/vue/vue-knowledge/4-computed-vs-methods.txt

-->


<script setup>
const handleClick = () => {
    console.log('Button clicked')
}
</script>


<!--

    >> Computed vs Methods:
        /33-Web-development/frontend/vue/vue-knowledge/computed-vs-methods.txt

-->
