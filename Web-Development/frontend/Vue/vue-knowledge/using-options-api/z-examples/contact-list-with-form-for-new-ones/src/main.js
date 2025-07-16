import { createApp } from 'vue'  // this method to call Vue only works with local installation!
import './style.css'  // once the index.html is NOT calling for this css file...
import App from './ParentComponent.vue'  // calling the main/parent app!

createApp(App).mount('#app')
