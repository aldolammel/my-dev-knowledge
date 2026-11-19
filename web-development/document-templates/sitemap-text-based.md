#### Web-development > Documents
# Sitemap text-based document

---

This template doesn't replace a good and editable [sitemap diagram](/web-development/document-templates/sitemap.md). This text-based version makes the sitemap more "readable" and cheap for AI assistance. That said, after you get the project sitemap (diagram) approved, make sure to convert that to a text-based version like this one below, storing the file in `/your_project/.agents/` folder as `sitemap.md` name.

==UPDATES==
Define with your team what you wanna do about the diagram and the text-based version when the sitemap demand update. 
**Recommendation:** no matter what it takes, keep the text-based updated!

---
## Public pages:
```
ProductMainDomain.com
├── Home                                       [page]
│   └── Registration                           [form]
│       └── User Email Confirmation            [email]
├── Login                                      [page]
│   └── Login                                  [form]
├── Support                                    [page]
│   └── Subject items                          [interface context]
│       └── Item                               [page]
├── Terms of Use                               [page]
└── Developed by You                           [external url]
```
## Authenticated pages:
```
ProductMainDomain.com
├── Home                                                                [page]
│   └── Items organized by SomethingA or SomethingB                     [interface context]
│       └── Item                                                        [page]
│           └── Another thing items organized by main item              [interface context]
│               └── Item by a user                                      [page]
├── Profile                                     [page]
│   └── Only for other profile pages            [interface context]
│       └── Report this user                    [page]
│           └── Reporting                       [form]
│               └── Email of report             [email]
├── Support                      [page]
│   └── Subject items            [interface context]
│       └── Item                 [page]
├── Terms of Use                 [page]
└── Developed by You             [external url]
```
## Shared system pages:
```
ProductMainDomain.com
├── Login Back-end CMS               [hidden page]
│   └── Back-end authenticated stuff [group of pages]
├── E-mail successfully confirmed    [page]
├── Password forgotten               [page]
│   └── Email password reset         [email]
├── Access denied (403)              [page]
└── Not found (404)                  [page]
```
## Navigation menus:

**Main menu**
```
Links only for visitor:
- Home (visitor version)           [link]
- Login                            [link]
Links only for authenticated user:
- Home (user version)              [link]
- User profile                     [link]
Link for both:
- Support                          [link]
- Language                         [drop-down menu]
```

**User menu in Profile**
```
Only for their own user profile page:
- Change password                  [link]
- Update your email                [link]
- Log out                          [link]
- Delete account                   [link]
Only for other user profile pages:
- Report this user                 [link]
```

**Footer menu**
```
- Terms of Use                     [link]
- Developed by You                 [external link]
```