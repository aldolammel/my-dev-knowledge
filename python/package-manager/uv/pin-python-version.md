#### Python > Package Manager > UV
# Defining which Python version a project must use

---
## 1) Defining a specific version or a range of them:

**Make a choice:**
- 1A) For a specific version only;
- 1B) Accepting multiple versions;

==Info!==
The *uv pin* command will auto-update the *.python-version* file!
### 1A) For just one version accepted
```
uv python pin <python-version>
```
E.g.
```
uv python pin 3.13.9
```
### 1B) For multiple versions accepted
```
uv python pin "<python-version>"
```
E.g.
```
uv python pin ">=3.13,<3.14"
```

---
## 2) Check the current version:
```
uv run python --version
```

---
