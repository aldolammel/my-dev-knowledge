<!--
  VUE: USING PROVIDE/INJECT TO AVOID PROPS DRILLING
  Multi-level Theme Configuration Data flow example:
  
  App.vue
    └─> DashboardLayout.vue
        └─> SidebarContainer.vue
            └─> NavigationMenu.vue
                └─> MenuItem.vue
                    └─> MenuIcon.vue
                    └─> MenuLabel.vue
                        └─> Badge.vue

  >> If you wanna see how hell is Props Drilling with the exactly same example:
    /JavaScript/Web-development/frontend/Vue/vue-knowledge/using-composition-api/z-examples/prop-drilling-example/example.vue
-->

<!-- App.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
import { reactive, provide } from "vue";
import DashboardLayout from "@/components/DashboardLayout.vue";

// Provide theme at the top level
const theme = reactive({
  primaryColor: "#3490dc",
  spacing: "compact",
  fontSize: "medium",
});

provide("theme", theme);
</script>

<template>
  <DashboardLayout />
</template>

<!-- DashboardLayout.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
// No theme prop needed!
</script>

<template>
  <div class="dashboard">
    <SidebarContainer />
  </div>
</template>

<!-- SidebarContainer.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
// No theme prop needed!
</script>

<template>
  <aside>
    <NavigationMenu />
  </aside>
</template>

<!-- NavigationMenu.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
// No theme prop needed!
</script>

<template>
  <nav>
    <MenuItem v-for="item in menuItems" :key="item.id" :item="item" />
  </nav>
</template>

<!-- MenuItem.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
import { inject } from "vue";

defineProps({ item: Object });

// Inject theme only where needed
const theme = inject("theme");
</script>

<template>
  <div :style="{ padding: theme.spacing === 'compact' ? '8px' : '16px' }">
    <MenuIcon :icon="item.icon" />
    <MenuLabel :label="item.label" />
  </div>
</template>

<!-- MenuLabel.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
import { inject } from "vue";

defineProps({ label: String });

// Inject theme directly
const theme = inject("theme");
</script>

<template>
  <span
    :style="{
      color: theme.primaryColor,
      fontSize: theme.fontSize === 'small' ? '12px' : '14px',
    }"
  >
    {{ label }}
    <Badge />
  </span>
</template>

<!-- Badge.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
import { inject } from "vue";

// Inject theme directly
const theme = inject("theme");
</script>

<template>
  <span class="badge" :style="{ backgroundColor: theme.primaryColor }"> New </span>
</template>
