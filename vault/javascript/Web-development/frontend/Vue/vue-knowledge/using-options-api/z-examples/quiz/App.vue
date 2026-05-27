<!-- Component logic using 'Options API' approach: -->
<script>
  // Installation: $ npm install dompurify
  // It prevents the external API to inject malicious scripts in this app:
  import DOMPurify from 'dompurify';

  export default {
    // Component state/data
    data() {
      return {
        quizData: null,
        scorePlayer: 0,
        scoreMachine: 0,
        isLoading: false,
        chosenAnswer: undefined,
        wasSubmitted: false,
        isRightAnswer: false,
        scoreLimit: 3,
      }
    },

    // Computed properties
    computed: {
      answers() {
        // This function set all possible answers in an array sorted by alphanumeric.
        // Using 'spread operator (...)' to create a shalow copy of that array:
        return [...this.quizData.incorrect_answers, this.quizData.correct_answer].toSorted()
      },
      
      hasWinner() {
        // This function checks if there is a winner.
        return this.scorePlayer === this.scoreLimit || this.scoreMachine === this.scoreLimit;
      },

      winnerMsg() {
        // This function defines the winner message.
        if (!this.hasWinner) return undefined;
        return this.scorePlayer === this.scoreLimit 
          ? "You're the winner!" 
          : "Machine wins! Sorry!";
      }
    },

    // Lifecycle hooks
    created() {
      this.fetchQuizData();
    },

    // Methods/functions
    methods: {
      sanitizeHTML(html) {
        // This function prevents the API to inject malicious script in this app.
        return DOMPurify.sanitize(html);
      },

      sleep(ms) {
        // This function is just a sleep for JS.
        // Use it as: await this.sleep(<duration in miliseconds>);
        return new Promise(resolve => setTimeout(resolve, ms));
      },

      score(isRightAnswer) {
        // This function calc the player and machine points.
        if (isRightAnswer) {
          this.scorePlayer++
        } else {
          this.scoreMachine++
        }
      },

      async submitForm() {
        // This function sends the answer chosen by the user.
        // If no answer was selected, alert the user:
        if (!this.chosenAnswer) {
          alert("Please, select an answer!");
        } else {
          // Form sent:
          this.wasSubmitted = true;
          // Check whether answer is right:
          if (this.chosenAnswer === this.quizData.correct_answer) {
            this.isRightAnswer = true;
          }
          this.score(this.isRightAnswer);
          // Cooldown:
          await this.sleep(5000);
          // Clean variables:
          this.chosenAnswer = undefined;
          this.wasSubmitted = false;
          this.isRightAnswer = false;
          // If no winner yet, load the next question:
          if (!this.hasWinner) {
            this.fetchQuizData();
          }
        }
      },

      async fetchQuizData() {
        // This function request to the API the question and return it back to this app.
        this.isLoading = true;
        
        try {
          const response = await fetch('https://opentdb.com/api.php?amount=1&category=18');
          
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          
          const data = await response.json();

          // Decode HTML entities in the question
          const decoder = document.createElement('div');
          decoder.innerHTML = data.results[0].question;
          data.results[0].question = decoder.textContent;
          
          // Defining the quizData based on the first (or the only one) result element in that array:
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
    <h3>Loading...</h3>
  </div>

  <div v-else-if="quizData">
    <div class="score">
      You <span>{{ scorePlayer }}</span> X <span>{{ scoreMachine }}</span> Machine
      <small>Win who reaches {{ scoreLimit }} points first.</small>
    </div>

    <hr>

    <div v-if="!hasWinner">
      <h1 v-html="sanitizeHTML(quizData.question)" />
      <small class="header">
        Difficulty: {{ quizData.difficulty }}
      </small>
      <template
        v-for="(answer, idx) in answers"
        :key="idx"
      >
        <input
          :id="`answr_${idx}`"
          v-model="chosenAnswer"
          type="radio"
          name="options"
          :value="answer"
        >
        <label
          :for="`answr_${idx}`"
          v-html="answer"
        /><br>
      </template>

      <div v-if="wasSubmitted">
        <p 
          v-if="isRightAnswer"
          class="answer-right"
        >
          Right answer! Cool!
        </p>
        <p 
          v-else
          class="answer-wrong"
        >
          Sorry! The right answer was<br>
          <strong v-html="quizData.correct_answer" />
        </p>
      </div>
          
      <button
        v-if="!wasSubmitted"
        class="send"
        type="button"
        @click="submitForm"
      >
        Check answer
      </button>
    </div>

    <div v-else>
      <h1>{{ winnerMsg }}</h1>
      <small class="header">Refresh your browser for a new try.</small>
    </div>
  </div>

  <div v-else>
    <h3>No quiz data available!</h3>
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
      color:#666;
      display:block;
    }

    small.header {
      margin:-32px 0 30px 0;
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

    p.answer-right {
      color: greenyellow;
    }

    p.answer-wrong {
      color: orange;
    }

    .score span {
      font-size: x-large;
    }
  }
</style>
