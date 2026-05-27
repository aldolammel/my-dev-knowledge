// THIS FILE: /project_django/frontend/vite.config.js

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import eslintPlugin from "vite-plugin-eslint";
import path from "path";
import { config } from "dotenv";

// Load front-end environment variables:
const frontEnvVars = config({ path: "./.env" }).parsed || {};

export default defineConfig({
  base: process.env.NODE_ENV === "production" ? "/static/" : "/",
  build: {
    outDir: "../templates", // Build to Django templates directory
    assetsDir: "static", // Place assets in static directory
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
    vue(),
    eslintPlugin({
      include: ["src/**/*.js", "src/**/*.vue", "src/*.js", "src/*.vue"],
      exclude: ["node_modules/**", "dist/**"],
      cache: false,
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(path.dirname(new URL(import.meta.url).pathname), "./src"),
    },
  },
  publicDir: "public",
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/assets/styles/vars" as *;`,
        /* 
        Bootstrap 2025 optional: Silence Sass deprecation warnings:
        Note: Sass deprecation warnings are shown when compiling source Sass files with the latest
        versions of Dart Sass. This doesn't prevent compilation or usage of Bootstrap. We’re working on a long-term fix, but in the meantime these deprecation notices can be ignored.
        */
        quietDeps: true, // Handling deprecation warnings!
        sassOptions: {
          quietDeps: true, // Belt and suspenders approach!
        },
      },
    },
  },
  server: {
    proxy: {
      "/api": {
        target: frontEnvVars.VITE_BASE_URL,
        changeOrigin: true,
      },
      "/media": {
        target: frontEnvVars.VITE_BASE_URL,
        changeOrigin: true,
      },
    },
  },
});
