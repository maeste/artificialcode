# Output Format for Deep-Dive Newsletter

The assembled newsletter follows this structure. All sections are separated by horizontal rules where indicated.

## Complete Document Structure

```markdown
# [Titolo della newsletter]

🔗 Scopri di più su di me, sul mio lavoro e su come restare in contatto: [maeste.it](https://maeste.it): biografia personale, progetti e link ai social.

[Testo introduttivo - paragrafo editoriale che inquadra il tema del numero]

### La mia agenda

[Contenuto agenda: podcast, eventi, progetti]

---

## [Titolo della sezione Deep-Dive]

[Contenuto dell'approfondimento - articolo completo]

---

## I link che mi hanno colpito questa settimana

### [Titolo Link 1](URL)
[Punto di vista dell'autore]

### [Titolo Link 2](URL)
[Punto di vista dell'autore]

...
```

The bio link line is fixed and verbatim: do NOT rephrase or restyle it.

## Links Section Variants

### Variant A: POV Only
When the user chooses to include only their personal commentary:

```markdown
### [Titolo Link](URL)
[Punto di vista dell'autore - cosa lo ha colpito di questo link]
```

### Variant B: POV + Brief Description
When the user chooses to include a factual description alongside their commentary:

```markdown
### [Titolo Link](URL)
*[Descrizione breve fattuale - max 20-30 parole]*

[Punto di vista dell'autore - cosa lo ha colpito di questo link]
```

## English Version Structure

The English translation follows the same structure with translated headers:

```markdown
# [Newsletter title]

🔗 Learn more about me, my work and how to stay in touch: [maeste.it](https://maeste.it): personal bio, projects and social links.

[Introduction paragraph]

### My agenda

[Agenda content]

---

## [Deep-dive section title]

[Deep-dive content]

---

## Links that caught my attention this week

### [Link Title](URL)
[Author's point of view]

...
```

The bio link line is fixed and verbatim: do NOT rephrase or restyle it.

## Notes
- The H1 title is the shareable newsletter title crafted in Step 7
- The deep-dive H2 title is specific to the article topic (chosen by the user)
- Exactly 2 horizontal rules (`---`) separate the 3 main content blocks
- All links must be properly formatted as clickable markdown links
- No em dashes anywhere in the document; use commas or parentheses
