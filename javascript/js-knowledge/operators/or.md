#### JavaScript > Operators
# Or (||)

---

Operators are exactly the same in JavaScript and TypeScript.

Important: `??` is  a close cousin for `null`/`undefined` only.

Example pure `.js`:
```js
const isAdmin = false;
const isModerator = true;
if (isAdmin || isModerator) {
	console.log("Access granted");
}
```

Examples in `.ts`:
```ts
const displayName = "" || "Guest"; // "Guest" ("" is falsy)
const port = 0 || 3000;            // 3000 (0 is falsy—watch out!)
const count = 0 ?? 10;             // 0 (kept!)
```

```ts
function formatId(id: string | number | null) {
  if (typeof id === "string" || typeof id === "number") {
    // TS narrows `id` here to `string | number`
    return String(id).toUpperCase();
  }
  return "NONE";
}
```
Note: A single `|` is the bitwise OR at runtime, and a **union type** operator in TypeScript type annotations like `string | number`.

---


