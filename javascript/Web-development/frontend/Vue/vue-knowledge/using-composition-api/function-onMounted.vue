<script setup>
// ...
// Composition functions:
onMounted(() => {
  if (props.slug) {
    // Only fetch if slug exists
    store.fetchPage(props.slug);
  }
});
</script>
