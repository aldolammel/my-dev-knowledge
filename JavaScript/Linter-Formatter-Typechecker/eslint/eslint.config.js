// FILE: /frontend/eslint.config.js

import js from "@eslint/js";
import globals from "globals";

export default [
  js.configs.recommended,
  {
    // Files ESLint should lint:
    files: ["**/*.js", "**/*.mjs"],
    // Language options (parser settings):
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        // Browser globals (window, document, etc):
        ...globals.browser,
        ...globals.node,
      },
    },
    // Core rules:
    rules: {
      "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
      "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    },
  },
  // Global ignores (standalone entry to apply project-wide):
  {
    ignores: ["node_modules/**", "dist/**", "public/**"],
  },
];