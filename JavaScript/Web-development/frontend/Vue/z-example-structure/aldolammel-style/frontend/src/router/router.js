import { createRouter, createWebHistory } from "vue-router";
import { routes, componentRegistry } from "@/router/routes"; // Bringing Vue Component pages and static routes!
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
import { usePostsStore } from "@/stores/posts"; // Vue Pinia
import { useCategoriesStore } from "@/stores/categories"; // Vue Pinia
import { useTagsStore } from "@/stores/tags"; // Vue Pinia
import { env } from "@/utils/env"; // Debug purposes

// Create the router instance:
const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

// Dynamic routes initialization function:
export async function initDynamicRoutes() {
  const store_pages = usePagesStore();
  const store_posts = usePostsStore();
  const store_categories = useCategoriesStore();
  const store_tags = useTagsStore();

  const pages = await store_pages.fetchAllPages();
  const posts = await store_posts.fetchAllPosts();
  const categories = await store_categories.fetchAllCategories();
  const tags = await store_tags.fetchAllTags();

  // Fetch each page and add their slug as a new route, storing them as Props, not as parameters:
  pages.forEach((page) => {
    const componentLoader = componentRegistry[page.vue_component];
    if (componentLoader) {
      // Adding the page slug as a new route:
      router.addRoute({
        path: `/${page.slug}`,
        component: componentLoader,
        props: { slug: page.slug },
      });
      if (page.is_home) {
        router.addRoute({
          path: "/",
          component: componentLoader,
          props: { slug: page.slug },
        });
      }
    } else {
      console.error(`FRONTEND ERROR > router.js: there's NO '${page.vue_component}' component!`);
    }
  });

  // Add category routes dynamically for each category:
  categories.forEach((category) => {
    router.addRoute({
      path: `/c/${category.slug}`, // It's also partially declared in /apps/pagex/constants.py
      component: componentRegistry["ListByCategory"],
      props: { categorySlug: category.slug },
    });
  });

  // Add tag routes dynamically for each tag:
  tags.forEach((tag) => {
    router.addRoute({
      path: `/t/${tag.slug}`, // It's also partially declared in /apps/pagex/constants.py
      component: componentRegistry["ListByTag"],
      props: { tagSlug: tag.slug },
    });
  });

  // Add blog routes dynamically for each blog:
  const uniqueBlogSlugs = [...new Set(posts.map((post) => post.blog_slug))];
  uniqueBlogSlugs.forEach((blogSlug) => {
    router.addRoute({
      path: `/${blogSlug}`,
      component: componentRegistry["LoadBlog"],
      props: { blogSlug },
    });
  });

  // Fetch each post and add their slug as a new route, storing them as Props, not as parameters:
  posts.forEach((post) => {
    router.addRoute({
      path: `/${post.blog_slug}/${post.slug}`,
      component: componentRegistry["LoadBlogPost"],
      props: { slug: post.slug, blogSlug: post.blog_slug },
    });
  });

  // Debug:
  if (env.isDebug) {
    console.debug(
      "FRONTEND DEBUG > router.js > Routes (statics + dynamics) available:",
      router.getRoutes(),
    );
  }
}

export default router;
