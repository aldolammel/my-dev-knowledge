<script setup>
import { ref, computed, onBeforeUnmount } from 'vue'

// Reactive state variables using ref()
// Basic progress value (0-100)
const basicProgress = ref(30)

// Custom progress bar value
const customProgress = ref(45)

// Animated progress bar value and animation state
const animatedProgress = ref(0)
const isAnimating = ref(false)
const animationInterval = ref(null)

// Multi-step progress data
const currentStep = ref(0)
const steps = ref(['Personal Info', 'Contact Details', 'Preferences', 'Review', 'Complete'])

// Circular progress value
const circularProgress = ref(75)

// SVG circle properties for circular progress
const circumference = 2 * Math.PI * 50 // 2πr where r=50

// Computed property - Calculate stroke-dashoffset for circular progress animation
const circularOffset = computed(() => {
  const progress = circularProgress.value / 100
  return circumference * (1 - progress)
})

// Function to update basic progress with random value
const updateBasicProgress = () => {
  basicProgress.value = Math.floor(Math.random() * 101)
}

// Function to increase custom progress by 10%
const increaseCustomProgress = () => {
  if (customProgress.value < 100) {
    customProgress.value = Math.min(customProgress.value + 10, 100)
  }
}

// Function to decrease custom progress by 10%
const decreaseCustomProgress = () => {
  if (customProgress.value > 0) {
    customProgress.value = Math.max(customProgress.value - 10, 0)
  }
}

// Function to reset custom progress to 0
const resetCustomProgress = () => {
  customProgress.value = 0
}

// Function to start animated progress simulation
const startAnimation = () => {
  if (isAnimating.value) return
  
  isAnimating.value = true
  animatedProgress.value = 0
  
  // Animate progress from 0 to 100 over 3 seconds
  animationInterval.value = setInterval(() => {
    animatedProgress.value += 2
    if (animatedProgress.value >= 100) {
      animatedProgress.value = 100
      clearInterval(animationInterval.value)
      isAnimating.value = false
    }
  }, 60) // Update every 60ms for smooth animation
}

// Function to get color based on progress percentage
const getProgressColor = (progress) => {
  if (progress < 30) return '#f44336' // Red for low progress
  if (progress < 70) return '#ff9800' // Orange for medium progress
  return '#4caf50' // Green for high progress
}

// Function to move to next step in multi-step progress
const nextStep = () => {
  if (currentStep.value < steps.value.length - 1) {
    currentStep.value++
  }
}

// Function to move to previous step in multi-step progress
const previousStep = () => {
  if (currentStep.value > 0) {
    currentStep.value--
  }
}

// Function to reset multi-step progress to beginning
const resetSteps = () => {
  currentStep.value = 0
}

// Function to increase circular progress by 5%
const increaseCircularProgress = () => {
  if (circularProgress.value < 100) {
    circularProgress.value = Math.min(circularProgress.value + 5, 100)
  }
}

// Function to decrease circular progress by 5%
const decreaseCircularProgress = () => {
  if (circularProgress.value > 0) {
    circularProgress.value = Math.max(circularProgress.value - 5, 0)
  }
}

// Lifecycle hook - Cleanup interval on component unmount
onBeforeUnmount(() => {
  if (animationInterval.value) {
    clearInterval(animationInterval.value)
  }
})
</script>

