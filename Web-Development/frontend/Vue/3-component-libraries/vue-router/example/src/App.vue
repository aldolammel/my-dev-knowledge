<template>
  <div id="app">
    <!-- Navigation menu -->
    <nav class="navbar">
      <div class="nav-brand">
        <RouterLink to="/">MyApp</RouterLink>
      </div>
      <ul class="nav-links">
        <li>
          <RouterLink to="/" class="nav-link">Home</RouterLink>
        </li>
        <li>
          <RouterLink to="/about" class="nav-link">About</RouterLink>
        </li>
        <li>
          <RouterLink to="/dashboard" class="nav-link">Dashboard</RouterLink>
        </li>
      </ul>
    </nav>

    <!-- Main content area where route components will be rendered -->
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>