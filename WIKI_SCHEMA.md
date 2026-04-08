# WIKI_SCHEMA.md — LLM Wiki Schema

This file defines conventions for maintaining the LLM Wiki in this repository.
Based on Andrej Karpathy's "LLM Wiki" pattern.

## Architecture

```
raw/            <- Immutable source documents (articles, papers, notes, images)
raw/assets/     <- Downloaded images referenced by sources
wiki/           <- LLM-generated markdown pages (summaries, entities, concepts)
wiki/index.md   <- Content catalog — updated on every ingest
wiki/log.md     <- Append-only chronological record
WIKI_SCHEMA.md  <- This file (schema & conventions)
```

## Page Types

### Source Summary (`wiki/src_<slug>.md`)
One per ingested source. Contains:
- YAML frontmatter: `title`, `date_ingested`, `source_type`, `tags`
- Key takeaways (bullet list)
- Detailed summary
- Links to related entity/concept pages

### Entity Page (`wiki/entity_<name>.md`)
One per notable person, organization, tool, or project.
- YAML frontmatter: `name`, `type`, `tags`
- Description, key facts
- Cross-references to sources and concepts

### Concept Page (`wiki/concept_<name>.md`)
One per important idea, technique, or theme.
- YAML frontmatter: `concept`, `tags`
- Explanation
- Cross-references, comparisons

### Analysis Page (`wiki/analysis_<slug>.md`)
Filed from valuable query results — comparisons, syntheses, insights.
- YAML frontmatter: `question`, `date`, `tags`
- The analysis content
- Sources cited

## Workflows

### Ingest (process a new source)

1. Read the source document in `raw/`.
2. Discuss key takeaways with the user.
3. Create `wiki/src_<slug>.md` with summary.
4. Create or update relevant entity and concept pages.
5. Update `wiki/index.md` with new/changed pages.
6. Append entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <Title>`

### Query (answer a question)

1. Read `wiki/index.md` to find relevant pages.
2. Read those pages, synthesize an answer.
3. If the answer is valuable, file it as `wiki/analysis_<slug>.md`.
4. Update index and log.

### Lint (health check)

1. Scan all wiki pages for:
   - Contradictions between pages
   - Orphan pages (no inbound links)
   - Important concepts mentioned but lacking own page
   - Missing cross-references
   - Stale claims superseded by newer sources
2. Report findings and suggest fixes.
3. Log the lint pass.

## Conventions

- Use `[[page_name]]` for internal wiki links (Obsidian-compatible).
- Filenames: lowercase, underscores, no spaces.
- All dates in ISO format (YYYY-MM-DD).
- Tags in frontmatter as YAML lists.
- The LLM owns all files in `wiki/`. The user owns `raw/` and this schema.
- Source files in `raw/` are never modified by the LLM.

## Log Format

Each log entry starts with: `## [YYYY-MM-DD] <operation> | <title>`
Operations: `ingest`, `query`, `lint`, `update`, `init`
This makes the log grep-friendly: `grep "^## \[" wiki/log.md | tail -5`
