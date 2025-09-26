<!--

    COMPOSITION API: METHODS OPTION
    
    Unlike in Options API approach, here there isn't a dedicated "methods option." Instead, you
    simply declare regular JavaScript functions within the setup() function or <script setup>.
    That said, methods are functions defined inside <scrip>. They are used to perform specific tasks,
    such as responding to user interactions (e.g., clicks), processing data, or executing any custom
    JavaScript logic. Methods can be called directly in your Vue templates or elsewhere in your
    component.

    Methods VS Computed:
        /JavaScript/Web-development/frontend/Vue/vue-knowledge/4-computed-vs-methods.txt

-->

<!--
    RECOMMENDED APPROACH!
    Composition-API (being coded with sintactic sugar, SMARTHER 'coz it's much more direct
    and flexible):
-->
<script setup>
const handleClick = () => {
  console.log("Button clicked");
};
</script>

<!--
    Composition-API (using Options-API structure, but with setup() that replace all options
    sections (data, computed, methods, lifecycle hooks, etc), making to be need the ref() usage:
-->
<script>
export default {
  setup() {
    function handleClick() {
      console.log("Button clicked");
    }

    return {
      handleClick,
    };
  },
};
</script>

<!--

    >> Example 2:
        /JavaScript/Web-development/frontend/Vue/vue-knowledge/using-composition-api/z-examples/adding-and-removing-things-by-form/

-->
