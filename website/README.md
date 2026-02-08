# Marketing Boutique Website Blueprint

This directory contains the complete structure, content, and architectural details for the **[marketing-boutique.com](https://marketing-boutique.com)** website.

## Overview
This is a high-fidelity blueprint designed for developers building the site in **Framer**. It serves as the single source of truth for the website's implementation, ensuring that all content, SEO requirements, and navigation logic are executed accurately.

## Tech Stack & Specs
- **Platform:** Framer
- **Target Domain:** [marketing-boutique.com](https://marketing-boutique.com)
- **Framework requirements:** The site must be built with a focus on speed and AI-Search optimization (AEO/GEO).

## Folder Structure
The folder hierarchy mirrors the intended URL structure of the live site:

- **[00_Navigation_and_Footer.md](file:///Users/fenilparekh/Documents. 

/MB%20SEO/website/00_Navigation_and_Footer.md)**: Master definition for the Global Navbar, Solutions Mega Menu, and Footer.
- **`/solutions`**: Pages focused on growth stages (Seed, Series A, Enterprise) and core service offerings.
- **`/intelligence`**: A heavy content wing containing research reports, engineering playbooks, and interactive tools.
- **`/results`**: Case studies and client success stories.
- **`/about` & `/contact`**: Agency-specific informational and conversion pages.

## Implementation Guide for Developers
1. **CMS Integration**: Use Framer's CMS to handle repetitive content types in `/intelligence` and `/results`.
2. **SEO & Metadata**: Every markdown file in this folder includes frontmatter or header details that MUST be mapped to the page's `<title>` tag and `meta description`.
3. **URL Consistency**: Follow the folder-based routing strategy: `marketing-boutique.com/[category]/[slug]`.
4. **UX/UI fidelity**: Use the content hierarchy in the markdown files to guide the layout—headers should be H1-H4 respectively, and CTA sections should be placed as indicated in the text.

---
*Documented for the Marketing Boutique Development Team.*
