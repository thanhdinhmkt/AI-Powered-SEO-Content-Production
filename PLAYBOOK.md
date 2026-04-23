# AI-Powered SEO Content Production — Playbook & SOP

**Version:** 1.0  
**Last Updated:** April 2026  
**Based on research from:** 10 practitioners (see `/research/sources.md`)  
**Author:** Research Synthesis

---

> **Before you read this:** This playbook is built entirely from primary research — LinkedIn posts, blog articles, and newsletter data collected directly from practitioners who run live sites and publish real numbers. Every recommendation below cites its source. Where experts contradict each other, I tell you which side I take and why. Where I disagree with all of them, I say so.

---

## Who This Playbook Is For

This SOP is for SEO content leads, growth marketers, and site operators who are:

- Producing 10+ articles per month and want to integrate AI into the production pipeline
- Trying to maintain or improve search visibility as AI Overviews and AI Mode expand
- Building content that gets cited by LLMs (ChatGPT, Gemini, Perplexity), not just ranked by Google
- Willing to prioritize sustainable results over short-term traffic spikes

This is **not** for people who want a copy-paste prompt template to generate content at zero cost. That strategy is structurally broken by 2026 and the data proves it.

---

## Core Philosophy

Two facts define the current moment in AI SEO:

**Fact 1:** AI traffic is still small but search behavior is structurally shifting. AI traffic currently represents only 1–2% of referral traffic for most websites, and ChatGPT has roughly 5.14 billion total visits vs. Google's 81.31 billion (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/ai-search-trends/), May 2025). But in the headphones vertical alone, AI Overviews expanded from 2.28% to 32.76% SERP presence in 12 months, while classic organic click share dropped from 73% to 50% (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/serp-shifts-ads-remonetized/), February 14, 2026). The structural shift is real even if the traffic shift isn't dramatic yet.

**Fact 2:** The same thing that makes you rank in Google is what gets you cited in LLMs. Retrieval rank is the #1 citation signal — a page at position 1 in ChatGPT's retrieval results has a 58% citation rate vs. 14% at position 10 (source: [Kevin Indig × AirOps](https://www.linkedin.com/in/kevinindig/), study of 815,000 query-page pairs, 2025). Google has stated explicitly: "There is no GEO without SEO" (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/what-we-learned-google-search-central-zurich-2025/), Google Search Central Zurich, December 2025).

**The strategic conclusion:** Don't pivot away from SEO fundamentals. Layer AI production efficiency and LLM citation optimization on top of solid SEO — not instead of it.

---

## Phase 1 — Strategy: Choose Your Battlefield

### 1.1 Target Commercial and Transactional Queries First

AI Overviews primarily trigger for **informational queries** — question-style searches where Google can synthesize a quick answer. Informational content faces the highest displacement risk (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/ai-search-trends/), May 2025).

**SOP step:** Audit your current keyword portfolio. Tag each cluster as informational, commercial, or transactional. Shift production capacity toward commercial and transactional clusters. This isn't abandoning informational content — it's sequencing your bets correctly.

### 1.2 Build a Topical Map Before Writing Anything

Before a single article is written, map the entire topic universe: every entity, attribute, and value in your niche. This is Koray Tuğberk GÜBÜR's core methodology — and his Unibaby case study (195% organic traffic growth in 2 months) is the most rigorous public proof of this approach (source: [Koray Tuğberk GÜBÜR](https://www.youtube.com/@TopicalAuthority), Holistic SEO, holisticseo.digital).

**SOP step:** For each target niche, use a tool or Python script to identify:
- Core entities (the main subjects)
- Supporting entities (related concepts)
- Entity attributes (properties of each entity)
- Entity values (specific instances)

Then group these into content clusters and determine production order. Topical authority is built bottom-up: smaller supporting articles create the semantic foundation that lets your pillar pages rank.

### 1.3 Use AI for Keyword Clustering, Not Keyword Generation

