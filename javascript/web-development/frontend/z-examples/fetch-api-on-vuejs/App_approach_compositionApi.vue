<!-- Using the 'Options API' logic to build-up this app, instead of the 'Composition API' -->
<script>
  // It prevents the external API to inject malicious scripts in this app:
  import DOMPurify from 'dompurify';

  export default {
    // Component state/data
    data() {
      return {
        quizData: null,
        isLoading: false,

      }
    },

    // Computed properties
    // Space reserved...

    // Lifecycle hooks
    created() {
      this.fetchQuizData();
    },

    // Methods/functions
    methods: {
      sanitizeHTML(html) {
        // This function prevents the API to inject malicious script in this app:
        return DOMPurify.sanitize(html);
      },

      async fetchQuizData() {
        this.isLoading = true;
        
        try {
          const response = await fetch('https://opentdb.com/api.php?amount=1&category=18&type=boolean');
          
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          
          const data = await response.json();

          // Decode HTML entities in the question
          const decoder = document.createElement('div');
          decoder.innerHTML = data.results[0].question;
          data.results[0].question = decoder.textContent;
          
          this.quizData = data.results[0];
          console.log('Quiz data fetched:', this.quizData);
        } catch (error) {
          console.error('Error fetching quiz data:', error);
        } finally {
          this.isLoading = false;
        }
      }
    }
  }
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
