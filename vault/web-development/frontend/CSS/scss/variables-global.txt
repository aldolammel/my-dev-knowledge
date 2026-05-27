

SCSS VARIABLES: GLOBAL VARIABLES:

    
    >> Through Vue+Vite projects:
    
    
        PRE) Assuming you already did it:
            ./vue-integration.txt

        
        1) To use global SCSS variables, update your vite.config.js:
            
            // FILE: /project/frontend/vite.config.js
            //...

            export default defineConfig({
                plugins: [
                    //...
                ],
                css: {
                    preprocessorOptions: {
                        scss: {
                            additionalData: `@use "@/assets/styles/vars" as *;`,
                        }
                    }
                },
                //...
            })