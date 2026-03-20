// FILE: /frontend/eslint.config.js
// This basic file model: /JavaScript/Linter-Formatter-Typechecker/eslint/eslint.config.js

import js from '@eslint/js';
import pluginVue from 'eslint-plugin-vue';  // <---- ADD IT!
//...

export default [
  js.configs.recommended,
  ...pluginVue.configs['flat/recommended'],  // <---- ADD IT!
  {
    files: ['**/*.vue', '**/*.js', '**/*.mjs'],  // <---- ADD IT!
    languageOptions: {
      parser: pluginVue.parser,  // <---- ADD IT!
      ecmaVersion: 'latest',
      //...
    },
    rules: {
      'vue/multi-word-component-names': 'off', // <---- ADD IT!
      //...
    },
  },
  //...
];