// FILE: /my_django_project/frontend/vite.config.js

//...
import { config } from "dotenv";

// Load front-end environment variables:
const frontEnvVars = config({ path: "./.env" }).parsed || {};

export default defineConfig({
  base: process.env.NODE_ENV === "production" ? "/static/" : "/",
  build: {
    // Ensure assets are placed in correct directory
    assetsDir: "assets",
    // Generate manifest for Django to read
    manifest: true,
    rollupOptions: {
      output: {
        // Ensure clean asset names
        assetFileNames: "assets/[name].[hash][extname]",
        chunkFileNames: "assets/[name].[hash].js",
        entryFileNames: "assets/[name].[hash].js",
      },
    },
  },
  plugins: [
    //...
  ],
  //...
  server: {
    proxy: {
      "/api": {
        target: frontEnvVars.VITE_BASE_URL, // Cannot use the import.meta.env.VITE_BASE_URL here!
        changeOrigin: true
      },
      "/media": {
        target: frontEnvVars.VITE_BASE_URL, // Cannot use the import.meta.env.VITE_BASE_URL here!
        changeOrigin: true
      }
    }
  }
});

// ...