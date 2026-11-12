FILE: `/frontend/eslint.config.js`:
```json
//...
import prettier from "eslint-plugin-prettier";
import prettierConfig from "eslint-config-prettier";

export default [
  //...
  // Adding Prettier config to disable conflicting rules:
  prettierConfig,
  {
    files: [...],
    //...
    plugins: {
      prettier,
    },
    // Core rules:
    rules: {
      //...
      "prettier/prettier": "error", // All Prettier rules are detailed in its .prettierrc!
    },
    //...
  },
]
```


