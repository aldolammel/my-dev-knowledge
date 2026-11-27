// FILE: /frontend/src/router/guards.ts:

import type { Router } from "vue-router";
import { useAuth } from "@/composables/useAuth";

// Register global navigation guards:
export function registerNavigationGuards(router: Router): void {
    // registerNavigationGuards() avoids circular dependencies between index.ts and guards.ts!
    router.beforeEach(to => {
        const { isAuthenticated } = useAuth();

        // Visitors cannot access authenticated views/pages:
        if (to.meta.requiresAuth && !isAuthenticated) {
            return {
                name: "Login",
                query: { redirect: to.fullPath },
            };
        }
        // Authenticated users cannot access a few views/pages:
        if (to.meta.guestOnly && isAuthenticated) {
            return { name: "HomeLogged" };
        }
    });
}
