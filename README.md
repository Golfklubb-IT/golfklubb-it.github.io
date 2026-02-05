# Golfklubb-IT GitHub Pages Portal 🏌️

Automatisk oppdatert oversiktsside for alle GitHub Pages i Golfklubb-IT-organisasjonen.

## 📋 Beskrivelse

Dette repository inneholder en automatisk generert portal som samler og viser alle aktive GitHub Pages-sider i vår organisasjon på én oversiktlig side.

**Live-side:** [https://golfklubb-it.github.io/](https://golfklubb-it.github.io/)

## 🚀 Hvordan det fungerer

Systemet består av tre hovedkomponenter:

1. **Python-script (`generate_index.py`)**: Henter alle repositories fra GitHub API, tester hver potensielle GitHub Pages-URL, og genererer en moderne HTML-side med oversikten.

2. **GitHub Actions workflow**: Kjører automatisk hver dag kl. 00:00 UTC og kan også trigges manuelt. Workflowen:
   - Henter alle repositories i organisasjonen
   - Sjekker om hver repository har en aktiv GitHub Pages-side
   - Genererer `index.html` med resultatet
   - Committer og pusher endringer automatisk

3. **GitHub Pages**: Publiserer den genererte `index.html` på `https://golfklubb-it.github.io/`

## 🔧 Aktivere GitHub Pages

For at dette repository skal publiseres som GitHub Pages:

1. Gå til **Settings** → **Pages** i dette repository
2. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
3. Klikk **Save**

GitHub Pages vil nå publisere `index.html` fra main branch.

## 🔄 Manuell oppdatering

For å kjøre workflowen manuelt:

1. Gå til **Actions**-fanen i dette repository
2. Velg "Update GitHub Pages Index" i venstre sidepanel
3. Klikk **Run workflow**
4. Velg branch (vanligvis `main`)
5. Klikk **Run workflow**

Workflowen vil kjøre og oppdatere oversikten innen få minutter.

## 📁 Filstruktur

```
.
├── .github/
│   └── workflows/
│       └── update-pages-index.yml  # GitHub Actions workflow
├── generate_index.py               # Python-script for generering
├── requirements.txt                # Python-avhengigheter
├── index.html                      # Generert oversiktsside (auto-generert)
├── .gitignore                      # Git ignore-fil
└── README.md                       # Denne filen
```

## 🎨 Design

Siden har et moderne, responsivt design med:
- Golf-inspirert grønn/hvit fargeprofil
- Kortbasert layout for hver aktiv GitHub Pages-side
- Hover-effekter og animasjoner
- Mobiloptimalisert
- Norsk språk

## 🔍 Hvordan legge til/fjerne sider

Dette skjer **automatisk**! Du trenger ikke gjøre noe manuelt.

### Legge til en ny side:
1. Aktiver GitHub Pages i det aktuelle repository (Settings → Pages)
2. Vent på neste automatiske kjøring (hver dag kl. 00:00 UTC) eller kjør workflow manuelt
3. Siden vil automatisk dukke opp i oversikten

### Fjerne en side:
1. Deaktiver GitHub Pages i det aktuelle repository
2. Vent på neste automatiske kjøring eller kjør workflow manuelt
3. Siden vil automatisk forsvinne fra oversikten

## 🛠️ Vedlikehold

### Tekniske detaljer:
- **Python-versjon**: 3.11
- **Dependencies**: `requests>=2.31.0`
- **Timeout**: 10 sekunder per URL-sjekk
- **Rate limiting**: Håndteres automatisk av GitHub API
- **Feilhåndtering**: Hvis en side ikke svarer, ekskluderes den automatisk

### Feilsøking:

**Hvis oversikten ikke oppdateres:**
1. Sjekk at workflowen kjører uten feil i Actions-fanen
2. Verifiser at GitHub Pages er aktivert i Settings → Pages
3. Sjekk at GITHUB_TOKEN har nødvendige permissions

**Hvis en side ikke vises:**
1. Verifiser at GitHub Pages er aktivert for den aktuelle repository
2. Sjekk at siden er tilgjengelig på `https://golfklubb-it.github.io/[repo-navn]/`
3. Vent på neste automatiske kjøring eller kjør workflow manuelt

## 📝 Lisens

Dette prosjektet er utviklet for Golfklubb-IT organisasjonen.

## 🤝 Bidrag

Har du forbedringsforslag? Opprett en issue eller send en pull request!

---

*Automatisk oppdatert av GitHub Actions* ⚙️
