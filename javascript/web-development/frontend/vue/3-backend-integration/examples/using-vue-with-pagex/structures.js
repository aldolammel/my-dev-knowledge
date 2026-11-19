/*
  THIS FILE: /project_django/frontend/src/stores/structures.js

  It's responsible to cache/store all Pagex structure data incoming from Django CMS.
  The data is used to populate the Vue pages (.vue).
*/

import { defineStore } from "pinia";
import { reactive, ref } from "vue";
import axios from "axios";
import { env } from "@/utils/env";

const PATH = "/api/structures"; // It's also partially declared in /apps/pagex/consts.py

export const useStructuresStore = defineStore("structures", () => {
  // State:
  const structures = reactive({}); // Cache structures by identifier
  const loading = ref(false);
  // Computed properties:
  // Reserved space...
  // Actions:
  async function fetchStructure(identifier) {
    /*This function accesses a specific page slug from Django Pagex API:
    FYI: Each Vue component page calls this to populate dynamically its template.*/
    try {
      loading.value = true;
      const url = `${PATH}/${identifier}/`;
      const response = await axios.get(url);
      if (response.data) {
        structures[identifier] = response.data; // store by identifier
      }
      if (env.isDebug) {
        console.debug("FRONTEND DEBUG > Structures API > Requesting URL:", url);
        console.debug("FRONTEND DEBUG > Structures API > fetchPage:", response.data);
      }
    } catch (error) {
      console.error("FRONTEND ERROR > Structures API > fetchStructure:", error.message);
    } finally {
      loading.value = false;
    }
  }
  async function fetchAllStructures() {
    /*This function accesses the Django Pagex API and returns all structure identifiers available:
    FYI: Vue Router calls this to build its routes dynamically.*/
    try {
      const response = await axios.get(`${PATH}/`);
      if (env.isDebug) {
        console.debug("FRONTEND DEBUG > Structures API > fetchAllStructures:", response.data);
      }
      response.data.forEach((struct) => {
        if (struct && struct.identifier) {
          structures[struct.identifier] = struct;
        }
      });
      return response.data;
    } catch (error) {
      console.error("FRONTEND ERROR > fetchAllStructures:", error.message);
      return [];
    }
  }
  return {
    // State:
    structures,
    loading,
    // Computed properties:
    // Reserved space...
    // Actions:
    fetchStructure,
    fetchAllStructures,
  };
});
