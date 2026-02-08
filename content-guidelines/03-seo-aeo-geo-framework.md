# SEO, AEO, GEO & SXO Content Framework

## Overview

This document outlines how to create content optimized for modern discovery. AI has fundamentally changed the SEO game—the goal is no longer just to rank, but to **be cited, be referenced, and be the answer**.

Modern search optimization is built on four layers:
1. **GEO (Generative Engine Optimization)** – ChatGPT & Gemini citations
2. **AEO (Answer Engine Optimization)** – Google AI Overview appearances, featured snippets
3. **AIO (AI Integration Optimization)** – Tool integration data, API visibility
4. **SXO (Search Experience Optimization)** – Conversion after arrival

All content should be designed with all four layers in mind. They are not mutually exclusive.

---

## Old SEO vs New SEO

> **The Core Question Has Changed**  
> Old: "Can we rank higher than competitors?"  
> New: "Would AI cite our content as truth?"

| Aspect | Old SEO | New SEO |
|--------|---------|----------|
| **Goal** | Win page one, get the click | Be cited, be referenced, be the answer |
| **Model** | Keywords + Backlinks + Technical | GEO + AEO + AIO + SXO |
| **What It Measured** | Keyword rankings, domain authority, traffic volume | Citation frequency, comprehension accuracy, conversion velocity |
| **When It Worked** | Building new site authority, capturing search demand at scale | Building category authority, becoming the referenced source |
| **The Limitation/Advantage** | Traffic without intent, clicks without conviction | Pre-qualified intent, built-in trust, visibility where decisions happen |
| **Success Metric** | Page one position, organic sessions | Citations, conversion rate, authority |

### The Conversion Math

| Approach | Visitors | Conversion Rate | Signups |
|----------|----------|-----------------|----------|
| Old SEO | 100 | 4% | 4 |
| New SEO (AI Search) | 50 | 24% | 12 |

**Result:** You need **6x less traffic** to hit the same targets with the new approach.

---

## The Four-Layer Model

```
┌─────────────────────────────────────────────────────────────┐
│                    MODERN DISCOVERY                         │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐ │
│  │   GEO    │ +  │   AEO    │ +  │   AIO    │ +  │  SXO   │ │
│  │Citations │    │Overviews │    │   Tools  │    │Convert │ │
│  └──────────┘    └──────────┘    └──────────┘    └────────┘ │
│                                                             │
│  Layer 1: ChatGPT & Gemini citations                        │
│  Layer 2: Google AI Overview appearances                    │
│  Layer 3: Tool integration data                             │
│  Layer 4: Conversion after arrival                          │
└─────────────────────────────────────────────────────────────┘
```

---

## SEO Best Practices

### Keyword Strategy

#### Research Process
1. Identify core topics (GTM Engineering, AEO, Usage-Based Billing, etc.)
2. Use tools (Ahrefs, SEMrush, Google Keyword Planner) to find related terms
3. Map keywords to intent:
   - **Informational:** "what is gtm engineering"
   - **Commercial:** "gtm engineering agency"
   - **Transactional:** "hire gtm engineer"

#### Keyword Placement
| Location | Priority | Example |
|----------|----------|---------|
| Title tag | Critical | "GTM Engineering for AI Startups | Marketing Boutique" |
| H1 | Critical | "GTM Engineering" |
| Meta description | High | Include primary keyword naturally |
| First 100 words | High | Use keyword in opening paragraph |
| H2/H3 headers | Medium | Use variations and related terms |
| Body content | Medium | Natural density (2-3%) |
| URL | Medium | `/solutions/gtm-engineering/` |
| Image alt text | Low | Describe image with keywords if relevant |

### On-Page SEO Checklist

- [ ] Title tag: 50-60 characters, keyword near front
- [ ] Meta description: 150-160 characters, includes keyword, has CTA
- [ ] H1: One per page, matches search intent
- [ ] H2/H3: Logical hierarchy, includes related terms
- [ ] Internal links: 3-5 per 1000 words to relevant pages
- [ ] External links: 1-2 to authoritative sources (sparingly)
- [ ] Images: Compressed, descriptive filenames, alt text
- [ ] URL: Short, descriptive, includes keyword

### Content Length Guidelines

| Content Type | Target Length | Minimum |
|--------------|--------------|---------|
| Solutions page | 1,500-2,500 words | 1,000 |
| Hub page | 800-1,500 words | 600 |
| Blog post | 1,500-3,000 words | 1,200 |
| Research article | 2,000-5,000 words | 1,500 |
| Tool/Calculator page | 500-1,000 words | 300 |

