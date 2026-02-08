# Hub Page Template

Use this template for index/navigation pages that link to sub-pages (e.g., Solutions index, Intelligence hub).

---

## Frontmatter

```yaml
---
title: [Hub Name] | [Tagline - Max 60 chars total]
description: [150-160 character meta description explaining what the hub contains]
layout: hub
schema:
  "@context": "https://schema.org"
  "@type": "CollectionPage"
  name: "[Hub Name]"
  description: "[Brief description of what the hub covers]"
---
```

---

## Page Structure

### Opening Section (H1 + Value Statement)

```markdown
# [Hub Name]

**[Bold value proposition or framing statement]**

[2-3 sentences explaining what this hub covers and why it matters. Frame the categories or approaches offered.]
```

**Example:**
```markdown
# Solutions

**We Engineer Growth Through Technical Infrastructure.**

Whether you're finding Product-Market Fit, scaling post-Series A, or dominating your category, we have solutions designed for your stage and challenges.
```

---

### Category Sections

Use multiple H2 sections to organize sub-pages. Common patterns:

#### Pattern 1: By Stage/Maturity

```markdown
---

## By Growth Stage

Choose the path that matches your current phase:

### [Stage 1 - Link](/path/)
**[One-line descriptor]**

[2-3 sentences explaining what this stage covers and who it's for.]

### [Stage 2 - Link](/path/)
**[One-line descriptor]**

[2-3 sentences explaining what this stage covers and who it's for.]

### [Stage 3 - Link](/path/)
**[One-line descriptor]**

[2-3 sentences explaining what this stage covers and who it's for.]
```

#### Pattern 2: By Challenge/Problem

```markdown
---

## By Challenge

Start with your biggest pain point:

| Challenge | Solution | What We Build |
|-----------|----------|---------------|
| [[Link]](/path/) | [Category] | [Brief deliverables] |
| [[Link]](/path/) | [Category] | [Brief deliverables] |
| [[Link]](/path/) | [Category] | [Brief deliverables] |
```

#### Pattern 3: By Service/Capability

```markdown
---

## By Service

Explore our core capabilities:

### [[Service 1]](/path/)
[2-3 sentence description of this service.]

### [[Service 2]](/path/)
[2-3 sentence description of this service.]

### [[Service 3]](/path/)
[2-3 sentence description of this service.]
```

---

### Optional: Featured Highlights

For hubs with rich sub-content, highlight key pieces:

```markdown
---

## Featured

### [Featured Item Title]
[Brief teaser description]

[Read More →](/path/)
```

---

### Closing CTA

```markdown
---

## Not Sure Where to Start?

[1-2 sentences offering help or next steps]

[**Book a Discovery Call →**](/contact/)
```

---

## Navigation Best Practices

- Each sub-page should be linked at least once
- Use consistent link formatting: `[Text](/path/)`
- Internal links should use relative paths
- Group related pages logically
- Provide multiple entry points (stage, challenge, service)

---

## Checklist Before Publishing

- [ ] Title ≤60 chars with keyword
- [ ] Meta description 150-160 chars
- [ ] H1 matches hub purpose
- [ ] Clear categorization logic (stage/challenge/service)
- [ ] All sub-pages linked at least once
- [ ] Brief descriptions for each link
- [ ] Closing CTA to contact or next step
- [ ] Schema markup (CollectionPage or WebPage)
