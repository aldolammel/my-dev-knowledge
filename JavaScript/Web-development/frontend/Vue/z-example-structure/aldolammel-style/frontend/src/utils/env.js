export const env = {
  // INFO: For Vue projects using Vite as Build-tool, Vite demands 'VITE_' prefix in env vars!
  isDebug: String(import.meta.env.VITE_DEBUG).toLowerCase() === "true",
};
