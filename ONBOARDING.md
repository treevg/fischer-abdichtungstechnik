# Team-Onboarding: Horizontalsperren Landingpage

Dieses Dokument enthält den Entwurf für die Onboarding-E-Mail an das Team sowie die Anleitung zum lokalen Einrichten des Projekts mit VS Code und GitHub.

---

### 📧 E-Mail-Entwurf für Kollegen

**Betreff:** 🚀 Onboarding: Neue Landingpage "Horizontalsperre" online & bereit zur Entwicklung!

Hallo zusammen,

wir haben die neue, conversion-optimierte Landingpage zur Bewerbung von **Horizontalsperren** aufgesetzt! Die Seite basiert auf dem Design von *fischer-abdichtungstechnik.de*, lädt dank maßgeschneiderter Vektorgrafiken (SVGs) extrem schnell und ist vollständig responsiv.

Um direkt in die Entwicklung oder Pflege der Seite einzusteigen, haben wir hier einen schnellen Onboarding-Leitfaden für euch zusammengestellt.

---

#### 🛠️ 1. Voraussetzungen & Tools installieren

1. **Code-Editor:** Wir verwenden **VS Code**. Falls noch nicht installiert, kannst du es hier herunterladen:
   👉 [VS Code herunterladen](https://code.visualstudio.com/)
2. **VS Code Erweiterung:** Für die lokale Vorschau mit automatischem Neuladen (Live Reload) empfehlen wir die Extension **Live Server**:
   👉 [Live Server Extension installieren](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
3. **Versionskontrolle:** Wir nutzen **GitHub** zum Hosten des Codes. Stelle sicher, dass Git installiert ist und du Zugriff auf das Repo hast.

---

#### 📥 2. Projekt klonen & einrichten

Öffne dein Terminal und führe folgende Befehle aus:

```bash
# 1. Repository von GitHub klonen (Ersetze [ORGA/REPO] mit dem tatsächlichen Link)
git clone https://github.com/[ORGA/REPO]/my-test-website.git

# 2. In den Projektordner wechseln
cd my-test-website

# 3. Projekt direkt in VS Code öffnen
code .
```

---

#### 🖥️ 3. Lokalen Server starten & testen

1. Öffne die Datei **`index.html`** in VS Code.
2. Klicke unten rechts in der Statusleiste auf **"Go Live"** oder mache einen Rechtsklick in der Datei und wähle **"Open with Live Server"**.
3. Die Seite öffnet sich automatisch in deinem Browser unter `http://127.0.0.1:5500`.

---

#### 🔍 4. Code validieren (Qualitätssicherung)

Wir haben ein automatisiertes Python-Skript integriert, das die Integrität aller Pfade und Links prüft. Führe dieses vor jedem Commit lokal aus:

```bash
python3 verify_site.py
```

---

#### 📁 Projektstruktur im Überblick

* `index.html` – Hauptseite mit modernsten interaktiven SVGs (keine schweren externen Bilddateien).
* `styles.css` – Globales Stylesheet (Montserrat + Open Sans, voll responsiv).
* `impressum.html` / `datenschutz.html` – Gesetzlich vorgeschriebene Unterseiten.
* `verify_site.py` – Unser Validierungsskript für fehlerfreie Verlinkung.

---

#### 📈 5. Google Analytics 4 (GA4) & Google Ads konfigurieren

Die Seite ist für Tracking-Dienste optimiert und erfasst erfolgreiche Kontaktanfragen als Conversions (Google Ads) und standardisierte Leads (GA4). Vor dem Live-Gang müssen folgende Platzhalter in **`index.html`** ersetzt werden:

1. **Einheitlicher Google-Tag (`<head>`-Bereich):**
   - Suche nach `G-XXXXXXXXXX` und ersetze es an zwei Stellen durch deine **GA4 Mess-ID** (z. B. `G-1A2B3C4D5E`).
   - Suche nach `AW-XXXXXXXXX` und ersetze es durch deine **Google Ads Conversion-ID** (z. B. `AW-987654321`).
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-DEINE_GA4_MESS_ID"></script>
   <script>
       ...
       // GA4 Initialisierung
       gtag('config', 'G-DEINE_GA4_MESS_ID');

       // Google Ads Initialisierung
       gtag('config', 'AW-DEINE_ADS_ID');
   </script>
   ```
2. **Google Ads Conversion Event (`handleFormSubmit`-Funktion):**
   Suche im `<script>`-Bereich nach `AW-XXXXXXXXX/YYYYYYYYYYYYYYYY` und ersetze es mit deiner Google Ads ID und dem dazugehörigen Label (z. B. `AW-987654321/AbCDeF_GhIjKlMnOpQr`):
   ```javascript
   gtag('event', 'conversion', {
       'send_to': 'AW-DEINE_ADS_ID/DEIN_CONVERSION_LABEL'
   });
   ```
3. **Google Analytics 4 Lead Event (`handleFormSubmit`-Funktion):**
   Das Standard-Event `generate_lead` wird automatisch an Google Analytics gesendet und kann dort direkt als Conversion markiert werden. Keine manuelle Anpassung erforderlich!

---

Bei Fragen oder Feedback zum Setup meldet euch gerne direkt bei mir!

Viele Grüße,  
[Dein Name]
