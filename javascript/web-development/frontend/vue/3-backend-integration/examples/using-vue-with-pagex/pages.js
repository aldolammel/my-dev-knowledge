/*
  THIS FILE: /project_django/frontend/src/stores/pagex.js

  It's responsible to cache/store all Pagex data incoming from Django CMS.
  The data is used to populate the Vue pages (.vue).
*/

import { defineStore } from "pinia";
import { reactive, ref } from "vue";
import axios from "axios";
import { env } from "@/utils/env";

const PATH = "/api/pages"; // It's also partially declared in /apps/pagex/consts.py

export const usePagesStore = defineStore("pages", () => {
  // State:
  const pages = reactive({}); // Cache menu by slug
  const loading = ref(false);
  // Computed properties:
  // Reserved space...
  // Actions:
  async function fetchPage(slug) {
    /*This function accesses a specific page slug from Django Pagex API:
    FYI: Each Vue component page calls this to populate dynamically its template.*/
    try {
      loading.value = true;
      const url = `${PATH}/${slug}/`;
      const response = await axios.get(url);
      if (response.data) {
        pages[slug] = response.data; // store by slug
      }
      if (env.isDebug) {
        console.debug("FRONTEND DEBUG > Pages API > Requesting URL:", url);
        console.debug("FRONTEND DEBUG > Pages API > fetchPage:", response.data);
      }
    } catch (error) {
      console.error("FRONTEND ERROR > Pages API > fetchPage:", error.message);
    } finally {
      loading.value = false;
    }
  }
  async function fetchAllPages() {
    /*This function accesses the Django Pagex API and returns all page slugs available:
    FYI: Vue Router calls this to build its routes dynamically.*/
    try {
      const response = await axios.get(`${PATH}/`);
      if (env.isDebug) {
        console.debug("FRONTEND DEBUG > Pages API > fetchAllPages:", response.data);
      }
      response.data.forEach((page) => {
        if (page && page.slug) {
          pages[page.slug] = page;
        }
      });
      return response.data;
    } catch (error) {
      console.error("FRONTEND ERROR > fetchAllPages:", error.message);
      return [];
    }
  }
  return {
    // State:
    pages,
    loading,
    // Computed properties:
    // Reserved space...
    // Actions:
    fetchPage,
    fetchAllPages,
  };
});
