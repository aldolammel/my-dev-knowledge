#### Python > Package Manager > UV
# Defining which Python version a project must use


==Info!==
The *pin* command will auto-update the *.python-version* file.


---

## 1) Make a choice:
- 1A) For a specific version only;
- 1B) Accepting multiple versions;

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
uv python pin "<python-version>"         <-- between quotes
```
E.g.
```
uv python pin ">=3.13,<3.14"             <-- need to test!!!!!
```


---
