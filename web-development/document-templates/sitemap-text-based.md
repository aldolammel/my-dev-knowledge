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
├── Create account (visitor home)      [page]
│   └── Registration                   [form]
│       └── User Email Confirmation    [email]
│
├── Login                              [page]
│   └── Login                          [form]
│
├── Support                            [page]
│
├── Donation                           [external link]
├── Terms of Use                       [page]
└── Developed by YOU                   [external link]
```
## Authenticated pages:
```
ProductMainDomain.com
├── Catalog (logged home)                              [page]
│   └── Aircraft (specific one) ...                    [pages]
│       └── Model ...                                  [pages]
│           └── Procedure by user ...                  [pages]
│               ├── User is not the author             [logical context]
│               │   └── Report this procedure          [page]
│               │       └── Reporting                  [form]
│               │           └── Email of report        [email]
│               │
│               └── User is the author                 [logical context]
│                   └── Edit procedure                 [page]
│                       └── Editing                    [form]
│
├── Create procedure                      [page]
│   └── Adding                            [form]
│
├── Profile                               [page]
│   ├── Viewing another profile           [logical context]
│   │   └── Report this user              [page]
│   │       └── Reporting                 [form]
│   │           └── Email of report       [email]
│   │
│   └── Viewing their own profile         [logical context]
│   ├── Edit profile                      [page]
│   │   ├── Editing                       [form]
│   │   │
│   │   ├── Change password               [page]
│   │   │   └── Changing                  [form]
│   │   │
│   │   └── Change email                   [page]
│   │       └── Changing                   [form]
│   │
│   └── Delete account                     [page]
│       └── Requesting                     [form]
│
├── Support                                [page]
│
├── Donation                               [external link]
├── Terms of Use                           [page]
└── Developed by YOU                       [external link]
```
## Shared system pages:
```
ProductMainDomain.com
├── Login Back-end CMS                   [hidden page]
│   └── ...                              [hidden pages]
│
├── E-mail successfully confirmed        [page]
├── Password forgotten                   [page]
│   └── Confirming email                 [form]
│       └── Email password reset         [email]
│
├── Access denied (403)                  [page]
└── Not found (404)                      [page]
```
## Navigation menus:

**Main menu**
```
Links for visitor:
- Create account (visitor home)    [link]
- Login                            [link]

Links for logged user:
- Catalog (logged home)            [link]
- Profile                          [link]

Link for both:
- Support                          [link]
- Donation                         [external link]
```

**Footer menu**
```
- Terms of Use                     [link]
- Developed by You                 [external link]
```

**Screen base menu**
```
Logged, only in Catalog:
- Create procedure                [link]
- My stuff                        [link]

Logged, only in user's own profile:
- Back                            [link]
- Catalog                         [link]
- Create procedure                [link]
```

