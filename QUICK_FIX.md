# ⚡ QUICK FIX: Tom Side på GitHub Pages

## 🔴 PROBLEMET

Din side på https://golfklubb-it.github.io/ er TOM fordi:

```
GitHub Pages innstillinger er FEIL:
❌ Branch: copilot/create-github-pages-overview
❌ Folder: /docs
```

## ✅ LØSNINGEN (2 Steg)

### Steg 1: MERGE PR
```
https://github.com/Golfklubb-IT/golfklubb-it.github.io/pulls
→ Klikk "Merge pull request"
→ Klikk "Confirm merge"
```

### Steg 2: FIX INNSTILLINGER
```
https://github.com/Golfklubb-IT/golfklubb-it.github.io/settings/pages

Endre til:
✅ Branch: main (ikke PR-branchen!)
✅ Folder: / (root) (ikke /docs!)

→ Klikk "Save"
→ Vent 2-3 minutter
```

### Steg 3: SE RESULTATET
```
https://golfklubb-it.github.io/
→ Skal vise 13 repositories med beskrivelser
→ Golf-tema med grønn design
```

---

## 📸 VISUELL GUIDE

### FEIL INNSTILLINGER (nå):
```
┌─────────────────────────────────────┐
│ Build and deployment                │
│                                     │
│ Source                              │
│ ▼ Deploy from a branch              │
│                                     │
│ Branch                              │
│ ▼ copilot/create-github...  ❌     │
│ ▼ /docs  ❌                         │
│                                     │
│ [Save]                              │
└─────────────────────────────────────┘

RESULTAT: Tom side (404)
```

### RIKTIGE INNSTILLINGER:
```
┌─────────────────────────────────────┐
│ Build and deployment                │
│                                     │
│ Source                              │
│ ▼ Deploy from a branch              │
│                                     │
│ Branch                              │
│ ▼ main  ✅                          │
│ ▼ / (root)  ✅                      │
│                                     │
│ [Save]                              │
└─────────────────────────────────────┘

RESULTAT: Full side med 13 repositories! 🎉
```

---

## ❓ HVORFOR ER DETTE FEIL?

### Problem 1: Feil Branch
```
copilot/create-github-pages-overview = PR branch
→ Innhold er ikke merget ennå
→ Ikke den "offisielle" versjonen

main = Hoved-branch
→ Der alt "live" innhold skal være
→ Der index.html må ligge
```

### Problem 2: Feil Folder
```
/docs folder
→ Eksisterer IKKE i vårt repo
→ GitHub finner ingen index.html
→ Tom side!

/ (root) folder
→ Der index.html ligger
→ Der favicon.ico og favicon.svg ligger
→ Alt innhold er her!
```

---

## 🎯 HUSK

1. **MERGE FØRST**, endre innstillinger ETTERPÅ
2. Branch må være `main`
3. Folder må være `/ (root)`
4. Vent 2-3 minutter etter endringer
5. Hard refresh (Ctrl+Shift+R)

---

Les **GITHUB_PAGES_SETUP.md** for full guide!
