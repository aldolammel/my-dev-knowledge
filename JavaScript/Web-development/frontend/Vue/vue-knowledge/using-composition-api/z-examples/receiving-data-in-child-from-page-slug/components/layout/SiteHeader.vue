<script setup>
import { computed } from "vue";
import { usePagesStore } from "@/stores/pages"; // Vue Pinia

// Receiving Props from Parent:
const props = defineProps({
  page: {
    type: String,
    required: true,
  },
});

// Get page data from store using the slug prop:
const store = usePagesStore();
const pg = computed(() => store.pages[props.page] || null);
</script>

<template>
  <!-- Start Hero Section -->
  <div v-if="pg" class="hero">
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-lg-5">
          <div class="intro-excerpt">
            <h1>
              {{ pg.seo_title }}
            </h1>
            <p class="mb-4">
              {{ pg.content["9065_titulo"].v }}
            </p>
            <p>
              <a href="" class="btn btn-secondary me-2">Sabia mais</a
              ><a href="#" class="btn btn-white-outline">Contato</a>
            </p>
          </div>
        </div>
        <div class="col-lg-7">
          <div class="hero-img-wrap">
            <img src="@/assets/imgs/couch.png" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Hero Section -->
</template>

<style lang="scss" scoped></style>
