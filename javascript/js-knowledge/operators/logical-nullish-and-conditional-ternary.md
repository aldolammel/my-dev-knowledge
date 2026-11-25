#### JavaScript > Operators
# Using operators for logical, nullish and conditional (Ternary)

---

```js
true && "ok";     // "ok" (AND: returns first falsy or last truthy)
false || "fallback"; // "fallback" (OR: returns first truthy or last falsy)
null ?? "default";   // "default" (Nullish coalescing: only for null or undefined)
0 ?? "default";      // 0 (unlike ||, 0 and "" are NOT nullish)
!false;              // true (NOT)

const status = x > 0 ? "positive" : "non-positive"; // ternary

// Logical assignment (ES2021+)
let a: string | null = null;
a ??= "init";     // assigns "init" only if null/undefined
a &&= "updated";  // assigns if truthy
a ||= "fallback"; // assigns if falsy
```