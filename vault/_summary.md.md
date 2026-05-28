# Summary

Before:

1. [What is this repo](https://github.com/aldolammel/my-dev-knowledge/blob/main/README.md)

Here below you find NOT the entire content, but a few examples of you can find. After a while browsing it, you'll be able to find lot of useful programming knowledge. Use your IDE finder tool to search specific stuff.

## Web development projects

- Back-end:
	- **Django** project:
		- Discovery: [[python/web-development/django/0-new-project/discovery-django]]
		- API: [[python/web-development/django/0-new-project/api]]
		- Update Django: [[python/web-development/django/0-new-project/update-django-version]]
		- App pure Django: [[python/web-development/django/0-new-project/web-project-django-only]]
		- App Django with Vue: [[python/web-development/django/0-new-project/web-project-django-with-vue]]
	- **Flask** project:
	    - API: [[python/web-development/flask/0-new-project/api]]
	    - App pure Flask: [[python/web-development/flask/0-new-project/web-project-flask-only]]
	    - App Flask with Vue: [[python/web-development/flask/0-new-project/web-project-flask-with-vue]]
	- **Node.js** project:
	    - Update Node: [[javascript/NodeJS/2-updating]]
- Front-end:
	- **Vue.js** project:
		- Update Vue: [[javascript/Web-development/frontend/Vue/2-updating-removing/updating-vue]]
		- App Vue with Django: [[python/web-development/django/0-new-project/web-project-django-with-vue]]
		- App Vue with Flask: [[python/web-development/flask/0-new-project/web-project-flask-with-vue]]

## Programming languages

- **Python**
	- What is it: [[python/_about]]
	- Installing: [[python/1-python-installation/_install]]
	- Updating Python: [[python/0-new-project/3-update-python-version-in-a-project]]
	- Updating a module/library: [[python/2-updating/updating-a-library]]
- **JavaScript**
	- What is it: [[javascript/_about]]

## Database

- Choosing a database (PACELC): [[database/principles-pacelc]]
	- **PostgreSQL**:
		- Why not: [[database/PostgreSQL/0-basic/0-why-not]]
		- Installing and integrating:
			- For Python project: [[python/web-development/django/3-1-models-database/0-installing-and-adminUser/PostgreSQL/installation]]
		- Starting and stopping the service: [[database/PostgreSQL/0-basic/starting-and-stopping]]
		- Updating: [[database/PostgreSQL/0-basic/updating]]
	- **SQLite**:
		- Installing and integrating:
			- For Python project: [[python/web-development/django/3-1-models-database/0-installing-and-adminUser/SQLite/installation]]

## Environment Variables

- What is it: [[environment-variables/_about]]
- .env for **local** development:
	- In back-end, example: [[vault/environment-variables/env-for-local/in-backend/.env]]
	- In front-end, example: [[vault/environment-variables/env-for-local/in-frontend/.env]]
- .env for **cloud** development:
	- In back-end, example: [[vault/environment-variables/env-for-cloud/in-backend/.env]]
	- In front-end, example: [[vault/environment-variables/env-for-cloud/in-frontend/.env]]
- Using env vars:
	- With Django: [[python/web-development/django/3-1-models-database/env-vars-on-django]]
	- With Vue: [[vault/javascript/Web-development/frontend/Vue/z-example-structure/aldolammel-style/project_root/frontend/src/utils/env.js]]

## Server

- Building up a Linux VPS: [[server/os/linux/_building-and-installing-a-server]]
- Updating server itself: [[server/os/linux/updating-server]]
- Updating web-app on server (using Git): [[server/os/linux/updating-web-app-via-git]]

## IDE

- VSCode
	- What is it and how it works: [[ide/vscode/_vscode-knowledge]]
	- Config files:
		- settings.json example: [[vault/ide/vscode/examples/.vscode/settings.json]]
		- extensions.json example: [[vault/ide/vscode/examples/.vscode/extensions.json]]

## Code quality

- Principles:
	- DRY: [[dev-concepts/principles-dry]]
- Tools: 
	- Formatter: [[dev-concepts/tool-formatter]]
	- Linter: [[dev-concepts/tool-linter]]
	- Type Checker: [[dev-concepts/tool-typechecker]]

## Versioning

- Git
	- How it works and basic commands: [[versioning/git/_basic]]
	- Git ignore (.gitignore) file: [[versioning/git/gitignore-file]]
  - Installing:
    - Install: [[versioning/git/_basic]]
    - Re-install in an existing project: [[versioning/git/re-install-git-folder-in-an-existent-local-project]]

## Operational Systems

- Linux:
	- Terminal basic commands: [[os/linux/terminal-basic-commands]]
		- (Any Linux distro) Formatting the system and installing it: [[os/linux/0-os-install/_roadmap]]
	- Distros:
		- **Debian**/**Ubuntu**:
			- Installing apps: [[os/linux/distros/debian/1-apps-install/1-installing-apps]]
			- Installed apps list: [[os/linux/distros/debian/1-apps-install/finding-installed-apps]]
			- Checking OS repo list: [[os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list]]
		- **Fedora**:
			- Installing apps: [[os/linux/distros/fedora/1-apps-install/1-installing-apps]]
			- Installed apps list: [[os/linux/distros/fedora/1-apps-install/finding-installed-apps]]
			- Checking the OS repo list: [[os/linux/distros/fedora/1-apps-install/checking-app-is-in-repo-list]]
- Windows:
	- Formatting the system and installing it: [[os/windows/0-os-install/_roadmap]]
