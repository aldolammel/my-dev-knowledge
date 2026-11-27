// REMINDER:
// 1: This '.d.ts' means .ts file is/must be just a 'declaration' file and nothing more than that!
// 2: TS auto-import this where the declared-module below is called, so no additional import needed!

import "vue-router";

// Declared module:
declare module "vue-router" {
    interface RouteMeta {
        guestOnly?: boolean;
        requiresAuth?: boolean;
    }
}
