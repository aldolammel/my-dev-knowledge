<!--
  PROP DRILLING ISSUE EXAMPLE
  Multi-level Theme Configuration Data flow example:
  
  App.vue
    └─> DashboardLayout.vue
        └─> SidebarContainer.vue
            └─> NavigationMenu.vue
                └─> MenuItem.vue
                    └─> MenuIcon.vue
                    └─> MenuLabel.vue
                        └─> Badge.vue
-->

<!-- App.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
import { reactive } from "vue";
import DashboardLayout from "@/components/DashboardLayout.vue";

const theme = reactive({
  primaryColor: "#3490dc",
  spacing: "compact",
  fontSize: "medium",
});
</script>

<template>
  <DashboardLayout :theme="theme" />
</template>

<!-- DashboardLayout.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
defineProps({ theme: Object });
</script>

<template>
  <div class="dashboard">
    <SidebarContainer :theme="theme" />
  </div>
</template>

<!-- SidebarContainer.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
defineProps({ theme: Object });
</script>

<template>
  <aside>
    <NavigationMenu :theme="theme" />
  </aside>
</template>

<!-- NavigationMenu.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
defineProps({ theme: Object });
</script>

<template>
  <nav>
    <MenuItem v-for="item in menuItems" :key="item.id" :item="item" />
  </nav>
</template>

<!-- MenuItem.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --->
<script setup>
defineProps({
  item: Object,
  theme: Object,
});
</script>

<template>
  <div :style="{ padding: theme.spacing === 'compact' ? '8px' : '16px' }">
    <MenuIcon :icon="item.icon" :theme="theme" />
    <MenuLabel :label="item.label" :theme="theme" />
  </div>
</template>

<!-- MenuLabel.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
defineProps({
  label: String,
  theme: Object,
});
</script>

<template>
  <span
    :style="{
      color: theme.primaryColor,
      fontSize: theme.fontSize === 'small' ? '12px' : '14px',
    }"
  >
    {{ label }}
    <Badge :theme="theme" />
  </span>
</template>

<!-- Badge.vue - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<script setup>
defineProps({ theme: Object });
</script>

<template>
  <span class="badge" :style="{ backgroundColor: theme.primaryColor }"> New </span>
</template>

<!--
  PROPS DRILLING PROBLEM:
  You're passing theme through 6+ components that don't even use it, just to reach the deepest child!

  SOLUTION: USING PROVIDE/INJECT:
    /JavaScript/Web-development/frontend/Vue/vue-knowledge/using-composition-api/z-examples/provide-inject-example-basic/example.vue
-->
