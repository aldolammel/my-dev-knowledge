<!-- 
  Of course this component need to be called through a page/view.
-->>

<script setup>
    import { useCounterStore } from '../stores/counter';

    const store = useCounterStore();
</script>

<template>
  <h2>Total Clicks: {{ store.totalClicks }}</h2>

  <div class="card">
    <button
      type="button"
      @click="store.increment('a')"
    >
      Option A clicked {{ store.options['a'] }} times
    </button>

    <button
      type="button"
      @click="store.delayedIncrement('b')"
    >
      Option B clicked {{ store.options['b'] }} times (asynchronous!)
    </button>

    <button
      type="button"
      @click="store.increment('c')"
    >
      Option C clicked {{ store.options['c'] }} times
    </button>
  </div>
</template>