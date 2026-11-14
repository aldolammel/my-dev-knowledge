/*
  This composable provides centralized error handling logic for API responses.
  It handles common HTTP status codes and redirects accordingly.
*/

import { useRouter } from "vue-router";

export function useErrorHandler() {
  const router = useRouter();

  /**
   * Handle API response errors with appropriate actions
   * param {object} result - Result obj from store action with { success, status }
   * returns {boolean} - True if error was handled and navigation occurred
   */
  function handleApiError(result) {
    if (result.success) {
      return false; // No error to handle ;)
    }
    switch (result.status) {
      case 404:
        console.warn("FRONTEND WARN > Error Handler > Resource not found (404)");
        router.push("/404");
        return true;
      case 503:
        console.error("FRONTEND ERROR > Error Handler > Service unavailable (503)");
        router.push("/503");
        return true;
      case 500:
        console.error("FRONTEND ERROR > Error Handler > Internal server error (500)");
        router.push("/503"); // Treat 500 like 503!
        return true;
      default:
        console.error(`FRONTEND ERROR > Error Handler > Unexpected error status: ${result.status}`);
        return false;
    }
  }

  /**
   * Get user-friendly error message based on status code
   * param {number} status - HTTP status code
   * returns {string} - User-friendly error message
   */
  function getErrorMsg(status) {
    const msg = {
      404: "Aparentemente, a página que você está tentando acessar não existe.",
      503: "Estamos offline, aparentemente. Por gentileza, volte em alguns minutos.",
      500: "Ocorreu um erro em nosso servidor. Tente novamente mais tarde.",
      default: "Algum erro ainda não-identificado ocorreu!",
    };

    return msg[status] || msg.default;
  }

  return {
    handleApiError,
    getErrorMsg,
  };
}
