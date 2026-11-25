#### JavaScript > Operators
# Using operators in object, array and function operators

---

```ts
const user = { name: "Ana", address: { city: "POA" } };

user?.address?.city; // "POA" (optional chaining; returns undefined if null/undefined)
"name" in user;      // true (property check; also narrows union types in TS)
user instanceof Date;// false (prototype check; also narrows classes in TS)
typeof user;         // "object" (runtime type string; also a type query in TS)
delete (user as { temp?: string }).temp; // deletes property (restricted on non-optional TS props)

const nums = [1, 2];
const combined = [...nums, 3]; // spread
const [first, ...rest] = combined; // rest in destructuring

function sum(...values: number[]) { // rest parameter in TS
  return values.reduce((acc, n) => acc + n, 0);
}

void (1 + 1); // undefined (evaluates expression, discards result)
```