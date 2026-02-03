<script setup>
// ...
// Composition functions:
watch(
  () => props.slug,
  (newSlug) => {
    if (newSlug) {
      store.fetchPage(newSlug);
    }
  },
  { immediate: true } // immediate: true ensures it runs on component mount!
);
</script>

<!--
  REAL EXAMPLES:
    ./z-examples/receiving-data-in-child-from-page-slug/
    ./z-examples/receiving-data-in-parent-from-page-slug/
-->
