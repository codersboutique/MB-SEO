# E-E-A-T Implementation Guide

## What is E-E-A-T?

E-E-A-T stands for:
- **E**xperience
- **E**xpertise
- **A**uthoritativeness
- **T**rustworthiness

Google uses E-E-A-T as a quality signal to evaluate content, especially for YMYL (Your Money or Your Life) topics. For B2B content about business strategy, technology, and investment, demonstrating E-E-A-T is essential.

---

## The E-E-A-T Framework

```
┌───────────────────────────────────────────────────────────────┐
│                         TRUST                                 │
│    ┌─────────────────────────────────────────────────────┐    │
│    │                   AUTHORITY                          │    │
│    │   ┌───────────────────────────────────────────┐     │    │
│    │   │              EXPERTISE                    │     │    │
│    │   │   ┌───────────────────────────────┐      │     │    │
│    │   │   │         EXPERIENCE            │      │     │    │
│    │   │   │  (First-hand knowledge)       │      │     │    │
│    │   │   └───────────────────────────────┘      │     │    │
│    │   │   (Deep domain knowledge)                │     │    │
│    │   └───────────────────────────────────────────┘     │    │
│    │   (Recognized source in the field)                  │    │
│    └─────────────────────────────────────────────────────┘    │
│    (Overall reliability and credibility)                      │
└───────────────────────────────────────────────────────────────┘
```

---

## 1. Experience Signals

**Experience = First-hand knowledge and direct involvement**

### How to Demonstrate Experience

#### Share Real Implementations
Don't just explain theory—show what you've actually done.

**Example:**
> ❌ "Enrichment waterfalls can improve data coverage."
> ✅ "When we built an enrichment waterfall for [Client], we increased email coverage from 62% to 94% by layering Apollo, Clearbit, and People Data Labs in sequence."

#### Include Specific Details
Specificity signals experience. Generic content signals theory.

| Generic (Low Experience) | Specific (High Experience) |
|--------------------------|---------------------------|
| "Set up proper tracking" | "Configure UTM parameters in this format: utm_source/utm_medium/utm_campaign/utm_term" |
| "Optimize your funnel" | "Our audits typically find 15-20% drop-off at the demo scheduling step due to form friction" |
| "Use the right tools" | "We use Clay for enrichment, n8n for automation, and HubSpot for CRM—here's why" |

#### Document Process, Not Just Outcomes
Showing the messy middle demonstrates you've actually done the work.

**Structure:**
- What we tried
- What didn't work (and why)
- What we learned
- What we do now

#### First-Person Perspective
Use "we" for company experience, "I" for individual expertise.

> "We've implemented this system for 30+ clients, and the most common failure point is..."
> "I've spent 10 years building GTM infrastructure, and the biggest mistake founders make is..."

---

## 2. Expertise Signals

**Expertise = Deep domain knowledge and skill**

### How to Demonstrate Expertise

#### Technical Depth
Don't shy away from complexity. Our audience is technical.

**Include:**
- Code snippets and configuration examples
- Workflow diagrams
- Tool-specific settings
- API references
- Edge cases and gotchas

#### Frameworks and Models
Create proprietary frameworks that organize domain knowledge.

**Marketing Boutique Frameworks:**
- Generative Authority Framework (GAF)
- Information Gain Protocol
- Entity-First Architecture
- Barbell Content Strategy

#### Comparative Analysis
Demonstrate expertise by comparing options with nuance.

**Example:**
> "For CRM, we typically recommend HubSpot for Seed/Series A and Salesforce for Series B+. Here's why:
> - HubSpot: Lower TCO, faster setup, better for small teams
> - Salesforce: More customizable, better enterprise integrations, required by some enterprise buyers"

#### Acknowledge Complexity
Experts know that simple answers are rarely correct.

> "The right answer depends on your sales cycle length, deal size, and team structure. Here's how to think about it..."

---

## 3. Authoritativeness Signals

**Authoritativeness = Recognition as a trusted source in the field**

### How to Build Authority

#### Original Research
Nothing builds authority faster than publishing data others don't have.

**Types of original research:**
- Benchmark reports (CAC by stage, sales cycle by industry)
- Visibility studies (AEO citation frequency analysis)
- Case studies with permission

