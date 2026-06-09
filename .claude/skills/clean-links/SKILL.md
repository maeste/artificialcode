---
name: clean-links
description: Cleans and synthesizes links from markdown documents for the codiceartificiale newsletter. Removes UTM parameters, resolves redirects, and generates concise descriptions in Italian. Defaults to thisweek_links.md as input and thisweek_links_clean.md as output. Use when user mentions "pulisci i link", "clean links", "normalizza per newsletter", or has a document with links that needs processing.
metadata:
  author: codiceartificiale
  version: "2.0"
---

# Clean Links Skill

You are a link cleaning and organization specialist for the "codiceartificiale" newsletter.

## Trigger Phrases
- "pulisci i link" / "clean the links"
- "elimina redirect" / "remove redirects"
- "normalizza per newsletter" / "normalize for newsletter"
- "documento con link" / "document with links"
- "versione pulita dei link" / "clean version of links"

## Task Instructions

### Step 0: Input/Output Validation (Defaults)

**Default input**: `thisweek_links.md`
**Default output**: `thisweek_links_clean.md`

Behavior:
- **If the user already expressed they want to use the defaults** when launching the skill (e.g. "usa i default", "use defaults", "con i default", "vai con i default"), **skip this validation step** and proceed directly with `thisweek_links.md` → `thisweek_links_clean.md`.
- **If the user provided an explicit input and/or output file**, use what they specified (no confirmation needed).
- **Otherwise**, propose the defaults and ask for confirmation, e.g.:

  > "Uso `thisweek_links.md` come input e `thisweek_links_clean.md` come output. Confermi o preferisci altri file?"

  Wait for the user's answer before proceeding.

### Step 1: Read and Analyze Input
1. Read the resolved input markdown file
2. Extract all links from the document
3. Preserve the relevant original text content (titles, descriptions)

### Step 2: Link Cleaning
For each link found:
1. **Remove UTM parameters**: Strip utm_source, utm_medium, utm_campaign, utm_content, utm_term
2. **Resolve redirects**: Follow all redirects to get the final destination URL
3. **Clean beehiiv links**: If link contains `https://link.mail.beehiiv.com`, resolve to direct URL
4. **Track failed links**: If any link cannot be resolved, log it with reason

### Step 3: Description Synthesis (in Italian)
For each link, produce a concise, clean description **in Italian**:
- Read the page content (resolved URL) to ground the description on what the page actually says
- Write a synthetic description in Italian, typically 40-80 words, capturing the key point of the resource
- If the original description is already in Italian and adequate, you may keep or lightly refine it; otherwise translate/synthesize from the content
- Never invent content: base everything on the actual page or the original text
- Preserve the link title (translate to Italian only if it improves clarity; keep product/proper names as-is)

### Step 4: Output Structure — NO Categories by Default
By default, **do NOT group links into thematic categories**. Output a single flat list of cleaned links with their synthesized Italian descriptions, preserving the input order.

**Only if the user explicitly requests categorization** (e.g. "raggruppa per categorie", "organizza per temi", "group by category"), then:
1. Propose these 5 default categories (or use the ones the user provides):
   1. **Novità e ricerca nei modelli AI** - Nuovi modelli, paper di ricerca, architetture innovative
   2. **Agentic AI** - Agenti autonomi, sistemi multi-agente, orchestrazione
   3. **AI Assisted Coding** - Strumenti di sviluppo assistito, copilot, refactoring AI
   4. **Business e società** - Impatto sociale, regolamentazione, mercato del lavoro
   5. **Robotica e Physical AI** - Robotica, computer vision, embodied AI
2. Ask: "Confermi queste categorie o preferisci fornirne di diverse?"
3. Categorize each link and sort by relevance within each category

### Step 5: Output Generation
Write the resolved output file (default `thisweek_links_clean.md`).

See [references/OUTPUT_FORMAT.md](references/OUTPUT_FORMAT.md) for the complete output structure (flat by default, categorized only on request).

## Important Rules

1. **Defaults**: input `thisweek_links.md`, output `thisweek_links_clean.md`. Validate first unless the user opted for defaults.
2. **Italian descriptions**: All synthesized descriptions must be in Italian, concise and clean.
3. **No categories by default**: Output a flat list; only categorize on explicit user request.
4. **Always access link content** to ground descriptions (web reader / fetch tool).
5. **Never invent content**: Base all descriptions on actual page content or original text.
6. **Resolve ALL redirects**: Ensure final URLs are direct links (decode `tracking.tldrnewsletter.com`, etc.).
7. **Clean beehiiv links**: Always resolve `link.mail.beehiiv.com` to destination.
8. **Remove UTM parameters**: Strip `utm_*` from every URL.
9. **Track failures**: List any links that could not be processed.
10. **Generate artifact**: Always create the output markdown file.

## Tool Selection

- **Link resolution**: web_reader MCP (for content extraction and redirect following)
- **Content fetching**: web_reader MCP
- **File operations**: Native Read/Write tools
- **Web search**: WebSearch for additional context if needed

## Error Handling

If a link cannot be processed:
1. Log the original URL
2. Document the specific error (timeout, 404, redirect loop, etc.)
3. Include in "Link Non Processati" section of output
4. Continue processing remaining links

## Example Workflow

```yaml
Launch: "pulisci i link con i default"

Step 0: Defaults requested → skip validation
  → Input: thisweek_links.md
  → Output: thisweek_links_clean.md

Step 1: Read file
  → Extract: 6 links found

Step 2: Clean each link
  → Remove: ?utm_source=tldrai
  → Decode: https://tracking.tldrnewsletter.com/CL0/... → direct URL
  → Resolve: https://link.mail.beehiiv.com/... → destination
  → Result: 6 clean direct URLs

Step 3: Synthesize descriptions in Italian
  → Fetch content per link
  → Write 40-80 word concise Italian descriptions

Step 4: Output structure
  → No categorization (default) → flat list, input order preserved

Step 5: Generate output
  → Write: thisweek_links_clean.md
  → Format: See references/OUTPUT_FORMAT.md
  → Include: "Link Non Processati" section if any failed
```

```yaml
Launch: "pulisci i link"   # no defaults stated, no files given

Step 0: Ask confirmation
  → "Uso thisweek_links.md come input e thisweek_links_clean.md come output. Confermi?"
  → Proceed after user answer
... (continue as above)
```
