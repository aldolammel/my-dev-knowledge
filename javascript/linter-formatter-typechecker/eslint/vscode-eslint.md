FILE: `/project/.vscode/settings.json`:
Check if validate lines make sense for your project!
```json
{
    // PROJECT SETTINGS
    "editor.codeActionsOnSave": { // ESLint
        // This will auto-correct all fixable ESLint errors:
        "source.fixAll.eslint": "explicit"
    },
    "eslint.validate": [ // ESLint
        "javascript", // Keep it always on!
        //"javascriptreact", // Add this only if the project is using React!
        //"typescript", // Add this only if the project uses TS!
        //"vue", // Add this only if the project is using Vue!
    ],
    "eslint.workingDirectories": [
        "frontend" // ESLint working directories (ONLY if it's in a subfolder of frontend installed)
    ],
}
```

