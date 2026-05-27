<script setup>
// THIS FILE: /project_django/frontend/src/components/common/HeroBig.vue

// Layout components:
// Reserved Space...
// Common components
// Reserved Space...

// Receiving Props from Parent:
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
  btText: {
    type: String,
    required: false,
    default: "Saiba mais",
  },
  btLink: {
    type: String,
    required: false,
    default: null,
  },
  img: {
    type: String,
    required: false,
    default: null,
  },
});
</script>

<template>
  <!-- Start Hero Section -->
  <div class="hero">
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-lg-5">
          <div class="intro-excerpt">
            <h1>
              {{ props.title }}
            </h1>
            <p class="mb-4">
              {{ props.subtitle }}
            </p>
            <p>
              <a :href="props.btLink" class="btn btn-secondary me-2">{{ props.btText }}</a>
              <a href="#" class="btn btn-white-outline">Xxxx</a>
            </p>
          </div>
        </div>
        <div class="col-lg-7">
          <div class="hero-img-wrap">
            <img :src="props.img" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Hero Section -->
</template>

<style lang="scss" scoped></style>
