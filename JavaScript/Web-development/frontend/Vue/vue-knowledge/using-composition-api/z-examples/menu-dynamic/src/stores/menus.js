/*
  This file is responsible to cache/store all Menus data incoming from Django CMS.
  This light-weight solution runs just one menu at a time, using fetchMenu(identifier).
*/

import { defineStore } from "pinia";
import { reactive, ref } from "vue";
import axios from "axios";
import { env } from "@/utils/env";

const PATH = "/api/menus"; // It's also partially declared in /apps/pagex/consts.py

export const useMenusStore = defineStore("menus", () => {
  // State:
  const menus = reactive({}); // Cache menu by identifier
  const loading = ref(false);
  // Computed properties:
  // Reserved space...
  // Actions:
  async function fetchMenu(identifier) {
    /*This function accesses a specific menu (by 'identifier' param) from Django Pagex API.*/
    try {
      loading.value = true;
      const url = `${PATH}/${identifier}/`;
      const response = await axios.get(url);
      if (env.isDebug) {
        console.debug("FRONTEND DEBUG > Menus API > Requesting URL:", url);
        console.debug("FRONTEND DEBUG > Menus API > fetchMenu:", response.data);
      }
      menus[identifier] = response.data.links;
    } catch (error) {
      console.error("FRONTEND ERROR > Menus API > fetchMenu:", error.message);
    } finally {
      loading.value = false;
    }
  }
  return {
    // State:
    menus,
    loading,
    // Computed properties:
    // Reserved space...
    // Actions:
    fetchMenu,
  };
});
