// FILE: /my_django_project/frontend/src/stores/pages.js

import { defineStore } from "pinia";
import axios from "axios";

export const usePagesStore = defineStore("pages", {
  state: () => ({
    pages: {},
    categories: {},
    loading: false,
    error: null,
  }),

  actions: {
    async fetchPage(id) {
      try {
        this.loading = true;
        const response = await axios.get(`/api/pages/${id}/`);
        this.pages[id] = response.data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },

    async fetchCategory(id) {
      try {
        this.loading = true;
        const response = await axios.get(`/api/categories/${id}/`);
        this.categories[id] = response.data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
  },
});
