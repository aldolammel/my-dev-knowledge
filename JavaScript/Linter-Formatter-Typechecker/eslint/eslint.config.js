// FILE: /frontend/eslint.config.js

//...
import prettier from "eslint-plugin-prettier";
import prettierConfig from "eslint-config-prettier";

export default [
  //...
  ...pluginVue.configs["flat/recommended"],

  // Adding Prettier config to disable conflicting rules:
  prettierConfig,
  {
    //...
    plugins: {
      prettier,
    },
    rules: {
      "prettier/prettier": [
        // Shows Prettier formatting issues as ESLint errors!
        "error",
        {
          printWidth: 100,
          semi: true,
          singleQuote: false,
          trailingComma: "es5",
        },
      ],
      //...
    },
    //...
  },
]