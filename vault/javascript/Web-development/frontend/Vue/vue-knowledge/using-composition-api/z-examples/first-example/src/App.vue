<script setup>
import { ref, reactive } from 'vue';
import Progress from './components/Progress.vue'

// Convention said the Ref() always' used for primitive values (strings, numbers etc):
let count = ref(0);

// Convention said the Reactive() always used for objects:
let courses = reactive([
  {
    title: "JavaScript",
    isDone: true
  },
  {
    title: "React",
    isDone: false
  },
  {
    title: "Vue.js",
    isDone: true
  }
]);

let newCourse = {
  isDone: false
};  // empty obj.


function addCourse() {
  // Adding what was typed through the input to the course list:
  courses.push(newCourse);
  // Cleaning up the input:
  newCourse = {
    isDone: false
  };
};

function counter() {
  // Increase the amount:
  count.value++  // This '.value' is needed coz 'count' is primitive, so the convention demands ref().
                 // If 'count' were an object, it'd use reactive() and then it could be using count++.
}
</script>

<template>
  <div>
    <h1>Courses List</h1>
    <ul>
      <li 
        v-for="(course, idx) in courses"
        :key="idx"
      >
        {{ course.title }}
      </li>
    </ul>
    <Progress :courses="courses" />
    <input
      v-model="newCourse.title"
      type="text"
    >
    <button
      type="text"
      @click="addCourse"
    >
      Add course
    </button>
  </div>
  <div>
    <p>It's just a counter:</p>
    {{ count }}
    <button
      type="button"
      @click="counter"
    >
      Click me!
    </button>
  </div>
</template>

<style lang="scss">
:root {
  font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

.card {
  padding: 2em;
}

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}
</style>