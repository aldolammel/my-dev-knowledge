import { createApp } from 'vue'  // this method to call Vue only works with local installation!
import './style.css'  // once the index.html is NOT calling for this css file...
import App from './App.vue'  // calling the main/parent app!

//createApp(App).mount('#app')
// or...

const app = createApp(App);
app.mount('#app');