AI keyword clustering — grouping keywords by semantic intent using embedding models rather than lexical similarity — is one of the highest-ROI uses of AI in SEO workflows. The workflow: export keywords → pass through embedding model → cluster by cosine similarity → assign to content hubs (source: [Nathan Gotch](https://www.youtube.com/@NathanGotch), nathangotch.com, Rankability.com).

**SOP step:** Run your keyword list through an AI clustering tool (Rankability, Surfer, or a custom Python script using OpenAI embeddings). Never assign one keyword to one article — assign keyword clusters to content hubs and sub-pages.

---

## Phase 2 — Content Architecture for AI Citation

This is the most important phase. The data here is unusually precise.

### 2.1 Write Focused Articles, Not Ultimate Guides

The SEO orthodoxy of "be comprehensive" is wrong for LLM citation. Pages covering 26–50% of ChatGPT's fanout sub-queries get cited **more** than pages covering 100%. The "ultimate guide" strategy produces worse results than a focused article covering two to three related angles well (source: [Kevin Indig × AirOps](https://www.growth-memo.com/), analysis of 815,000 query-page pairs across 16,851 queries, 2025).

**SOP step:** Write the page that is the **best answer to one question**. Not the page that adequately answers twenty.

**Target parameters:**
- Word count: 500–2,000 words (citation sweet spot)
- Subheadings: 7–20 (enough structure, not enough dilution)
- Subtopic coverage: 30–50% of related sub-queries (focused, not exhaustive)

### 2.2 Engineer Your Heading Structure

Subheadings are the primary on-page lever for AI citation — more impactful than word count, topical breadth, or body copy (source: [Aleyda Solis](https://www.linkedin.com/in/aleyda/), citing Kevin Indig × AirOps, LinkedIn post, April 2026).

Specific heading rules from an analysis of 6.8 million subheadings across 815,000 query-page pairs (source: [Kevin Indig](https://www.linkedin.com/in/kevinindig/), Growth Memo, 2025):

| Rule | Data |
|------|------|
| Use question-format H2–H4s | Question headings cited at **1.5x** rate of declarative headings |
| Keep headings 20–39 characters | 20–39 chars = **32.7%** citation rate peak |
| Avoid headings over 60 characters | 60+ chars = **6 percentage point drop** in citation rate |
| Avoid one-word headings (e.g., "Overview") | Sub-20 chars = poor matching |

**SOP step:** For each article, ensure 25–50% of your H2s are phrased as user questions. Example: "What does X cost?" beats both "Pricing" and "A complete breakdown of pricing options for X."

### 2.3 Write a Strong Introduction

We analyzed 1.2 million ChatGPT responses and found a simple pattern: **strong intros drive more citations** (source: [Kevin Indig](https://www.linkedin.com/in/kevinindig/), Growth Memo, 2025). Pages with headlines that directly answer the question get cited 41% of the time; pages with loosely related headlines drop to 29%.

**SOP step:** Every article introduction must do three things in the first 100 words:
1. State the core answer to the query directly
2. Include the primary keyword in a natural sentence
3. Give the reader a reason to continue (a number, a surprising fact, or a clear promise)

### 2.4 Use Primary Sources and Proprietary Data

LLMs cite content that contains information **not available anywhere else** (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, 2026). AI cited it because there was nothing else like it anywhere.

**The proprietary data moat framework (Nick Jordan):** A 60-second conversation with a subject matter expert is worth more to an LLM than a 3,000-word blog post rewritten from Google's page 1. Client case study: wealth management firm published content based on advisor call recordings → 3 articles got pulled into Google AI Overview → 3 demos followed at five-to-six figure deal sizes (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn post, 2026).

**SOP step:** For every article cluster, conduct at least one 15-minute SME interview. Extract objections, edge cases, and questions that come up repeatedly. Publish this under the expert's name. This is the content LLMs have nothing to compete with.

Additionally (source: [Nathan Gotch](https://nathangotch.com/), March 2026):
- Add dates, numbers, and definitions to every major claim
- Use primary sources (government data, peer-reviewed papers, original studies) not aggregators
- Include a "What changed / What to do next" section in every article

---

## Phase 3 — AI Production Pipeline

### 3.1 The Production Stack

Full-automation pipelines (keyword research → AI brief → AI draft → auto-publish) are operationally impressive but strategically fragile (see "What I Rejected and Why"). The correct stack is **AI-augmented, human-governed:**

```
1. KEYWORD CLUSTER (AI-assisted)
   → AI clustering tool groups keywords by semantic intent

2. BRIEF (AI-generated, human-reviewed)
   → Generate a brief: target heading structure, questions to answer,
     SME input needed, primary source to cite
   → Human reviews and adds proprietary data points from SME interview

3. DRAFT (AI-generated)
   → AI writes first draft following brief exactly
   → Heading format rules applied (question format, 20–39 chars)
   → Word count target: 500–2,000 words

4. EDIT (Human)
   → Add SME quotes/data
   → Strengthen introduction
   → Verify all claims against primary sources
   → Check heading structure against citation rules

5. PUBLISH
   → Clear URL structure reflecting topic intent
   → Internal links based on topical proximity map
```

### 3.2 What AI Does Well vs. Badly in Content Production

**AI does well:**
- Generating structured outlines from a heading template
- Writing neutral, factual summaries of well-documented topics
- Reformatting existing content (summaries, FAQs, alternative angles)
- Keyword clustering and gap analysis

**AI does badly:**
- Writing anything that requires a first-person expert perspective
- Generating novel insights not present in training data
- Producing content that will be uniquely citeable (by definition — if AI knows it, it's not proprietary)
- Maintaining consistent brand voice across a large content portfolio

### 3.3 Automation: What Actually Works

Full-stack automation is possible but creates a quality ceiling (source: [Julian Goldie](https://www.youtube.com/@JulianGoldieSEO), YouTube, 2025). The highest-ROI automation points are:

- **Internal linking:** AI analyzes site structure and inserts internal links based on topical proximity (source: [Nathan Gotch](https://rankability.com/), Rankability)
- **Keyword clustering:** Embedding-model-based clustering at scale
- **Brief generation:** Template-driven brief creation from keyword cluster inputs
- **Content decay alerts:** Automated GSC monitoring for pages losing impressions (source: [Aleyda Solis](https://www.linkedin.com/in/aleyda/), referencing GSC Wizard, LinkedIn post, 2026)

---

## Phase 4 — LLM Visibility (GEO)

### 4.1 What Actually Drives AI Citation (and What Doesn't)

Based on the AirOps × Growth Memo study (16,851 queries, 353,000+ pages):

**Signals that help:**
- Retrieval rank position (the #1 signal by far)
- Heading match to query (strong vs weak = 41% vs 29% citation rate)
- Focused subtopic coverage (26–50% beats 100%)
- Short-to-medium word count (500–2,000 words)
- Strong introduction

**Signals with no measurable positive effect:**
- Domain Authority (no positive correlation — slightly inverse)
- Backlink volume
- llms.txt — SE Ranking analyzed 300,000 domains and found no measurable link between having the file and getting cited by LLMs (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, citing SE Ranking data, 2026). Google confirmed: "It's just a text file for us" (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/what-we-learned-google-search-central-zurich-2025/), Google Search Central Zurich, December 2025)
- Robots.txt GPTBot/ClaudeBot rules (no citation effect)
- FAQPage schema (climbing in adoption but no demonstrated LLM citation benefit)

**SOP step:** Do not spend time on llms.txt, robots.txt AI-crawler rules, or AEO-specific schema until there is evidence these signals are weighted by LLMs. That time is better spent on the heading structure and proprietary data steps above.

### 4.2 Brand Trust Is the Long-Term Moat

LLMs don't respond to domain authority; they respond to whether your brand gets referenced in the real world (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026). You don't acquire your way into an LLM answer by building links or publishing more content. You get there by being a brand the world already talked about before you started optimizing.

Furthermore: LLMs are trained on everything people say about you — reviews, forums, Reddit threads. If you've prompted your way into a five-star recommendation but deliver a three-star experience, the feedback loop corrects itself faster than Google's ever did (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026).

**SOP step:** The non-content work that matters for LLM visibility:
- Build genuine backlinks (PR, partnerships, expert mentions) — these contribute to the reference corpus LLMs train on
- Manage reviews actively (G2, Trustpilot, Google) — this is now SEO
- Ensure expert authors have public profiles with real attribution
- Create content worth talking about, not just content worth indexing

### 4.3 Understand Query Fan-Out

When Google AI Mode receives a query, it generates **multiple sub-queries** (the "fan-out") and retrieves results for each before synthesizing an answer. A single page can be cited for queries it wasn't explicitly optimized for — if it covers related sub-topics that appear in the fan-out (source: [Aleyda Solis](https://www.aleydasolis.com/en/ai-search/google-query-fan-out/), May 2025).

**SOP step:** After completing an article, generate 5–10 related questions that a reader might ask next. Ensure your article addresses at least 3 of them. This is the practical application of the 26–50% subtopic coverage finding.

---

## Phase 5 — Measurement

### 5.1 Stop Reporting Traffic, Start Reporting Pipeline

Performance marketers present ROAS. SEOs present "traffic is trending positively." One of these people is getting budget next quarter (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, 2026).

**New measurement framework:**

| Old metric | New metric |
|------------|------------|
| Organic sessions | AI Overview appearances (GSC impressions by feature type) |
| Keyword rankings | Brand mention rate in LLM responses (query sampling) |
| Backlink count | Citation rate in target AI tools (manual sampling, 10 queries/week) |
| Page views | Pipeline attributed to organic (CRM UTM tracking) |

### 5.2 Track the SERP Share Shift

Monitor paid vs. organic vs. AI click share in your vertical quarterly. Use Similarweb or manual GSC sampling (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/serp-shifts-ads-remonetized/), February 2026). The headphones vertical lost 23 percentage points of organic click share in 12 months — knowing your vertical's trajectory tells you how urgently to shift production strategy.

---

## Where Experts Disagree

### Disagreement 1: Content Depth — Comprehensive vs. Focused

**What the traditional approach says (and what most content marketers still do):**
"Ultimate guides" and comprehensive content win because they signal expertise, earn more backlinks, and satisfy more search intent variants in one page.

**What Kevin Indig's data says:**
Pages covering 26–50% of ChatGPT's fanout sub-queries outperform pages covering 100%. The citation sweet spot is 500–2,000 words. "Build the page that is the best answer to one question. Not the page that adequately answers twenty." (source: [Kevin Indig](https://www.linkedin.com/in/kevinindig/), LinkedIn, Growth Memo, 2025)

**What Income School's longitudinal approach suggests:**
Depth within a niche is what drives long-term ad revenue (RPM) and return visitor rates. Surface-level content — even if it ranks — generates weak monetization signals (source: [Income School](https://www.youtube.com/@IncomeSchool), Project 24 methodology, incomeschool.com).

**My take: Kevin Indig wins for AI citation specifically; Income School wins for monetization.** These are not contradictory. Write focused, question-answering articles (500–2,000 words) for LLM citation and informational traffic. Write deeper, high-dwell-time articles for commercial clusters where you're monetizing via affiliate or display. Different content types, different optimization targets.

---

### Disagreement 2: Automation Level — Full Stack vs. Human-in-the-Loop

**What Julian Goldie advocates:**
Full-stack automation: keyword research → AI brief generation → AI draft → automated publishing via CMS integrations, with Zapier/Make connecting every step. The goal is maximum articles per hour of human input (source: [Julian Goldie](https://www.youtube.com/@JulianGoldieSEO), YouTube channel, 2025).

**What Nick Jordan advocates:**
Human-in-the-loop is non-negotiable because the content that gets cited by LLMs is content that contains **proprietary data** — information that doesn't exist anywhere else. That information only comes from SME interviews, internal call recordings, and founder expertise. No automation pipeline produces it (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, 2026).

**My take: Nick Jordan wins, and the data confirms it.** The SE Ranking study (300,000 domains) and the Kevin Indig citation research both point to content uniqueness and structural clarity as the citation signals that matter. Fully automated content is, by definition, derivative — it recombines what already exists. It cannot produce the proprietary insights that make LLMs cite you over anyone else. Julian Goldie's approach may still generate traffic from low-competition long-tail terms, but it creates no defensible moat.

---

### Disagreement 3: The Role of Backlinks and Domain Authority in AI Search

**What Matt Diggity's research shows:**
Backlinks still matter in AI search, but the nature of what matters has shifted. Nofollow links carry real weight in AI search visibility. Link quality and diversity outperform raw volume. Image links move the needle on domain authority in AI contexts (source: [Matt Diggity](https://diggitymarketing.com/news-roundup-oct-2025/), Diggity Marketing News Roundup, October 2025, citing Kevin Indig's 1,000-domain study).

**What Kevin Indig's citation study shows:**
Domain Authority shows no positive correlation with AI citation rate — and is slightly inversely correlated. Always-cited pages have lower DA than never-cited pages (source: [Kevin Indig](https://www.linkedin.com/in/kevinindig/), AirOps study, 815,000 query-page pairs, 2025).

**What Eli Schwartz argues:**
"Citations are not backlinks. You don't acquire your way into an LLM answer by building links or publishing more content." (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026)

**My take: The apparent contradiction resolves when you separate two questions.** Question 1: Does DA predict whether a page gets *retrieved* by an LLM? Answer: Weakly — DA contributes to traditional ranking which IS the #1 citation signal. Question 2: Does DA predict whether a *retrieved* page gets *cited*? Answer: No — Kevin Indig's data is clear on this. So backlinks matter for step 1 (getting retrieved) but content quality and structure determine step 2 (getting cited). Build links for rank; build content for citation. Both matter; neither alone is sufficient.

---

### Disagreement 4: Should You Optimize Specifically for GEO/AEO?

**What the AEO tooling industry says:**
Buy a GEO dashboard, track your AI mentions, optimize your llms.txt, add FAQPage schema, run targeted citation campaigns.

**What Eli Schwartz says:**
"Most AEO and GEO tools are a scam... Strip away the branding and the pitch deck language, and you're left with a UI layer on top of absolutely nothing." Use Ahrefs free instead — more data than most AEO tools (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026, in partnership with Ahrefs).

**What Nick Jordan's operational data shows:**
Every site they've gotten cited in AI Mode had the same thing in common: good content, structured clearly. Not a single .txt file in the mix (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, 2026).

**My take: Eli Schwartz and Nick Jordan are right, with one nuance.** Do not pay for AEO-specific tooling in 2026. The fundamentals of LLM citation are SEO fundamentals with heading structure optimization layered on. However, I would not dismiss GEO *thinking* entirely — the SEO vs GEO framework that Aleyda Solis documents (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/seo-vs-geo-optimizing-for-traditional-vs-ai-search/), June 2025) is a useful mental model for identifying where optimization areas diverge. The problem is the tooling industry, not the concept.

---

## What I Rejected and Why

### Rejection 1: Julian Goldie's Full-Stack Automation Pipeline

**What he recommends:** Connect keyword research → AI brief generation → AI content production → automated CMS publishing in a single pipeline with minimal human touchpoints. Maximize articles-per-hour-of-human-input.

**Why I rejected it:**

The pipeline is operationally impressive but strategically self-defeating at the current moment in AI search. There are two reasons:

**Reason A — Citation failure:** Kevin Indig's data shows that the pages which consistently win in LLM citation are ones with proprietary data, question-matched headings, and focused scope. A fully automated pipeline produces none of these by default. It recombines what already exists. LLMs are trained on that existing content. You are producing the least citable type of content at scale.

**Reason B — The feedback loop:** Eli Schwartz correctly identifies that LLMs train on everything written about you — including negative experiential reviews from users who got AI-generated content that felt hollow (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026). A content factory optimized for volume actively generates the negative signal corpus that corrects any initial AI visibility gains.

**What I kept from Julian Goldie:** Automation of the *operational* steps — brief templating, internal link suggestions, content decay alerts, publishing workflows. These are legitimate efficiency gains. The mistake is extending automation to the creative and editorial layer.

---

### Rejection 2: GEO-First, SEO-Second Framing

**What some practitioners argue:** GEO is a new discipline that should be the primary optimization target. SEO is legacy thinking. Optimize for AI citation first, traditional ranking second.

**Why I rejected it:**

Because the data says the opposite. Retrieval rank is the #1 LLM citation signal — position 1 gets a 58% citation rate, position 10 gets 14% (source: [Kevin Indig](https://www.linkedin.com/in/kevinindig/), AirOps study, 2025). You cannot get cited if you are not retrieved. You cannot be reliably retrieved if you do not rank. Google has stated directly: "There is no GEO without SEO" (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/what-we-learned-google-search-central-zurich-2025/), Google Search Central Zurich, December 2025). Nathan Gotch's framework explicitly positions GEO as building *on* SEO, not replacing it (source: [Nathan Gotch](https://nathangotch.com/), *AI SEO For Dummies*, Rankability).

The GEO-first framing also subtly encourages investment in the unproven tooling and technical signals (llms.txt, FAQPage schema, AI-specific robots.txt rules) that both Nick Jordan and Eli Schwartz have shown to have no measurable citation effect.

---

## My Original Ideas

### Idea 1: The Cite-Chain Architecture

**What it is:**

Every expert in this research has identified that getting cited in LLMs requires being *already talked about* (Eli Schwartz), having *proprietary data* (Nick Jordan), and *ranking highly* (Kevin Indig). None of them has operationalized how to deliberately engineer a compounding citation loop — I call it the **cite-chain**.

**How it works:**

The insight comes from Aleyda Solis's SERP re-monetization data: the only site that grew absolute organic clicks in the headphones vertical as AIO expanded was **YouTube** (178K → 244K clicks while brand sites collapsed) (source: [Aleyda Solis](https://www.aleydasolis.com/en/search-engine-optimization/serp-shifts-ads-remonetized/), February 2026). YouTube grew because videos get embedded in other content, cited in newsletters, referenced in forums — creating a citation corpus that pre-dates any specific optimization effort.

The cite-chain is a content architecture designed to replicate this effect in text format:

```
Step 1 — Create the primary source
  Publish original research: an SME interview, dataset, or case study
  that does not exist anywhere else.

Step 2 — Create a citable artifact
  Extract the most surprising/specific data point into a standalone
  resource (a table, a stat card, a named framework).
  Give it a proper name so it's referenceable.

Step 3 — Seed the citation network
  Publish the artifact in 3 different formats/channels:
  the original article, a LinkedIn post, and a community forum thread.
  This creates the "multiple independent sources" pattern that LLMs
  weight more heavily than a single authoritative source.

Step 4 — Wait for second-order citations
  Other content producers cite your data. LLMs train on their content.
  Your original data now exists in hundreds of documents in the
  training corpus, not just one. Citation probability compounds.
```

**Why it could work:**

Kevin Indig identified that LLM citation is probabilistic and context-sensitive — the same query produces different citations across runs (source: [Kevin Indig](https://www.growth-memo.com/p/how-much-can-we-influence-ai-responses), Growth Memo, January 2026). The cite-chain increases your probability mass across that distribution by being present in multiple independent documents in the training corpus, not just one highly-optimized page. Eli Schwartz's feedback loop insight confirms this works in both directions — negative experiences compound negatively, so positive citation experiences should compound positively by the same mechanism.

**What I have not proven:** Whether the lag between publishing and LLM training data cutoffs makes this operationally impractical for real-time optimization. This is the biggest unknown.

---

## Weaknesses of This Playbook

**1. The citation data is ChatGPT-specific.**
Kevin Indig's AirOps study — the most rigorous dataset in this research — analyzes ChatGPT's retrieval pipeline specifically. The heading format rules, subtopic coverage findings, and word count sweet spots may not transfer identically to Gemini, Claude, or Perplexity. Each model has different retrieval architecture and training data. This playbook assumes generalizability that has not been empirically confirmed across all LLMs.

**2. Everything has a 6-month shelf life.**
Aleyda Solis's SERP data showed a 23 percentage point organic click share shift in 12 months in a single vertical. Matt Diggity documented AIO expansion from 2.28% to 32.76% in 12 months. The AI search landscape is moving faster than any playbook can track. Specific numbers in this document (citation rates, click share percentages, heading character counts) should be treated as directionally correct, not permanently valid. Re-validate quarterly.

**3. The SME interview approach does not scale easily.**
Nick Jordan's proprietary data moat framework is compelling and the case study is real (source: [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/), LinkedIn, 2026). But conducting genuine SME interviews for every content cluster at scale requires either significant time investment or a large enough team to systematize expert knowledge extraction. For solo operators or small teams producing 100+ articles per month, this is a constraint that limits the strategy's applicability.

**4. Income School's longitudinal data is not yet conclusive.**
The most important unanswered question in AI content production is: what happens to a site's revenue 18–24 months after switching fully to AI-generated content? Income School is the only practitioner tracking this with real revenue data and no-backlink controls (source: [Income School](https://www.youtube.com/@IncomeSchool), Project 24 methodology). As of April 2026, they have not published conclusive results. This playbook cannot tell you with confidence whether AI content is sustainable over multi-year horizons.

**5. The original ideas section is untested.**
The cite-chain architecture is my synthesis, not a validated framework. No practitioner in this research has published data on whether deliberately engineering a multi-platform citation corpus produces measurable LLM citation rate improvements. Treat it as a hypothesis to test, not a proven method.

**6. Eli Schwartz has a conflict of interest in Post 1.**
His strongest "AEO tools are a scam" post explicitly promotes Ahrefs and is labeled "In partnership with Ahrefs" (source: [Eli Schwartz](https://www.linkedin.com/in/schwartze/), LinkedIn, 2026). His core argument is correct — I believe it and so does the data — but readers should know the post was sponsored. His other posts on this topic (Posts 2–5) are not sponsored and make the same argument, which increases confidence in the underlying position.

---

## Who I Would NOT Recommend Following and Why

### Primary: Julian Goldie

**The content:**
Julian Goldie publishes extremely high-frequency YouTube content — multiple videos per week, each documenting an AI SEO automation workflow. Operationally, the videos are detailed screen-share tutorials showing how to connect tools (Claude/ChatGPT → Surfer → Zapier → WordPress) into automated content pipelines.

**Why I would not recommend him as a primary source:**

**1. His framework optimizes for the wrong metric.**
Julian's success metric is articles-per-hour-of-human-input. The data in this research consistently shows that what gets cited, what drives sustainable revenue, and what survives algorithm updates is *content quality and uniqueness* — which are inversely related to production velocity. Following Julian's primary framework leads you toward a local maximum: high output, low defensibility. The practitioners whose data I trust most (Kevin Indig, Nick Jordan, Eli Schwartz, Income School) all point away from this approach.

**2. The signal-to-noise ratio on his channel is poor.**
Publishing 3–5 videos per week means most of the content is reactive — testing tools that launched days ago, covering trends that haven't matured. This isn't inherently bad for entertainment, but it is bad for a research base. A practitioner who publishes less frequently but with more data (Kevin Indig, Aleyda Solis, Matt Diggity's monthly roundups) produces more durable insights per hour of your reading time.

**3. The absence of longitudinal data.**
Julian does not publish long-term outcome data from his automation workflows — traffic trajectories, revenue figures, or ranking stability over 12+ months. The practitioners who do (Income School, Gael Breton, Matt Diggity) consistently show that production methodology alone doesn't predict long-term outcomes. Without this data, Julian's approach is unvalidated at the time horizon that matters most.

**What he is useful for:**
Julian Goldie is a genuinely useful source for *tool integration tutorials* — if you want to know how to connect Zapier to your CMS or build a no-code content brief generator, his channel is practically valuable. The mistake is using him as a *strategic* source.

---

### Secondary note: Koray Tuğberk GÜBÜR (conditional)

Koray is one of the highest-signal researchers in this corpus — his topical authority framework is intellectually rigorous and his case study data is real. I am **not** removing him from the expert roster. However, his methodology is significantly more technically demanding than most practitioners can implement: Python-scripted entity mapping, custom semantic gap analysis, and deep reading of Google patents. For solo operators or small content teams, following Koray without the technical infrastructure to execute his system produces cargo-cult results — people who build "topical maps" in spreadsheets and call it semantic SEO. **Only follow Koray if you can actually implement what he teaches.**

---

## Quick-Reference Checklist

Before publishing any article, verify:

- [ ] Targets a commercial or transactional cluster (not pure informational)
- [ ] Covers 30–50% of related sub-queries (focused, not exhaustive)
- [ ] Word count: 500–2,000 words
- [ ] 7–20 subheadings
- [ ] 25–50% of H2s are question-format
- [ ] All headings: 20–39 characters
- [ ] Introduction answers the core query in the first 100 words
- [ ] At least one data point, quote, or insight not available elsewhere (proprietary)
- [ ] Primary sources cited (not aggregators)
- [ ] Internal links based on topical proximity
- [ ] Expert attribution if using SME interview content

---

## Source Index

All sources cited in this playbook:

| Expert | Source Type | URL |
|--------|-------------|-----|
| Aleyda Solis | Blog (May 2025) | https://www.aleydasolis.com/en/search-engine-optimization/ai-search-trends/ |
| Aleyda Solis | Blog (June 2025) | https://www.aleydasolis.com/en/search-engine-optimization/seo-vs-geo-optimizing-for-traditional-vs-ai-search/ |
| Aleyda Solis | Blog (May 2025) | https://www.aleydasolis.com/en/ai-search/google-query-fan-out/ |
| Aleyda Solis | Blog (Feb 2026) | https://www.aleydasolis.com/en/search-engine-optimization/serp-shifts-ads-remonetized/ |
| Aleyda Solis | Blog (Dec 2025) | https://www.aleydasolis.com/en/search-engine-optimization/what-we-learned-google-search-central-zurich-2025/ |
| Aleyda Solis | LinkedIn (Apr 2026) | https://www.linkedin.com/in/aleyda/ |
| Kevin Indig | LinkedIn + Growth Memo (2025) | https://www.linkedin.com/in/kevinindig/ + https://www.growth-memo.com/ |
| Kevin Indig | Growth Memo (Jan 2026) | https://www.growth-memo.com/p/how-much-can-we-influence-ai-responses |
| Nick Jordan | LinkedIn (2026) | https://www.linkedin.com/in/nickfromseattle/ |
| Eli Schwartz | LinkedIn (2026) | https://www.linkedin.com/in/schwartze/ |
| Koray Tuğberk GÜBÜR | YouTube + Blog | https://www.youtube.com/@TopicalAuthority + https://www.holisticseo.digital/ |
| Matt Diggity | Blog (Oct 2025) | https://diggitymarketing.com/news-roundup-oct-2025/ |
| Nathan Gotch | Website + Book | https://nathangotch.com/ + *AI SEO For Dummies* |
| Julian Goldie | YouTube | https://www.youtube.com/@JulianGoldieSEO |
| Income School | YouTube | https://www.youtube.com/@IncomeSchool |

---

*This playbook will be updated as new data becomes available. Last validated: April 2026.*