#### Industry Citations
When others cite you, authority compounds.

**Get cited by:**
- Publishing research that journalists and analysts reference
- Contributing quotes to industry publications
- Speaking at relevant conferences
- Guest posting on authoritative sites

#### Backlink Profile
Authority is partially measured by who links to you.

**Link-earning content:**
- Research and data studies
- Free tools and calculators
- Comprehensive guides
- Controversial/opinionated takes (Barbell Strategy)

#### Third-Party Signals
Display signals of recognition:
- Client logos (with permission)
- Case study results
- Awards or certifications
- Media mentions

---

## 4. Trustworthiness Signals

**Trustworthiness = Overall reliability and honesty**

### How to Build Trust

#### Transparency
Be open about methodology, limitations, and conflicts.

**Include:**
- How data was collected (for research)
- Our perspective and biases
- What we don't know
- Who we work best with (and who we don't)

#### Accuracy
Every claim should be verifiable.

**Best practices:**
- Cite sources for statistics
- Date-stamp time-sensitive information
- Update content when information changes
- Correct errors publicly

#### Contact Information
Easy-to-find contact details signal legitimacy.

**Include on every page:**
- Link to Contact page
- Company name and location
- Email address

#### Privacy and Security
For a B2B site handling leads:
- Clear privacy policy
- HTTPS everywhere
- Clear data handling practices

#### Consistent Identity
Trust requires recognition.

- Consistent branding across all pages
- Same company name format everywhere
- Author bylines on articles with bio links
- Updated "Last modified" dates

---

## E-E-A-T Checklist by Content Type

### Solutions Pages

| Signal | Implementation |
|--------|---------------|
| Experience | Case study snippets, specific metrics, "what we build" sections |
| Expertise | Technical details on approach, tool-specific guidance |
| Authority | Client results, testimonials, industry benchmarks |
| Trust | Clear pricing approach, FAQ section, contact CTA |

### Blog/Research Articles

| Signal | Implementation |
|--------|---------------|
| Experience | First-person narrative, process documentation |
| Expertise | In-depth analysis, frameworks, code examples |
| Authority | Original data, citations from others, author credentials |
| Trust | Sources cited, methodology explained, date published |

### Hub/Index Pages

| Signal | Implementation |
|--------|---------------|
| Experience | Overview of capability areas with experience markers |
| Expertise | Categorization that displays domain knowledge |
| Authority | Links to detailed content, third-party signals |
| Trust | Consistent navigation, clear organization |

### About Page

| Signal | Implementation |
|--------|---------------|
| Experience | Founding story, years in business, team background |
| Expertise | Areas of specialization, team credentials |
| Authority | Notable clients, media mentions, speaking engagements |
| Trust | Photos, location, values, contact accessibility |

---

## Author/Entity Pages

For GEO and E-E-A-T, consider creating:

### Team Member Pages
For each key team member, include:
- Photo
- Role and responsibilities
- Background and credentials
- LinkedIn link
- Articles they've authored

### Entity Summary (for Schema)
```yaml
schema:
  "@type": "Person"
  name: "[Full Name]"
  jobTitle: "[Role]"
  worksFor:
    "@type": "Organization"
    name: "Marketing Boutique"
  sameAs:
    - "https://linkedin.com/in/[handle]"
    - "https://twitter.com/[handle]"
```

---

## Monthly E-E-A-T Audit

Periodically review content for E-E-A-T signals:

### Experience Audit
- [ ] Does content include real examples from our work?
- [ ] Are outcomes specific with real numbers?
- [ ] Does language reflect hands-on involvement?

### Expertise Audit
- [ ] Is technical depth appropriate for the audience?
- [ ] Are our frameworks and models clearly articulated?
- [ ] Do we address nuance and complexity?

### Authority Audit
- [ ] Is our research cited by others?
- [ ] Are we earning backlinks to key pages?
- [ ] Are third-party signals (logos, quotes) up to date?

### Trust Audit
- [ ] Is contact information visible and accurate?
- [ ] Are claims sourced and dated?
- [ ] Is the site secure and policy-compliant?
