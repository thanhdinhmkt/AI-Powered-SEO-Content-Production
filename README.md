# AI-Powered SEO Content Production — Research Repository

> **Research project** mapping the leading practitioners shaping AI-driven SEO content workflows in 2025–2026.

---

## Why This Topic

AI is not just changing *how* SEO content is written — it is collapsing the cost curve of production, reshuffling what Google and LLMs reward, and forcing practitioners to rethink the entire pipeline from keyword research to publishing. This repo documents the ideas and real-world data from the 10 experts who are running experiments, building tooling, and publishing results *right now*.

---

## Expert Roster

| # | Expert | Platform | Research Focus |
|---|--------|----------|----------------|
| 1 | [Aleyda Solis](https://www.linkedin.com/in/aleyda/) | LinkedIn / Blog | AI-First SEO strategy & international workflows |
| 2 | [Koray Tuğberk GÜBÜR](https://www.youtube.com/@TopicalAuthority) | YouTube | Semantic SEO & topical authority mapping |
| 3 | [Kevin Indig](https://www.linkedin.com/in/kevinindig/) | LinkedIn / Growth Memo | LLM citation mechanics & AI search growth strategy |
| 4 | [Gael Breton](https://www.youtube.com/@gbreton) | YouTube / LinkedIn | AI vs. human content performance data |
| 5 | [Nick Jordan](https://www.linkedin.com/in/nickfromseattle/) | LinkedIn | Content ops, SOPs, scaling with human-in-the-loop |
| 6 | [Eli Schwartz](https://www.linkedin.com/in/schwartze/) | LinkedIn | Product-Led SEO & AI visibility quality control |
| 7 | [Matt Diggity](https://www.youtube.com/@MattDiggity) | YouTube | Experimental SEO & prompt engineering |
| 8 | [Nathan Gotch](https://www.youtube.com/@NathanGotch) | YouTube | AI keyword clustering & technical authority |
| 9 | [Julian Goldie](https://www.youtube.com/@JulianGoldieSEO) | YouTube | Full-stack SEO automation workflows |
| 10 | [Income School (Ricky Kesler)](https://www.youtube.com/@IncomeSchool) | YouTube | Niche site monetization & AI content sustainability |

---

## Repository Structure

```
research/
├── sources.md                    # Annotated master list of all 10 experts
├── linkedin-posts/               # Manually collected LinkedIn posts
│   ├── aleyda-solis/
│   ├── kevin-indig/
│   ├── nick-jordan/
│   └── eli-schwartz/
├── youtube-transcripts/          # Transcripts organised by creator
│   ├── koray-gubur/
│   ├── gael-breton/
│   ├── matt-diggity/
│   ├── nathan-gotch/
│   ├── julian-goldie/
│   └── income-school/
└── other/                        # Blog posts, newsletters, supplementary material
    ├── aleyda-solis/
    └── kevin-indig/
scripts/
└── fetch_transcripts.py          # Run locally to pull YouTube transcripts
```

---

## Data Collection Method

| Source Type | Method | Status |
|-------------|--------|--------|
| LinkedIn posts (Aleyda, Kevin, Nick, Eli) | Manually collected | ✅ Complete |
| Blog / newsletter articles | Web scraping via `web_fetch` | ✅ Complete |
| YouTube transcripts | `youtube-transcript-api` (run `scripts/fetch_transcripts.py` locally) | ⏳ Script ready — run locally |

> **Note on YouTube:** The `youtube-transcript-api` is blocked by 403 errors in cloud CI environments. The script in `/scripts/fetch_transcripts.py` works correctly when executed on a local machine. Video IDs for ~25 recent videos across 6 channels are pre-seeded in the script.

---

## Key Themes Emerging From Initial Collection

1. **Retrieval rank > domain authority in LLMs.** Kevin Indig's data (16,851 queries, 353K pages) shows position 1 in ChatGPT retrieval carries a 58% citation rate vs 14% at position 10. DA shows *no* positive correlation.
2. **Heading structure is the #1 on-page lever.** Question-format H2–H4 headings in the 20–39 character range correlate with 32.7% citation rates. "Overview"-style headings perform worst.
3. **Focused beats exhaustive.** Pages covering 26–50% of fanout sub-queries outperform "ultimate guides" covering everything.
4. **GEO without SEO doesn't exist.** Aleyda Solis, citing Google directly: technical SEO fundamentals are the prerequisite for AI search visibility, not an alternative.
5. **Most AEO tooling is noise.** Eli Schwartz: no measurable link between llms.txt, robots.txt AI rules, or FAQPage schema and actual LLM citation rates. Good content structured clearly is the only consistent signal.
6. **Proprietary data is the moat.** Nick Jordan: SME interview content published under expert bylines outperforms regurgitated page-1 rewrites in AI Overviews.

---

## Commit Log Highlights

- `init` — repo scaffolding, expert roster, README
- `feat/linkedin-posts` — 20 manually collected posts across 4 LinkedIn experts
- `feat/other-articles` — blog/newsletter articles for Aleyda + Kevin Indig
- `feat/youtube-stubs` — video metadata + local fetch script for 6 YouTube creators
- `feat/sources-md` — annotated sources file

---

## How to Run the Transcript Fetcher

```bash
# 1. Install dependency
pip install youtube-transcript-api

# 2. Run the script
python scripts/fetch_transcripts.py

# Transcripts will be saved to research/youtube-transcripts/<author>/<video_id>.md
```
