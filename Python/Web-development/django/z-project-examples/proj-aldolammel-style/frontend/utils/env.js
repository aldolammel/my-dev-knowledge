export const env = {
  // INFO: If you're using Vue with Vite, Vite demands from each front-end env var the 'VITE_' prefix:
  isDebug: String(import.meta.env.VITE_DEBUG).toLowerCase() === "true",
};
