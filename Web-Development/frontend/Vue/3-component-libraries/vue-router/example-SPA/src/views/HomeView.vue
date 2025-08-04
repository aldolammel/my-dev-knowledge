<!-- 
  The file's content is irrelevant. It's here just to contextualize the Router example.

  BY THE WAY: This view (page) will be rendered where the <RouterView /> tag is called (App.vue).
-->

<script setup>
	import SiteHeader from '../components/SiteHeader.vue'
	import SectionProfiles from '../components/SectionProfiles.vue'
	import SectionAbout from '../components/SectionAbout.vue'
	import Section3 from '../components/Section3.vue'
	import Section4 from '../components/Section4.vue'
	import Section5 from '../components/Section5.vue'
	import SectionBlog from '../components/SectionBlog.vue'
</script>

<template>
  <SiteHeader />
  <SectionProfiles />
  <SectionAbout />
  <Section3 />
  <Section4 />
  <Section5 />
  <SectionBlog />
</template>

<style lang="scss" scoped>
</style>
