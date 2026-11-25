#### JavaScript > Vue
# Deployment

---
## x) xxxxxxxxxxxxx:
X) (Your project on Prod) When you are ready to ship your app to production, run the following:
```bash
npm run build
```
This will create a production-ready build of your app in the project's `./dist` directory.

---
## X) Front-end's `.env`:
Prepare the `/frontend/.env` file:
- Case you are using [Vite](/javascript/build-tools/vite/_install.md):
	- Change the `VITE_BASE_URL` value.

## X) If using Vite:
x.1) In `/frontend/vite.config.js` (or `frontend/vite.config.ts`), check which folder (`publicDir`) Vite will compile its file when ready to production.
