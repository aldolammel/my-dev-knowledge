// File: eslint.config.js
// MORE ABOUT: https://eslint.vuejs.org/

import js from '@eslint/js';
import pluginVue from 'eslint-plugin-vue';
import globals from 'globals';

export default [
  js.configs.recommended,
  ...pluginVue.configs['flat/recommended'],
  {
    files: ['**/*.vue', '**/*.js', '**/*.mjs'],
    languageOptions: {
      parser: pluginVue.parser,
      ecmaVersion: 2022,
      sourceType: 'module',
      globals: {
        ...globals.browser,
        process: true
      }
    },
    rules: {
      // Vue rules
      'vue/multi-word-component-names': 'off',
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    },
  },
  {
    ignores: [
      'node_modules/**',
      'dist/**',
      'public/**',
    ],
  },
];