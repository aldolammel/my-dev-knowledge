<script setup>
// ...
</script>

<template>
  <!-- Navigation menu - START -->
  <nav>
    <div>
      <RouterLink to="/">
        LOGO-BRAND
      </RouterLink>
    </div>

    <ul>
      <li>
        <RouterLink to="/">
          HOME
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/about">
          ABOUT
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/contact">
          CONTACT
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/dashboard">
          DASHBOARD
        </RouterLink>
      </li>
    </ul>
  </nav>
  <!-- Navigation menu - END -->
</template>
