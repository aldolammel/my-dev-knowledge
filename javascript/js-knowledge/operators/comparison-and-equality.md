#### JavaScript > Operators
# Using operators for comparison and equality

---

```ts
5 === 5;         // true (strict equality: same type & value)
5 !== "5";       // true (strict inequality)

// Loose equality (coerces types) — TS often flags obvious type mismatches at compile time
5 == "5" as any; // true at runtime, though `5 == "5"` is a TS compile error without widening/casting
5 != "6" as any; // true

10 > 5;          // true
10 >= 10;        // true
3 < 5;           // true
3 <= 3;          // true
```


