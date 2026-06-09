# Clean Links Output Format

The output file (default `thisweek_links_clean.md`) is a **flat list** of cleaned links with concise Italian descriptions, preserving the input order. Categorization is applied **only when the user explicitly requests it**.

## Default Format (flat, no categories)

```markdown
### [Link Title](clean_url)

Descrizione sintetica in italiano (circa 40-80 parole) basata sul contenuto reale della pagina...

---

### [Link Title 2](clean_url)

Descrizione sintetica in italiano...

---

## Note di processamento

- Eventuali note su redirect decodificati, parametri rimossi, descrizioni arricchite via fetch, ecc.

## Link Non Processati

Elenca i link che non è stato possibile processare con la relativa ragione:
- `[original_url]` - Motivo dell'esclusione (timeout, 404, redirect loop, ecc.)

Se nessun link è stato escluso, indicarlo esplicitamente.
```

## Categorized Format (only on explicit request)

```markdown
## 📚 [Category 1 Name]

*Breve descrizione di cosa copre questa categoria*

### [Link Title 1](clean_url)
Descrizione sintetica in italiano...

### [Link Title 2](clean_url)
Descrizione sintetica in italiano...

## 🔧 [Category 2 Name]

*Breve descrizione*

### [Link Title 3](clean_url)
Descrizione sintetica in italiano...

[... continue for all categories ...]

---

## Link Non Processati
- `[original_url]` - Motivo dell'esclusione
```

## Notes
- All URLs must be clean (no UTM parameters, no redirects, no tracking wrappers)
- Descriptions are written in **Italian**, concise (≈40-80 words)
- Input order is preserved in the default flat format
- Categories are used only when the user explicitly asks for them
- Always include a "Link Non Processati" section (state explicitly if empty)
