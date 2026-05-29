# Summary

Before:

1. [What is this repo](https://github.com/aldolammel/my-dev-knowledge/blob/main/README.md)

Here below you find NOT the entire content, but a few examples of you can find. After a while browsing it, you'll be able to find lot of useful programming knowledge. Use your IDE finder tool to search specific stuff.

## Web development projects

- Back-end:
	- **Django** project:
		- Discovery: [discovery-django](discovery-django.md)
		- API: [python/web-development/django/0-new-project/api](python/web-development/django/0-new-project/api.md)
		- Update Django: [update-django-version](update-django-version.md)
		- App pure Django: [web-project-django-only](web-project-django-only.md)
		- App Django with Vue: [python/web-development/django/0-new-project/web-project-django-with-vue](python/web-development/django/0-new-project/web-project-django-with-vue.md)
	- **Flask** project:
	    - API: [python/web-development/flask/0-new-project/api](python/web-development/flask/0-new-project/api.md)
	    - App pure Flask: [web-project-flask-only](web-project-flask-only.md)
	    - App Flask with Vue: [python/web-development/flask/0-new-project/web-project-flask-with-vue](python/web-development/flask/0-new-project/web-project-flask-with-vue.md)
	- **Node.js** project:
	    - Update Node: [2-updating](2-updating.md)
- Front-end:
	- **Vue.js** project:
		- Update Vue: [updating-vue](updating-vue.md)
		- App Vue with Django: [python/web-development/django/0-new-project/web-project-django-with-vue](python/web-development/django/0-new-project/web-project-django-with-vue.md)
		- App Vue with Flask: [python/web-development/flask/0-new-project/web-project-flask-with-vue](python/web-development/flask/0-new-project/web-project-flask-with-vue.md)

## Programming languages

- **Python**
	- What is it: [python/_about](python/_about.md)
	- Installing: [python/1-python-installation/_install](python/1-python-installation/_install.md)
	- Updating Python: [3-update-python-version-in-a-project](3-update-python-version-in-a-project.md)
	- Updating a module/library: [updating-a-library](updating-a-library.md)
- **JavaScript**
	- What is it: [javascript/_about](javascript/_about.md)

## Database

- Choosing a database (PACELC): [database/principles-pacelc](database/principles-pacelc.md)
	- **PostgreSQL**:
		- Why not: [database/PostgreSQL/0-basic/0-why-not](database/PostgreSQL/0-basic/0-why-not.md)
		- Installing and integrating:
			- For Python project: [python/web-development/django/3-1-models-database/0-installing-and-adminUser/PostgreSQL/installation](python/web-development/django/3-1-models-database/0-installing-and-adminUser/PostgreSQL/installation.md)
		- Starting and stopping the service: [database/PostgreSQL/0-basic/starting-and-stopping](database/PostgreSQL/0-basic/starting-and-stopping.md)
		- Updating: [database/PostgreSQL/0-basic/updating](database/PostgreSQL/0-basic/updating.md)
	- **SQLite**:
		- Installing and integrating:
			- For Python project: [python/web-development/django/3-1-models-database/0-installing-and-adminUser/SQLite/installation](python/web-development/django/3-1-models-database/0-installing-and-adminUser/SQLite/installation.md)

## Environment Variables

- What is it: [environment-variables/_about](environment-variables/_about.md)
- .env for **local** development:
	- In back-end, example: [environment-variables/env-for-local/in-backend/.env](environment-variables/env-for-local/in-backend/.env)
	- In front-end, example: [environment-variables/env-for-local/in-frontend/.env](environment-variables/env-for-local/in-frontend/.env)
- .env for **cloud** development:
	- In back-end, example: [environment-variables/env-for-cloud/in-backend/.env](environment-variables/env-for-cloud/in-backend/.env)
	- In front-end, example: [environment-variables/env-for-cloud/in-frontend/.env](environment-variables/env-for-cloud/in-frontend/.env)
- Using env vars:
	- With Django: [env-vars-on-django](env-vars-on-django.md)
	- With Vue: [javascript/Web-development/frontend/Vue/z-example-structure/aldolammel-style/project_root/frontend/src/utils/env.js](javascript/Web-development/frontend/Vue/z-example-structure/aldolammel-style/project_root/frontend/src/utils/env.js)

## Server

- Building up a Linux VPS: [_building-and-installing-a-server](_building-and-installing-a-server.md)
- Updating server itself: [updating-server](updating-server.md)
- Updating web-app on server (using Git): [updating-web-app-via-git](updating-web-app-via-git.md)

## IDE

- VSCode
	- What is it and how it works: [_vscode-knowledge](_vscode-knowledge.md)
	- Config files:
		- settings.json example: [ide/vscode/examples/.vscode/settings.json](ide/vscode/examples/.vscode/settings.json)
		- extensions.json example: [ide/vscode/examples/.vscode/extensions.json](ide/vscode/examples/.vscode/extensions.json)

## Code quality

- Principles:
	- DRY: [principles-dry](principles-dry.md)
- Tools: 
	- Formatter: [tool-formatter](tool-formatter.md)
	- Linter: [tool-linter](tool-linter.md)
	- Type Checker: [tool-typechecker](tool-typechecker.md)

## Versioning

- Git
	- How it works and basic commands: [versioning/git/_basic](versioning/git/_basic.md)
	- Git ignore (.gitignore) file: [gitignore-file](gitignore-file.md)
  - Installing:
    - Install: [versioning/git/_basic](versioning/git/_basic.md)
    - Re-install in an existing project: [re-install-git-folder-in-an-existent-local-project](re-install-git-folder-in-an-existent-local-project.md)

## Operational Systems

- Linux:
	- Terminal basic commands: [os/linux/terminal-basic-commands](os/linux/terminal-basic-commands.md)
		- (Any Linux distro) Formatting the system and installing it: [os/linux/0-os-install/_roadmap](os/linux/0-os-install/_roadmap.md)
	- Distros:
		- **Debian**/**Ubuntu**:
			- Installing apps: [os/linux/distros/debian/1-apps-install/1-installing-apps](os/linux/distros/debian/1-apps-install/1-installing-apps.md)
			- Installed apps list: [os/linux/distros/debian/1-apps-install/finding-installed-apps](os/linux/distros/debian/1-apps-install/finding-installed-apps.md)
			- Checking OS repo list: [os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list](os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list.md)
		- **Fedora**:
			- Installing apps: [os/linux/distros/fedora/1-apps-install/1-installing-apps](os/linux/distros/fedora/1-apps-install/1-installing-apps.md)
			- Installed apps list: [os/linux/distros/fedora/1-apps-install/finding-installed-apps](os/linux/distros/fedora/1-apps-install/finding-installed-apps.md)
			- Checking the OS repo list: [os/linux/distros/fedora/1-apps-install/checking-app-is-in-repo-list](os/linux/distros/fedora/1-apps-install/checking-app-is-in-repo-list.md)
- Windows:
	- Formatting the system and installing it: [os/windows/0-os-install/_roadmap](os/windows/0-os-install/_roadmap.md)
