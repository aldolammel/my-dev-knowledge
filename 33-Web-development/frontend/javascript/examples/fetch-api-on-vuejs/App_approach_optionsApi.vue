<!-- Using the 'Composition API' logic to build-up this app, instead of the 'Options API' -->
<script setup>
  // Example of using Fetch API in a Vue.js component
  import { ref, onMounted } from 'vue';
  // Keep DOMPurify in your project. It's a small dependency but provides crucial security protection when rendering HTML content from external sources:
  // $ npm install dompurify
  import DOMPurify from 'dompurify';

  // Reference to store the quiz data
  const quizData = ref(null);
  const isLoading = ref(false);

  const sanitizeHTML = (html) => {
    return DOMPurify.sanitize(html);
  };
  // Function to fetch the quiz data
  const fetchQuizData = async () => {
    isLoading.value = true;
    
    try {
      // Make the fetch request to the API
      const response = await fetch('https://opentdb.com/api.php?amount=1&category=18&type=boolean');
      
      // Check if the response is ok (status in the range 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      // Parse the JSON from the response
      const data = await response.json();

      // Decode HTML entities in the question
      const decoder = document.createElement('div');
      decoder.innerHTML = data.results[0].question;
      data.results[0].question = decoder.textContent;
      
      // Store the data in our ref
      quizData.value = data.results[0];
      console.log('Quiz data fetched:', quizData.value);
    } catch (error) {
      // Handle any errors
      console.error('Error fetching quiz data:', error);
    } finally {
      // Set loading to false when done
      isLoading.value = false;
    }
  };
  // Fetch data when the component is mounted
  onMounted(() => {
    fetchQuizData();
  });
</script>

<template>
  <div v-if="isLoading">
    <h1>Loading...</h1>
  </div>
  <div v-else-if="quizData">
    <h1 v-html="sanitizeHTML(quizData.question)" />
    <small>
      Difficulty: {{ quizData.difficulty }}
    </small>    
    <input
      type="radio"
      name="options"
      value="True"
    >
    <label>True</label><br>
        
    <input
      type="radio"
      name="options"
      value="False"
    >
    <label>False</label><br>
        
    <button
      class="send"
      type="button"
    >
      Check answer
    </button>
  </div>
  <div v-else>
    <h1>No quiz data available!</h1>
    <button 
      class="send"
      type="button"  
      @click="fetchQuizData"
    >
      Reload quiz
    </button>
  </div>
</template>

<style lang="scss" scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin: 60px auto;
    max-width: 960px;

    small {
      margin:-30px 0 30px 0;
      color:#666;
      display:block;
    }

    input[type='radio'] {
      margin: 12px 4px;
    }

    button.send {
      margin-top: 12px;
      height: 40px;
      min-width: 120px;
      padding: 0 16px;
      color: #fff;
      background-color: #1867c0;
      border: 1px solid #1867c0;
      cursor: pointer;
    }
  }
</style>
