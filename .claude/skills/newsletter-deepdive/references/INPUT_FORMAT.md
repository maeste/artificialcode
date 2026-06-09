# Input Format for Links File

The input markdown file contains the collected links for the week. These are the same links used in the roundup format, organized by category or as a flat list.

## Accepted Formats

### Format A: Categorized (same as roundup skill)
```markdown
# [Titolo Documento]

## [Nome Categoria 1]

### [Titolo Link 1](URL_pulito)
Descrizione del link...

### [Titolo Link 2](URL_pulito)
Descrizione del link...

## [Nome Categoria 2]

### [Titolo Link 3](URL_pulito)
Descrizione del link...
```

### Format B: Flat list
```markdown
# Link della settimana

### [Titolo Link 1](URL_pulito)
Descrizione del link...

### [Titolo Link 2](URL_pulito)
Descrizione del link...
```

## Requirements
- Links should already be clean (no UTM parameters, no redirects)
- Each link should have at least a brief description
- Both categorized and flat formats are accepted; the skill will present all links as a numbered flat list regardless of input format