<template>
  <div class="progress-examples">
    <h2>Vue.js Progress Bar Examples</h2>

    <!-- Example 1: Basic HTML5 Progress Element -->
    <div class="example-section">
      <h3>1. HTML5 Progress Element</h3>
      <!-- Basic progress bar using native HTML5 progress element -->
      <progress :value="basicProgress" max="100">{{ basicProgress }}%</progress>
      <p>Progress: {{ basicProgress }}%</p>
      <!-- Button to simulate progress updates -->
      <button @click="updateBasicProgress">Update Progress</button>
    </div>

    <!-- Example 2: Custom CSS Progress Bar -->
    <div class="example-section">
      <h3>2. Custom CSS Progress Bar</h3>
      <!-- Custom progress bar with dynamic width based on completion percentage -->
      <div class="progress-container">
        <div 
          class="progress-bar" 
          :style="{ width: customProgress + '%' }"
        >
          {{ customProgress }}%
        </div>
      </div>
      <!-- Controls to increase/decrease progress -->
      <div class="controls">
        <button @click="decreaseCustomProgress">-</button>
        <button @click="increaseCustomProgress">+</button>
        <button @click="resetCustomProgress">Reset</button>
      </div>
    </div>

    <!-- Example 3: Animated Progress Bar with Color Changes -->
    <div class="example-section">
      <h3>3. Animated Progress Bar with Color Changes</h3>
      <!-- Progress bar that changes color based on completion level -->
      <div class="animated-progress-container">
        <div 
          class="animated-progress-bar" 
          :style="{ 
            width: animatedProgress + '%',
            backgroundColor: getProgressColor(animatedProgress)
          }"
        >
          <span class="progress-text">{{ animatedProgress }}%</span>
        </div>
      </div>
      <!-- Button to start automated progress simulation -->
      <button @click="startAnimation" :disabled="isAnimating">
        {{ isAnimating ? 'Animating...' : 'Start Animation' }}
      </button>
    </div>

    <!-- Example 4: Multi-step Progress Indicator -->
    <div class="example-section">
      <h3>4. Multi-step Progress Indicator</h3>
      <!-- Step-by-step progress indicator for forms or wizards -->
      <div class="steps-container">
        <div 
          v-for="(step, index) in steps" 
          :key="index"
          class="step"
          :class="{ 
            'completed': index < currentStep, 
            'active': index === currentStep 
          }"
        >
          <!-- Step number or checkmark for completed steps -->
          <div class="step-indicator">
            <span v-if="index < currentStep">✓</span>
            <span v-else>{{ index + 1 }}</span>
          </div>
          <!-- Step label -->
          <span class="step-label">{{ step }}</span>
        </div>
      </div>
      <!-- Navigation buttons for steps -->
      <div class="step-controls">
        <button @click="previousStep" :disabled="currentStep === 0">Previous</button>
        <button @click="nextStep" :disabled="currentStep === steps.length - 1">Next</button>
        <button @click="resetSteps">Reset</button>
      </div>
    </div>

    <!-- Example 5: Circular Progress Bar -->
    <div class="example-section">
      <h3>5. Circular Progress Bar (SVG)</h3>
      <!-- SVG-based circular progress indicator -->
      <div class="circular-progress">
        <svg width="120" height="120">
          <!-- Background circle -->
          <circle
            cx="60"
            cy="60"
            r="50"
            stroke="#e0e0e0"
            stroke-width="8"
            fill="none"
          />
          <!-- Progress circle that animates based on completion -->
          <circle
            cx="60"
            cy="60"
            r="50"
            stroke="#4CAF50"
            stroke-width="8"
            fill="none"
            :stroke-dasharray="circumference"
            :stroke-dashoffset="circularOffset"
            transform="rotate(-90 60 60)"
            class="progress-circle"
          />
        </svg>
        <!-- Centered percentage text -->
        <div class="circular-text">{{ circularProgress }}%</div>
      </div>
      <!-- Controls for circular progress -->
      <div class="controls">
        <button @click="decreaseCircularProgress">-</button>
        <button @click="increaseCircularProgress">+</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Container styling */
.progress-examples {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* Section spacing */
.example-section {
  margin-bottom: 40px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

/* Basic HTML5 progress element styling */
progress {
  width: 100%;
  height: 30px;
  margin: 10px 0;
}

/* Custom progress bar container */
.progress-container {
  width: 100%;
  height: 30px;
  background-color: #e0e0e0;
  border-radius: 15px;
  overflow: hidden;
  margin: 10px 0;
}

/* Custom progress bar fill */
.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #4CAF50, #45a049);
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  transition: width 0.3s ease;
  min-width: 50px; /* Ensure text is visible even at low percentages */
}

/* Animated progress bar container */
.animated-progress-container {
  width: 100%;
  height: 35px;
  background-color: #e0e0e0;
  border-radius: 17px;
  overflow: hidden;
  margin: 10px 0;
  position: relative;
}

/* Animated progress bar with smooth transitions */
.animated-progress-bar {
  height: 100%;
  border-radius: 17px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: width 0.1s ease, background-color 0.3s ease;
  position: relative;
}

/* Progress text styling */
.progress-text {
  color: white;
  font-weight: bold;
  font-size: 14px;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}

/* Control buttons styling */
.controls {
  margin-top: 15px;
}

.controls button, .step-controls button {
  margin: 0 5px;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #2196F3;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.controls button:hover, .step-controls button:hover {
  background-color: #1976D2;
}

.controls button:disabled, .step-controls button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Multi-step progress indicator */
.steps-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px 0;
  position: relative;
}

/* Connection line between steps */
.steps-container::before {
  content: '';
  position: absolute;
  top: 20px;
  left: 20px;
  right: 20px;
  height: 2px;
  background-color: #e0e0e0;
  z-index: 1;
}

/* Individual step styling */
.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 2;
}

/* Step indicator circle */
.step-indicator {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin-bottom: 8px;
  transition: all 0.3s ease;
}

/* Active step styling */
.step.active .step-indicator {
  background-color: #2196F3;
  color: white;
}

/* Completed step styling */
.step.completed .step-indicator {
  background-color: #4CAF50;
  color: white;
}

/* Step label */
.step-label {
  font-size: 12px;
  text-align: center;
  color: #666;
  max-width: 80px;
}

.step.active .step-label {
  color: #2196F3;
  font-weight: bold;
}

.step.completed .step-label {
  color: #4CAF50;
}

/* Step control buttons */
.step-controls {
  margin-top: 20px;
  text-align: center;
}

/* Circular progress bar container */
.circular-progress {
  position: relative;
  display: inline-block;
  margin: 20px;
}

/* Circular progress animation */
.progress-circle {
  transition: stroke-dashoffset 0.3s ease;
}

/* Centered text in circular progress */
.circular-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

/* Responsive design for smaller screens */
@media (max-width: 600px) {
  .steps-container {
    flex-direction: column;
    gap: 20px;
  }
  
  .steps-container::before {
    display: none;
  }
  
  .step {
    width: 100%;
    flex-direction: row;
    justify-content: flex-start;
    gap: 15px;
  }
  
  .step-label {
    max-width: none;
    font-size: 14px;
  }
}
</style>