---

## AEO Best Practices

### What is AEO?
AEO (Answer Engine Optimization) focuses on getting your content featured in:
- Google Featured Snippets
- Google AI Overviews
- Bing Answer Boxes
- Knowledge Panels

### Content Structures for Snippets

#### Definition Snippets
When answering "What is X?", provide a clear 40-60 word definition immediately after the H2.

**Format:**
```markdown
## What is GTM Engineering?

GTM Engineering is the technical discipline of building go-to-market infrastructure using automation, data enrichment, and integrated tooling. It treats marketing and sales operations as an engineering problem—designing systems, pipelines, and workflows that scale revenue without linear headcount growth.
```

#### List Snippets
For "How to" or "Steps" queries, use numbered or bulleted lists.

**Format:**
```markdown
## How to Build an Enrichment Waterfall

1. **Define your data fields** – Identify what you need: email, phone, company size, tech stack
2. **Select primary sources** – Apollo, Clearbit, LinkedIn Sales Navigator
3. **Configure waterfall logic** – Try source A, if empty try B, if empty try C
4. **Test coverage rates** – Measure what percentage of records are enriched
5. **Connect to CRM** – Push enriched data to HubSpot or Salesforce
```

#### Table Snippets
For comparisons and data, use Markdown tables.

**Format:**
```markdown
| Stage | CAC Benchmark | Sales Cycle |
|-------|---------------|-------------|
| Seed | $500-2,000 | 30-60 days |
| Series A | $2,000-5,000 | 60-90 days |
| Series B | $5,000-15,000 | 90-180 days |
```

### Snippet Bait Strategy

**"Snippet Bait"** = Content structured specifically to be extracted by answer engines.

1. **Lead with the answer** – Don't bury information; put it upfront
2. **Use header-then-content pattern** – H2/H3 as the question, immediate answer below
3. **Be comprehensive but concise** – Enough detail to be definitive, not so much it's overwhelming
4. **Include data points** – Numbers, percentages, and benchmarks are highly extractable

---

## AIO Best Practices

### What is AIO?

AIO (AI Integration Optimization) focuses on making your content and brand discoverable through AI tools and integrations:
- AI assistant tool recommendations ("Use this calculator for...")
- API-based citations in AI workflows
- Integration with AI-powered research and analysis tools

### AIO Content Principles

#### 1. Tool Discoverability
Create content that positions your tools, calculators, and resources as solutions AI can recommend.

**Implementation:**
- Use `SoftwareApplication` schema for tools
- Include clear use-case descriptions ("Use this when...")
- Provide structured input/output documentation
- Create comparison content ("X vs Y tool")

#### 2. API-Ready Content
Structure content so AI systems can easily extract and reference it.

**Implementation:**
- JSON-LD for all structured data
- Clear endpoint-style content organization
- Machine-readable pricing, features, and specifications

#### 3. Integration Positioning
Position your offerings within tool ecosystems AI assistants understand.

**Examples:**
- "Works with HubSpot, Salesforce, and Apollo"
- "Integrates with your existing CRM"
- "Replaces [common tool] with AI-native approach"

---

## SXO Best Practices

### What is SXO?

SXO (Search Experience Optimization) focuses on what happens **after** the visitor arrives:
- **Comprehension accuracy** – Is your content immediately understandable?
- **Conversion velocity** – How fast can visitors take their intended action?
- **Intent fulfillment** – Does the page deliver exactly what was promised?

### SXO Content Principles

#### 1. Comprehension First
Visitors from AI search arrive with high intent and pre-existing context. Don't waste their time.

**Implementation:**
- Lead with the answer, then expand
- Use visual hierarchy to enable scanning
- Clear CTAs visible without scrolling
- Progressive disclosure for complex topics

#### 2. Conversion Velocity
Optimize the path from arrival to action.

**Implementation:**
- Single primary CTA per page
- Minimal form fields (name + email for initial contact)
- Calendar booking embedded, not linked
- Social proof near decision points

#### 3. Intent-Content Match
Every page should fulfill exactly one intent exceptionally well.

**Ask yourself:**
- What question brought them here?
- What action should they take?
- What objections might remain?

---

## GEO Best Practices

