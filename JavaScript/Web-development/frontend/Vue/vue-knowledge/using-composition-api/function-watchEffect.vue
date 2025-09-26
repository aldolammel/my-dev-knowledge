<script setup>
// ...
// Composition functions:
watchEffect(() => {
  if (props.slug) {
    // Only fetch if slug exists
    store.fetchPage(props.slug);
  }
});
</script>
