In `/frontend/eslint.config.js`:
```js
// ...
import globals from "globals";
import { defineConfig } from "eslint/config";

const isProd = process.env.NODE_ENV === "production";

export default defineConfig([
    // Global ignores:
    {
        ignores: ["node_modules/**", "dist/**", "public/**"],
    },

    // Core configuration:
    {
        files: [...],
        // ...,
        languageOptions: {
            sourceType: "module", // Uses ES Modules (import/export)
            globals: globals.browser,
        },
        rules: {
            // Disable console and debugger warnings only in development:
            "no-console": isProd ? "warn" : "off",
            "no-debugger": isProd ? "warn" : "off",
        },
    },
    
    // TypeScript configuration: (if available)
    // Reserved space...
    
    // Your JS Front-end framework configuration:
    // Reserved space...
]);

```

---
## TypeScript version:
(I don't like for ESLint config file because JS version is more solid/compatible)


