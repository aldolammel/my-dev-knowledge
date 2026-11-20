<script setup lang="ts">
import { useHead } from "@unhead/vue";
// Components:
import NewsletterFormCommon from "@/components/common/NewsletterFormCommon.vue";

// Custom HTML <head>:
useHead({
  title: "Home",
  meta: [
    {
      name: "description",
      content: "Welcome to our website",
    },
  ],
});
</script>

<template>
  <h1>HOME PUBLIC</h1>
  <NewsletterFormCommon />
</template>

<style lang="scss" scoped></style>