### What is GEO?
GEO (Generative Engine Optimization) focuses on getting your content:
- Cited by LLMs (ChatGPT, Claude, Perplexity)
- Recommended when users ask about your category
- Used as a source for AI-generated answers

### The Citation Hierarchy

LLMs prioritize sources based on:
1. **Entity Recognition** – Is your brand a "known entity" (Wikipedia, Wikidata)?
2. **Source Authority** – Domain authority, backlinks, age
3. **Content Quality** – Depth, originality, information gain
4. **Freshness** – How recently was content updated?
5. **Format** – Is content machine-readable?

### GEO Content Principles

#### 1. Information Gain Protocol
Every piece of content should add something **new** to the conversation—not rehash existing information.

**Ways to achieve information gain:**
- Original research and data
- Proprietary frameworks and models
- First-hand case studies
- Expert insights not available elsewhere
- Unique combinations of existing knowledge

#### 2. Entity-Based Writing
Write about your brand as an **entity** with clear relationships.

**Include in content:**
- Company name with consistent formatting
- Founder/team names and credentials
- Service names (use consistent terminology)
- Client names (with permission)
- Partner/tool relationships

#### 3. Structured Data
Machine-readable formatting helps LLMs extract and cite your content.

**Implementation:**
- JSON-LD schema in page metadata
- Clear Markdown formatting
- Tables with explicit headers
- Bulleted/numbered lists

#### 4. Citation Worthiness
Ask: "Would an LLM cite this as a source?"

**Citation-worthy content includes:**
- Specific statistics with sources
- Definitive statements ("X is defined as...")
- Step-by-step processes
- Comparative analyses
- Original research findings

### llms.txt Implementation

Create a `/llms.txt` file to help LLMs understand your site structure:

```
# Marketing Boutique

> GTM Engineering and Generative Authority for AI-native B2B startups

## Main Pages
- [Homepage](/) - Overview of services and positioning
- [Solutions](/solutions/) - GTM Engineering, AEO/GEO, Revenue Operations
- [Intelligence](/intelligence/) - Research, playbooks, and tools
- [About](/about/) - Company philosophy and team
- [Contact](/contact/) - Book a strategy call

## Key Topics
- GTM Engineering
- Answer Engine Optimization (AEO)
- Generative Engine Optimization (GEO)
- Usage-Based RevOps
- Data Enrichment
- Signal-Based Prospecting
```

---

## Frontmatter Schema Template

Every content page should include schema markup in the frontmatter:

```yaml
---
title: "[Page Title] | Marketing Boutique"
description: "[150-160 character meta description with keyword]"
layout: [solution|hub|article|tool]
schema:
  "@context": "https://schema.org"
  "@type": "[WebPage|Service|Article|FAQPage|HowTo]"
  name: "[Page name]"
  description: "[Description for schema]"
  provider:
    "@type": "Organization"
    name: "Marketing Boutique"
---
```

### Schema Types by Page

| Page Type | Primary Schema | Additional Schema |
|-----------|---------------|-------------------|
| Homepage | Organization | WebSite |
| Solutions page | Service | FAQPage |
| Hub page | WebPage | CollectionPage |
| Blog post | Article | FAQPage (if has FAQ) |
| Research | Article | Dataset (if data-heavy) |
| Case study | Article | Organization (client) |
| Tool page | SoftwareApplication | HowTo |

---

## Success Metrics: Old vs New

### Stop Optimizing For (Old Metrics)
- ❌ Keyword rankings (vanity metric)
- ❌ Domain authority (means-to-end)
- ❌ Raw traffic volume (quantity over quality)

### Start Optimizing For (New Metrics)
- ✅ **Citation frequency** – How often are you referenced by AI?
- ✅ **Comprehension accuracy** – Does AI represent you correctly?
- ✅ **Conversion velocity** – How fast do qualified visitors convert?

---

## The New Playbook

1. ✅ **Deploy schema on core pages** – Every key page needs complete JSON-LD markup
2. ✅ **Refresh content every 30 days** – LLMs favor fresh, updated sources
3. ✅ **Track visibility + comprehension + conversion** – Monitor how AI cites you
4. ✅ **Structure for AI consumption first** – Then optimize for human reading

---

## AI Search Readiness Assessment

Use this scorecard to assess your current AI search readiness across all three dimensions.

### SEO Health Check

**Warning Signs:**
- ⚠️ Content hasn't been updated in 90+ days
- ⚠️ No schema markup deployed
- ⚠️ Slow page load times (>3 sec)
- ⚠️ Thin content (<800 words)
- ⚠️ No systematic refresh process

