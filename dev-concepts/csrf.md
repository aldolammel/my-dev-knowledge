#### Dev concepts
# Cross-Site Request Forgery (CSRF)

---

It's a important web vulnerability where a malicious site tricks a user's browser into making an unintended, authenticated request to another site where the user is already logged in.

---
### How It Works

1. You log into `bank.com`, and your browser stores a session cookie.
2. You visit a malicious site (`evil.com`) in another tab.
3. `evil.com` triggers a hidden form or request to `[bank.com/transfer?to=attacker&amount=1000](https://bank.com/transfer?to=attacker&amount=1000)`.
4. Your browser automatically attaches your `bank.com` session cookie, so `bank.com` treats the request as legitimate.

---
