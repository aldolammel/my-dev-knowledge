#### JavaScript > Operators
# And (&&)

---

Operators are exactly the same in JavaScript and TypeScript.

Example pure `.js`:
```js
const isLoggedIn = true;
const isAdmin = true;

if (isLoggedIn && isAdmin) {
  console.log("Access granted");
}
```
Example in `.ts`:
```ts
function printLength(text: string | null) {
	// TS knows `text` is a `string` after `text !== null`
	if (text !== null && text.length > 0) {
		console.log(text.toUpperCase());
	}
}
```
Note: A single `&` is the bitwise AND operator in both languages — avoid using it for standard boolean conditions.

---

