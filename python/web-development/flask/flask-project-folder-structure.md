#### Python > Flask > Structure
# Files & Folder Structure

---

Unlike Django, Flask has a absolutely freestyle project folder structure! Here is what I like:

---
### A) Flask as ENTIRE solution for back and front-end
```python
my_project_name/
├── .agents/                     # Critical context documents and/or instructions to help you with AI assistance.
│   ├── architecture-design.md   # Where the basic Flask architecture design is written during the development.
│   └── instructions.md          # Basic instruction of this system for AI assistance.
│
├── .venv/                       # Virtual env folder where Django things are installed.
│
├── instance/                        # xxxxxx.
│   └── product_database.db          # xxxxxxxx.
│
├── static/                # xxxxx
│   ├── css/               # xxxxx
│   ├── favico/               # xxxxx
│   ├── img/               # xxxxx
│   ├── js/                # xxxxx
│   └── vendor/              # xxxxx
│
├── templates/               # Templates.
│   ├── base_site.html         # xxxxx
│   ├── inc_footer.html         # xxxxx
│   ├── inc_header.html         # xxxxx
│   ├── index.html         # xxxxx
│   └── ...
│
├── .env                   # Exclusive back-end environment variables.
├── .gitignore             # For Git repository untrack specific files and folders.
├── .python-version        # xxxxxxxxxxxxxx
├── manage.py              # Command-line utility for Django core.
└── pyproject.toml         # List of all Django project's (backend) dependencies.
```

---