**Current State Assessment:**
- [ ] Technical SEO optimized
- [ ] Content clusters mapped
- [ ] Internal linking structured
- [ ] Backlinks from authority sites
- [ ] Core Web Vitals optimized

**SEO Score:**
| Score | Status |
|-------|--------|
| 5/5 | Category domination |
| 3-4/5 | Holding position |
| 1-2/5 | Losing ground |
| 0/5 | Invisible |

---

### AEO Health Check

**Warning Signs:**
- ⚠️ No FAQ schema anywhere
- ⚠️ Unstructured content
- ⚠️ Incomplete answers
- ⚠️ Missing metadata
- ⚠️ No citation tracking

**Current State Assessment:**
- [ ] FAQ schema deployed
- [ ] Appearing in AI Overviews
- [ ] Featured snippets captured
- [ ] Q&A format structured
- [ ] Profound tracking active

**AEO Score:**
| Score | Status |
|-------|--------|
| 5/5 | AI trusts your answers |
| 3-4/5 | Inconsistent visibility |
| 1-2/5 | Rarely surfaces |
| 0/5 | Never cited |

---

### GEO Health Check

**Warning Signs:**
- ⚠️ Never cited by ChatGPT
- ⚠️ Generic positioning
- ⚠️ No original research
- ⚠️ Weak authority signals
- ⚠️ Content reads like everyone else's

**Current State Assessment:**
- [ ] Original research published
- [ ] Expert authority documented
- [ ] AI platforms cite content
- [ ] Strong brand recognition
- [ ] Competitive differentiation

**GEO Score:**
| Score | Status |
|-------|--------|
| 5/5 | The cited authority |
| 3-4/5 | Occasionally mentioned |
| 1-2/5 | Generic and ignored |
| 0/5 | Unknown to AI |

---

### Total Score Calculation

```
SEO Score ___/5  +  AEO Score ___/5  +  GEO Score ___/5  =  TOTAL ___/15
```

### Action Playbook by Score

| Score | Status | What to Do |
|-------|--------|------------|
| **13-15** | Market Leader | Document winning patterns • Expand to adjacent topics • Publish original research monthly • Maintain 30-day refresh cadence |
| **10-12** | Strong Position | Map competitor content gaps • Add schema to remaining pages • Refresh top 20 pages monthly • Launch citation tracking |
| **6-9** | Building Phase | Focus on top 10 pages only • Deploy FAQ schema this week • Set up Profound tracking • Commit to 90-day sprint |
| **0-5** | Invisible | Audit current schema (likely zero) • Add Article + FAQ to 5 pages • Mine 50 questions from Reddit • Establish weekly measurement |

---

### Benchmark Targets

Based on Webflow's 90-day results:

| Metric | Target |
|--------|--------|
| **AI Search Signups** | 10% of total signups from AI search |
| **AI Citations** | +331 new AI citations in 90 days |
| **Conversion Rate** | 6x higher conversion from ChatGPT traffic |
| **SEO Impressions** | +24% increase in SEO impressions |

**Your goal:** Beat your baseline in 90 days or less.

---

## Content Optimization Checklist

### SEO Checklist
- [ ] Primary keyword in title, H1, first 100 words
- [ ] Meta description with keyword and CTA
- [ ] 3-5 internal links
- [ ] Proper header hierarchy (H1 > H2 > H3)
- [ ] Image optimization (compressed, alt text)

### AEO Checklist
- [ ] At least one snippet-optimized section (definition, list, or table)
- [ ] Clear header-then-answer structure
- [ ] Specific data points with sources
- [ ] FAQ section with Q&A format

### GEO Checklist
- [ ] Information gain (something new/original)
- [ ] Entity mentions (brand, people, tools)
- [ ] Schema markup in frontmatter
- [ ] Machine-readable formatting (tables, lists)
- [ ] Citation-worthy statements with specificity

### AIO Checklist
- [ ] Tool/resource pages use SoftwareApplication schema
- [ ] Clear use-case descriptions included
- [ ] Integration ecosystem mentioned where relevant
- [ ] Comparison content for discoverability

### SXO Checklist
- [ ] Answer appears above the fold
- [ ] Single clear CTA per page
- [ ] Page fulfills one intent exceptionally
- [ ] Social proof near decision points
- [ ] Minimal friction to conversion
