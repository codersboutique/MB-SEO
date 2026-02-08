# Research/Article Template

Use this template for blog posts, research articles, and intelligence pieces.

---

## Frontmatter

```yaml
---
title: [Article Title] | Marketing Boutique
description: [150-160 character meta description with keyword]
author: [Author Name]
date: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
category: [research|engineering-log|insight]
tags: [tag1, tag2, tag3]
layout: article
schema:
  "@context": "https://schema.org"
  "@type": "Article"
  headline: "[Article Title]"
  author:
    "@type": "Person"
    name: "[Author Name]"
  datePublished: "[YYYY-MM-DD]"
  dateModified: "[YYYY-MM-DD]"
  publisher:
    "@type": "Organization"
    name: "Marketing Boutique"
---
```

---

## Article Structure

### Opening Hook

```markdown
# [Article Title]

**[Bold statement, statistic, or provocative insight]**

[1-2 paragraphs introducing the topic, explaining why it matters, and previewing what the reader will learn.]
```

**Hook Types:**
- **Statistic:** "72% of AI startups have zero Knowledge Panel presence."
- **Contrarian take:** "Your blog strategy is probably wrong."
- **Question:** "Why does your outbound only get 2% reply rates?"
- **Outcome:** "We reduced CAC by 40% in 3 months. Here's how."

---

### Table of Contents (Optional for long articles)

```markdown
---

**In This Article:**
1. [Section 1 Title](#section-1-anchor)
2. [Section 2 Title](#section-2-anchor)
3. [Section 3 Title](#section-3-anchor)
```

---

### Main Content Sections

Use H2 for major sections, H3 for subsections.

```markdown
---

## [Section Title]

[Content paragraphs...]

### [Subsection if needed]

[More detailed content...]
```

---

### Key Takeaways (Optional, mid-article or end)

```markdown
> **Key Insight:** [Single sentence capturing the most important point]
```

Or use a callout block:

```markdown
> [!IMPORTANT]
> [Critical takeaway the reader should remember]
```

---

### Data/Research Section (if applicable)

```markdown
---

## [Data Section Title]

[Context for the data or methodology]

| [Header 1] | [Header 2] | [Header 3] |
|------------|------------|------------|
| [Data] | [Data] | [Data] |
| [Data] | [Data] | [Data] |
| [Data] | [Data] | [Data] |

**Source:** [Source information or methodology note]
```

---

### Practical Application

```markdown
---

## How to Apply This

[Transition sentence]

### Step 1: [Action Title]
[Explanation of how to implement]

### Step 2: [Action Title]
[Explanation of how to implement]

### Step 3: [Action Title]
[Explanation of how to implement]
```

---

### Closing

```markdown
---

## What This Means for You

[1-2 paragraphs summarizing implications and next steps]

---

**Want help implementing this?**

[**Book a Strategy Call →**](/contact/)
```

---

## Article Types

### Research Article
- Original data and analysis
- Methodology explanation
- Multiple data tables/charts
- Longer form (2,000-5,000 words)

### Engineering Log
- Step-by-step walkthrough
- Code snippets or configurations
- Tool-specific details
- Practical how-to focus

### Insight Piece
- Commentary on trends
- Opinion with evidence
- Shorter form (1,000-1,500 words)
- Designed for social sharing

---

## Checklist Before Publishing

- [ ] Title compelling and ≤60 chars with keyword
- [ ] Meta description 150-160 chars
- [ ] Author and date in frontmatter
- [ ] Strong opening hook
- [ ] Clear section structure with H2/H3
- [ ] At least one table, list, or structured data element
- [ ] Internal links to related content (3-5)
- [ ] Closing CTA
- [ ] Schema markup with Article type
- [ ] Tags for categorization
