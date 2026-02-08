# Case Study Template

Use this template for all case studies and client success stories.

---

## Frontmatter

```yaml
---
title: "[Client/Industry]: [Outcome Headline]"
description: [150-160 character summary of the outcome with key metric]
client: [Client Name or Anonymized Descriptor]
industry: [Industry Category]
stage: [Seed|Series A|Series B|Enterprise]
services: [GTM Engineering, AEO/GEO, etc.]
layout: case-study
schema:
  "@context": "https://schema.org"
  "@type": "Article"
  headline: "[Case Study Title]"
  author:
    "@type": "Organization"
    name: "Marketing Boutique"
  about:
    "@type": "Organization"
    name: "[Client Name]"
---
```

---

## Case Study Structure

### Header Section

```markdown
# [Outcome Headline]

**[Client Description]** – [Industry], [Stage]

---

## At a Glance

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| [Primary KPI] | [Value] | [Value] | [+X% or Δ] |
| [Secondary KPI] | [Value] | [Value] | [+X% or Δ] |
| [Tertiary KPI] | [Value] | [Value] | [+X% or Δ] |

**Services Used:** [GTM Engineering, AEO/GEO, etc.]
**Timeline:** [X months]
```

**Example:**
```markdown
# From 0 to $2M Pipeline in 6 Months

**AI Infrastructure Startup** – Developer Tools, Series A

---

## At a Glance

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Monthly Pipeline | $150K | $500K | +233% |
| Reply Rate (Cold) | 2% | 12% | +6x |
| Meetings/Month | 8 | 45 | +462% |

**Services Used:** GTM Engineering, AEO/GEO
**Timeline:** 6 months
```

---

### Challenge Section

```markdown
---

## The Challenge

[2-3 paragraphs describing:]
- Who the client is (without revealing if anonymized)
- What they were struggling with
- What they had tried before
- The stakes (why solving this mattered)

### Key Pain Points
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]
```

---

### Solution Section

```markdown
---

## Our Approach

[1 paragraph overview of the strategy]

### Phase 1: [Phase Name]
[What we did in this phase]

**Specific actions:**
- [Action 1]
- [Action 2]
- [Action 3]

### Phase 2: [Phase Name]
[What we did in this phase]

**Specific actions:**
- [Action 1]
- [Action 2]
- [Action 3]

### Phase 3: [Phase Name]
[Same structure...]
```

---

### Technical Details (Optional but recommended)

```markdown
---

## Technical Implementation

[For technically sophisticated readers, describe the systems built:]

### [System/Component Name]
[Description of what was built and how it works]

**Tech Stack:**
- [Tool 1]
- [Tool 2]
- [Tool 3]
```

---

### Results Section

```markdown
---

## Results

[1-2 paragraphs summarizing the overall impact]

### Key Metrics

| Metric | Before | After | Timeline |
|--------|--------|-------|----------|
| [Metric 1] | [Value] | [Value] | [Timeframe] |
| [Metric 2] | [Value] | [Value] | [Timeframe] |
| [Metric 3] | [Value] | [Value] | [Timeframe] |
| [Metric 4] | [Value] | [Value] | [Timeframe] |

### Additional Outcomes
- [Qualitative outcome 1]
- [Qualitative outcome 2]
- [Unexpected benefit]
```

---

### Client Quote (if available)

```markdown
---

## What [Client Name] Says

> "[Direct quote from client about working with us and the outcomes]"
>
> — **[Name]**, [Title] at [Company]
```

---

### Closing CTA

```markdown
---

## Ready to See Similar Results?

[1-2 sentences offering next steps]

[**Book a Strategy Call →**](/contact/)
```

---

## Case Study Best Practices

### Specificity is Key
- Use exact numbers, not ranges
- Include timeframes for results
- Specify tools and technologies used
- Describe the actual process, not generalized steps

### Anonymization When Needed
If client wishes to remain anonymous:
- Use descriptors: "AI Infrastructure Startup"
- Include industry and stage
- All metrics should still be real

### Outcome-Focused Headlines
Lead with the result:
- ✅ "From 0 to $2M Pipeline in 6 Months"
- ✅ "40% CAC Reduction for Developer Tools Platform"
- ❌ "How We Helped Client X with Marketing"

---

## Checklist Before Publishing

- [ ] Client approval obtained (or properly anonymized)
- [ ] Title leads with outcome metric
- [ ] At-a-Glance table with before/after metrics
- [ ] Clear challenge → solution → results structure
- [ ] Specific numbers, not generalizations
- [ ] Technical details appropriate for audience
- [ ] Client quote if available
- [ ] Services and timeline documented
- [ ] Schema markup in frontmatter
- [ ] Strong closing CTA
