/*
  This composable provides centralized error handling logic for API responses.
  It handles common HTTP status codes and redirects accordingly.
*/

import { useRouter } from "vue-router";

interface ApiResult {
  success: boolean;
  status: number;
}

export function useErrorHandler() {
  const router = useRouter();

  /**
   * Handle API response errors with appropriate actions
   * @param result - Result object from store action with { success, status }
   * @returns True if error was handled and navigation occurred
   */
  function handleApiError(result: ApiResult): boolean {
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
        console.error(
          `FRONTEND ERROR > Error Handler > Unexpected error status: ${result.status}`,
        );
        return false;
    }
  }

  /**
   * Get user-friendly error message based on status code
   * @param status - HTTP status code
   * @returns User-friendly error message
   */
  function getErrorMsg(status: number): string {
    const messages: Record<number | "default", string> = {
      404: "Aparentemente, a página que você está tentando acessar não existe.",
      503: "Estamos offline, aparentemente. Por gentileza, volte em alguns minutos.",
      500: "Ocorreu um erro em nosso servidor. Tente novamente mais tarde.",
      default: "Algum erro ainda não-identificado ocorreu!",
    };

    return messages[status] ?? messages.default;
  }

  return {
    handleApiError,
    getErrorMsg,
  };
}
