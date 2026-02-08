# Solutions Page Template

Use this template for all service/solution pages (e.g., GTM Engineering, AEO/GEO, Revenue Operations).

---

## Frontmatter

```yaml
---
title: [Solution Name] | [Tagline - Max 60 chars total]
description: [150-160 character meta description with primary keyword and CTA]
layout: solution
schema:
  "@context": "https://schema.org"
  "@type": "Service"
  serviceType: "[Solution Name]"
  provider:
    "@type": "Organization"
    name: "Marketing Boutique"
  areaServed: "Worldwide"
---
```

---

## Page Structure

### Opening Hook (H1 + Problem Statement)

```markdown
# [Solution Name]

**[Bold problem statement or provocative insight]**

[2-3 sentences explaining the core problem your audience faces. Be specific to AI startups. End with how you solve it.]
```

**Example:**
```markdown
# GTM Engineering

**Your Sales Team Shouldn't Be Doing Data Entry.**

AI startups waste hundreds of hours per month on manual prospecting, data cleanup, and tool configuration. GTM Engineering automates the infrastructure—so your team can focus on closing deals.
```

---

### The Problem Section (H2)

```markdown
---

## The [Problem] for AI Startups

[1-2 paragraphs explaining the problem in detail]

| Common Mistake | Why It Fails |
|----------------|--------------|
| [Mistake 1] | [Consequence] |
| [Mistake 2] | [Consequence] |
| [Mistake 3] | [Consequence] |

**The reality:** [Summary statement about the core insight]
```

---

### Solution Overview (H2)

```markdown
---

## Our [Solution] Services

### 1. [Service Component 1]
[Description paragraph]

**What We Build:**
- [Specific deliverable 1]
- [Specific deliverable 2]
- [Specific deliverable 3]

### 2. [Service Component 2]
[Description paragraph]

**What We Build:**
- [Specific deliverable 1]
- [Specific deliverable 2]
- [Specific deliverable 3]

### 3. [Service Component 3]
[Same structure...]

### 4. [Service Component 4]
[Same structure...]
```

---

### Metrics/Outcomes Section (H2)

```markdown
---

## Key Metrics We Impact

| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| [Metric 1] | [Definition] | [Business impact] |
| [Metric 2] | [Definition] | [Business impact] |
| [Metric 3] | [Definition] | [Business impact] |
| [Metric 4] | [Definition] | [Business impact] |
```

---

### Optional: Benchmarks/Data Section (H2)

```markdown
---

## Benchmarks for AI Startups

Based on our work with [Seed / Series A / Series B] AI companies:

| Metric | Healthy Benchmark |
|--------|-------------------|
| [Metric 1] | [Value] |
| [Metric 2] | [Value] |
| [Metric 3] | [Value] |

If you're below these benchmarks, we identify why and build the infrastructure to improve.
```

---

### FAQ Section (H2)

```markdown
---

## Frequently Asked Questions

### [Question 1]
[Direct, specific answer in 2-4 sentences]

### [Question 2]
[Direct, specific answer in 2-4 sentences]

### [Question 3]
[Direct, specific answer in 2-4 sentences]
```

---

### Closing CTA

```markdown
---

[**[Action CTA] →**](/contact/)
```

**CTA Examples:**
- "Build Your GTM Infrastructure →"
- "Optimize Your Funnel →"
- "Start Your Audit →"

---

## Checklist Before Publishing

- [ ] Title ≤60 chars with keyword
- [ ] Meta description 150-160 chars with keyword and CTA
- [ ] H1 matches page title and search intent
- [ ] Problem section has table with specific issues
- [ ] 3-5 service components with specific deliverables
- [ ] Metrics table with definitions and business impact
- [ ] FAQ with 3-5 common questions
- [ ] Strong closing CTA with link
- [ ] Schema markup in frontmatter
- [ ] Internal links to related solutions
