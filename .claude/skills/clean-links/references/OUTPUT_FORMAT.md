# Clean Links Output Format

The output file (`{original_name}_clean.md`) follows this structure:

```markdown
# [Original Document Title - Organizzato]

## 📚 [Category 1 Name]

*Breve descrizione di cosa copre questa categoria*

### [Link Title 1](clean_url)
Full description (50-100 words) based on actual page content...

### [Link Title 2](clean_url)
Full description (50-100 words) based on actual page content...

## 🔧 [Category 2 Name]

*Breve descrizione*

### [Link Title 3](clean_url)
Full description (50-100 words)...

[... continue for all categories ...]

---

## Link Non Processati

List any links that could not be processed with reasons:
- `[original_url]` - Reason for exclusion (timeout, 404, redirect loop, etc.)
```

## Notes
- All URLs should be clean (no UTM parameters, no redirects)
- Descriptions should be 50-100 words each
- Categories should match the confirmed categories from Step 4
- Links within each category should be sorted by relevance
- Emoji icons (📚, 🔧, etc.) match the category themes
