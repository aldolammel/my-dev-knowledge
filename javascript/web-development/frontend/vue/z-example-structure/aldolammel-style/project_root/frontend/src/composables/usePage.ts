
/*
  This Vue composable manages page data retrieval and computed state for the app. It does:
  1. Route-based slug extraction: Parses the current URL to extract slugs without route params;
  2. Page data management: Fetches and caches page data from a Pinia store (pagesStore);
  3. Blog-specific handling: For blog pages, also manages associated blog posts (postsStore);
  4. Readiness checking: Set when a page has loaded enough content to render;
  5. Content access helper: Serve getPagex() method to safely extract specific content values;
*/

import { computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
import { usePostsStore } from "@/stores/posts"; // Vue Pinia

interface PageContentField {
  v?: string | null;
  [key: string]: unknown;
}

interface Page {
  slug: string;
  is_home?: boolean;
  is_blog?: boolean;
  content?: Record<string, PageContentField>;
  [key: string]: unknown;
}

type PageValue = string | null | undefined | Record<string, unknown>;

 /*
 * Composable for page data management:
 * @param isHome - Whether this is the home page (needs is_home fallback)
 * @param isBlog - Whether this is a blog page (needs is_blog fallback)
 */
export function usePage(isHome = false, isBlog = false) {
  const route = useRoute();
  const router = useRouter();
  const pagesStore = usePagesStore();
  const postsStore = usePostsStore();

  // Compute page blogSlug from current route path:
  // This project router doesn't use slug as params but props!
  const blogSlug = computed<string | null>(() => {
    if (isBlog) {
      const pathParts = route.path.split("/");
      return pathParts[1] || null; // Gets 'blog_slug' from '/blog_slug' or '/blog_slug/post-slug'
    }
    return null;
  });

  // Compute page slug from current route path:
  // This project router doesn't use slug as parameters but props!
  const slug = computed<string | null>(() => {
    // For Page blogs:
    if (isBlog) {
      return route.path.slice(1);
    }

    // If path is just a '/', then pathSlug is '', otherwise pathSlug is the last part of the path:
    const pathSlug = route.path === "/" ? "" : route.path.slice(1);

    // If Home, use path slug or fallback to is_home page:
    if (isHome) {
      if (pathSlug) return pathSlug;

      const homePage = Object.values(pagesStore.pages).find((p: Page) => p.is_home);

      return homePage ? homePage.slug : null;
    }

    // Regular pages:
    return pathSlug || null;
  });

  // Get page data from pagesStore:
  const pg = computed<Page | null>(() => {
    if (isBlog) {
      return pagesStore.pages[blogSlug.value] || null;
    }

    return slug.value ? pagesStore.pages[slug.value] || null : null;
  });

  // If this page's content is loaded, page ready to render:
  const isPageReady = computed<boolean>(() => {
    // For blog pages, check both page content and posts data:
    if (isBlog) {
      const hasPageContent =
        pg.value?.content && Object.keys(pg.value.content).length > 0;

      const hasBlogPosts =
        blogSlug.value &&
        Object.keys(postsStore.getPostsByBlog(blogSlug.value)).length > 0;

      return Boolean(
        hasPageContent &&
        hasBlogPosts &&
        !pagesStore.loading &&
        !postsStore.loading
      );
    }

    // Otherwise, for regular pages:
    return Boolean(
      pg.value?.content &&
      Object.keys(pg.value.content).length > 0 &&
      !pagesStore.loading
    );
  });

  /**
   * Function/Helper to extract Pagex content
   * @param key - A dictionary element key that's contain the content to use.
   * @returns key value | null
   */
  const getPagex = (key: string): PageValue => {
    // First, check if it's a flat/root-level field (like SEO fields):
    if (pg.value?.[key] !== undefined) {
      return pg.value[key] as PageValue;
    }

    // Otherwise, check nested content fields (with .v property):
    // TODO: it wont work properly with tags and categories 'cause the nested struct isn't the same!
    return pg.value?.content?.[key]?.v || null;
  };

  // Fetch page data on component mount:
  onMounted(async (): Promise<void> => {
    if (slug.value) {
      const result = await pagesStore.fetchPage(slug.value);

      if (!result.success && result.status === 503) {
        router.push("/503");
        return;
      }

      // If it's a blog page, also fetch posts:
      if (isBlog && blogSlug.value) {
        await postsStore.fetchAllPosts();
      }
    }
  });

  return {
    slug,
    blogSlug,
    pg,
    isPageReady,
    getPagex,
    loading: computed<boolean>(() =>
      isBlog ? pagesStore.loading || postsStore.loading : pagesStore.loading
    ),
  };
}
