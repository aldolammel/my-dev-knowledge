// FILE: /my_django_project/frontend/vite.config.js

//...

export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  build: {
    // Ensure assets are placed in correct directory
    assetsDir: 'assets',
    // Generate manifest for Django to read
    manifest: true,
    rollupOptions: {
      output: {
        // Ensure clean asset names
        assetFileNames: 'assets/[name].[hash][extname]',
        chunkFileNames: 'assets/[name].[hash].js',
        entryFileNames: 'assets/[name].[hash].js',
      },
    },
  },
  plugins: [
    //...
  ],
  //...
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      },
      '/media': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
});

// ...