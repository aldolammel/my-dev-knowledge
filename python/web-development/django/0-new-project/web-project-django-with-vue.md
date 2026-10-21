#### Python > Django > Project types
# Django as back-end + Vue as front-end

---

Below, you find a roadmap with all crucial responsibilities that might orbit a developer in the project (depends too much about your role and company).

---
## Before:
1. [x] To read: *Software Requirements Specification* (SRS) document.
2. [x] To read: [Technical Design Document (TDD)](/python/web-development/django/document-templates/tdd.md) document.
3. [x] To read: project [System ERD](/database/document-templates/erd.md) document.
4. [x] To read: project *Sitemap* document.
## 1) Setup:

### 1.1) Database
1. [x] What db should be used: [/database/principles-pacelc](/database/principles-pacelc.md)
### 1.2) Back-end
1. [x] Django install options: [/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup](/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup.md)
### 1.3) Front-end
If you are not responsible for this, just ignore it. If you see the possibility to make it later to put your focus into the back-end, go ahead, skip it for now.
1. [ ] IDE, framework setup:  [VSCode for Vue](/javascript/web-development/frontend/vue/ide/vscode/basic-for-vue.md) or [PyCharm for Vue](/javascript/web-development/frontend/vue/ide/pycharm/basic-for-vue.md).
2. [ ] Vue installation (and its dependencies): [0-vue-installation-and-setup](/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)
3. [ ] (Optional) CSS Framework: [Vuetify](/web-development/frontend/css/css-libraries-frameworks/vuetify/_about.md) or [Bootstrap](web-development/frontend/css/css-libraries-frameworks/bootstrap/_about-and-installation.md) or [Tailwind](/web-development/frontend/css/css-libraries-frameworks/tailwind/install-and-integration.md) or  [Bulma](/web-development/frontend/css/css-libraries-frameworks/bulma/_about.md).

---
## 2) Development:

### 2.1) Before
1. [ ] Create the AI assistance basic instruction (context prompt) for the project: [python/web-development/django/document-templates/ai-prompt-context-model](python/web-development/django/document-templates/ai-prompt-context-model.md)
### 2.2) Non-stop control:
1. Update *Project Dashboard*.
2. Update *Technical Design Document* (TDD).
3. Create and keep updating [Django Architecture Design](/python/web-development/django/document-templates/django-architecture-design.md) document.
### 2.3) Front-end
1. [ ] Convert the HTML template to Vue templates/components;
2. [ ] Code the entire navigation;
3. [ ]  Integrate back-end with front-end: [/python/web-development/django/4-cms-admin/2-frontend-integration/with-vue/\_integration-using-pagex](_integration-using-pagex.md)
### 2.4) Back-end
1. [ ] Build up the main classes from *Django Architecture Design* document:
	- List of model class templates:  [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)
		- List of field classes for your classes: [/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)
	- List of admin class templates: [/python/web-development/django/4-cms-admin/\_admin-class-model.py](/python/web-development/django/4-cms-admin/_admin-class-model.py)
2. [ ] (If applicable) Multi-step adding detail-view or similar: [/python/web-development/django/4-cms-admin/\_what-kind-of-cms-ux-do-you-need](/python/web-development/django/4-cms-admin/_what-kind-of-cms-ux-do-you-need.md)
3. [ ] Develop and test validations for each model (app-level + db-level): [/python/web-development/django/6-errors-and-validations/1-validation-basic](/python/web-development/django/6-errors-and-validations/1-validation-basic.md)
4. [ ] (If applicable) If not yet, complete the translation roadmap: [/python/web-development/django/8-translate-and-internationalization/1-starting-translation](/python/web-development/django/8-translate-and-internationalization/1-starting-translation.md)
### 2.5) Final touches
1. [ ] Back-end > xxxx
2. [ ] Back-end > xxxx
3. [ ] Front-end > xxxx
4. [ ] Front-end > xxxx

---
## 3) Deployment:

### Before
1. [ ] Check the deployment heads-up: [/python/web-development/django/15-deployment/\_about](/python/web-development/django/15-deployment/_about.md)
### 3.1) Xxxxxx
1. [ ] xxxxxxxxxxxxxxxxxxxxxx
2. [ ] xxxxxxxxxxxxxxxxxxxxx
### 3.X) Archiving
1. [ ] Update the *Software Requirements Specification* (SRS) document.
2. [ ] Update the *Entity-Relationships Diagram* (ERD).
3. [ ] Update the *Sitemap* diagram.
4. [ ] Make sure all those **Non-stop control** steps were updated.

---
