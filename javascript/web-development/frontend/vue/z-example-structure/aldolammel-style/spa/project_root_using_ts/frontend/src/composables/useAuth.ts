// CRITICAL: attention, this user authentication is temporary before the Pinia implementation!
export function useAuth() {
  const isAuthenticated =
    import.meta.env.VITE_DEBUG === "true" && import.meta.env.VITE_LOCAL_FAKE_USER_LOGGED === "true";
  return {
    isAuthenticated,
  };
}
