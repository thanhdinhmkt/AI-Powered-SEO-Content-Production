# Loom Video Script — AI-Powered SEO Content Production
## 100Hires Final Assessment | Target: 12–14 minutes

---

> **HOW TO USE THIS SCRIPT**
> - `[SCREEN]` = what to have visible on screen at that moment
> - `[SAY]` = your spoken words (read naturally, not robotically)
> - `[PAUSE]` = natural beat — scroll, click, or breathe
> - Estimated time per section is shown in brackets
> - Rehearse once before recording. You do not need to match this word-for-word.

---

## INTRO — [0:00–0:45]

`[SCREEN: Desktop, nothing open yet. Open Loom, face visible in corner.]`

`[SAY:]`
"Hi — I'm Thanh. This is my walkthrough for the 100Hires assessment.

The project is a research-to-playbook pipeline on AI-powered SEO content production. I'll walk you through the structure, show you exactly how I used AI tools to build it, trace how specific sources shaped specific decisions, and at the end explain how I'd apply all of this to real work at 100Hires — not in theory, but in the next two weeks with specific outputs.

Let's start with the repo."

---

## SECTION 1 — Repo Structure [0:45–2:30]

`[SCREEN: Open browser → https://github.com/thanhdinhmkt/AI-Powered-SEO-Content-Production]`

`[SAY:]`
"Here's the repository. The structure follows the brief exactly, but the organisation reflects a specific logic — not just compliance.

The root has two key files: README and PLAYBOOK. Everything else feeds into those two."

`[SCREEN: Click into /research folder, show the 4 subdirectories]`

`[SAY:]`
"Inside /research: four directories.

**sources.md** — this is the anchor document. Ten experts, each with a full annotation: why I picked them, what research focus they cover, what I actually collected, and when. It's not a list of names — it's a sourcing rationale.

**linkedin-posts** — four experts whose primary publishing channel is LinkedIn. I collected these manually because LinkedIn has no public API. Twenty posts total, cleaned and formatted, with researcher notes at the bottom of each file synthesising what themes are emerging.

**youtube-transcripts** — six creators. The transcripts couldn't be fetched from a cloud environment because YouTube returns 403s to non-browser requests. So what's here is channel intelligence: methodology summaries, known video IDs pre-seeded, and a fetch script you run locally."

`[SCREEN: Click scripts/fetch_transcripts.py briefly]`

`[SAY:]`
"That's this script. It auto-discovers the five most recent videos per channel via yt-dlp, merges them with the pre-seeded IDs, fetches transcripts, and saves them as markdown. Idempotent — you can re-run it without duplicating files.

**other** — blog articles and newsletter content. Aleyda Solis's six blog posts with data points extracted. Kevin Indig's Growth Memo synthesis including the full AirOps study data table."

`[SCREEN: Click PLAYBOOK.md]`

`[SAY:]`
"And PLAYBOOK.md — this is the deliverable. Everything in the research directory is input to this file. Let me show you how."

---

## SECTION 2 — How I Used AI Tools [2:30–4:30]

`[SCREEN: Open Cursor IDE or VS Code with the repo loaded, or show terminal + Claude]`

`[SAY:]`
"Let me show you how AI was actually part of this workflow — not as a black box that generated the output, but as a specific tool at specific stages.

There were three places AI added real value."

`[SCREEN: Show the research/other/kevin-indig/growth-memo-articles.md file]`

`[SAY:]`
"**First — source synthesis.** I used Claude to help me read and organise 15+ sources simultaneously. The prompt I ran was essentially: 'Here are five LinkedIn posts from Kevin Indig on LLM citation mechanics. Extract every specific data point — sample sizes, percentages, methodology details — and flag any internal contradictions.' 

This let me build the data table you see here — 16 signals from the AirOps study, each with a specific metric — in a fraction of the time manual extraction would take."

`[SCREEN: Scroll to the heading structure rules table in PLAYBOOK.md]`

`[SAY:]`
"**Second — cross-source pattern matching.** I had Aleyda Solis sharing Kevin Indig's study in a LinkedIn post, Kevin Indig sharing it in his newsletter, and Matt Diggity citing a related study in his monthly roundup. Three different framings of overlapping data. I prompted Claude: 'These three sources all reference similar research. What are the exact points where they agree, where they diverge, and where the framing obscures a real difference?' That's how the 'Where Experts Disagree' section got structured — not from me already knowing the answers, but from using AI to surface the tension."

`[SCREEN: Show the scripts/fetch_transcripts.py file]`

`[SAY:]`
"**Third — scripting.** The transcript fetcher was written with Claude Code. I gave it the spec: six channels, pre-seeded video IDs, merge with auto-discovery, idempotent re-runs, write failed stubs so we know what to retry. It handled the implementation. I reviewed and corrected one bug in the yt-dlp output parsing — it was splitting on pipe characters that appeared in video titles. That's the right relationship with AI code generation: you spec it, it drafts, you catch the edge cases."

---

## SECTION 3 — How Sources Shaped the Playbook [4:30–7:00]

`[SAY:]`
"Now let me show you three specific moments where a source directly changed what's in the playbook."

`[SCREEN: Open research/linkedin-posts/kevin-indig/posts.md — scroll to Post 3 on comprehensive content]`

`[SAY:]`
"**Source one: Kevin Indig, LinkedIn Post 3.**

This post challenged the most deeply held assumption in SEO content production — that comprehensive, long-form content wins. His study of 815,000 query-page pairs found the opposite: pages covering 26 to 50 percent of related sub-queries get cited more than pages covering everything.

That finding directly produced this rule in the playbook."

`[SCREEN: Switch to PLAYBOOK.md, scroll to Section 2.1 — 'Write Focused Articles']`

`[SAY:]`
"'Write the page that is the best answer to one question. Not the page that adequately answers twenty.' 500 to 2,000 words. 30 to 50 percent subtopic coverage. That's not an opinion — it's that dataset applied directly."

`[PAUSE — scroll]`

`[SCREEN: Open research/linkedin-posts/nick-jordan/posts.md — scroll to Post 4, the SME case study]`

`[SAY:]`
"**Source two: Nick Jordan, LinkedIn Post 4.**

Nick documented a specific client case: wealth management firm, advisors' call recordings turned into published content, three articles appeared in Google AI Overview, three demos followed. This is not a theoretical argument — it's a result with attribution.

That case study produced the most operationally specific recommendation in the playbook."

`[SCREEN: Switch to PLAYBOOK.md, scroll to Section 2.4 — 'Use Primary Sources and Proprietary Data']`

`[SAY:]`
"'A 60-second conversation with a subject matter expert is worth more to an LLM than a 3,000-word blog post rewritten from Google's page 1.' That framing is his, the case study is his, and the SOP step — conduct at least one 15-minute SME interview for every article cluster — comes directly from it."

`[PAUSE]`

`[SCREEN: Open research/other/aleyda-solis/blog-articles.md — scroll to Article 4, the Feb 2026 SERP data]`

`[SAY:]`
"**Source three: Aleyda Solis, February 2026.**

This is the most important data in the whole research corpus. Aleyda used Similarweb to track what actually happened to click share in the headphones vertical over 12 months. Organic dropped 23 percentage points. Paid more than doubled. YouTube was the only site that grew absolute clicks.

That data drove the core philosophy section of the playbook — why we prioritize commercial and transactional queries first, and why multi-format content is the only resilient strategy long-term."

`[SCREEN: Switch to PLAYBOOK.md, scroll to Core Philosophy section]`

`[SAY:]`
"You can see it cited directly here — source, date, URL. Every claim in this playbook traces back to a named source. That was a hard constraint I set for myself."

---

## SECTION 4 — Where Experts Contradicted Each Other [7:00–8:30]

`[SCREEN: PLAYBOOK.md — scroll to 'Where Experts Disagree', Disagreement 2]`

`[SAY:]`
"The disagreement I find most interesting — and most important to resolve correctly — is the automation depth debate.

Julian Goldie argues for full-stack automation: keyword research feeds into AI brief generation, which feeds into AI content production, which publishes automatically. Maximise articles per hour of human input.

Nick Jordan argues the opposite: the content that gets cited by LLMs contains proprietary data — things that don't exist anywhere else. That information only comes from SME interviews, internal call recordings, founder expertise. No automation pipeline produces it by definition.

I sided with Nick Jordan, and here's why I'm confident about it."

`[SCREEN: Scroll to the resolution paragraph under Disagreement 2]`

`[SAY:]`
"Kevin Indig's dataset shows that citation probability correlates most strongly with content uniqueness and structural clarity. A fully automated pipeline produces derivative content by design — it recombines what already exists in training data. It is, literally, the least citable type of content you can produce at scale.

There's also Eli Schwartz's feedback loop point. LLMs train on everything written about you — including negative reviews from users who got hollow AI-generated content. So the automation approach doesn't just produce weak content. It actively generates the negative training corpus that corrects any initial AI visibility gains.

Julian Goldie is useful for tool integration tutorials. He is not a good strategic source, and I explain that in the 'Who Not to Follow' section."

---

## SECTION 5 — My Original Idea [8:30–10:00]

`[SCREEN: PLAYBOOK.md — scroll to 'My Original Ideas' section]`

`[SAY:]`
"The original idea is what I'm calling the Cite-Chain Architecture.

Every expert in this research identified what you need for LLM citation: Eli Schwartz says you need to already be talked about in the real world. Nick Jordan says you need proprietary data. Kevin Indig says you need to rank. None of them operationalised how to deliberately engineer a compounding citation loop.

The insight that unlocked it came from Aleyda Solis's SERP data. The only site that grew absolute organic clicks in the headphones vertical as AI Overviews expanded was YouTube. Not a brand site. Not a publisher. YouTube — because videos get embedded, cited in newsletters, referenced in forum threads. They exist in multiple independent documents in the training corpus.

The cite-chain replicates that in text. Four steps."

`[SCREEN: Scroll to the cite-chain four-step block]`

`[SAY:]`
"First: create original research — an SME interview, a dataset, a named case study. Something that does not exist anywhere else.

Second: extract the most surprising data point and give it a proper name. 'The Fan-Out Citation Gap' or 'The Proprietary Data Moat' — something referenceable.

Third: publish it in three formats simultaneously. The original article, a LinkedIn post, a community forum thread. This creates the multi-source pattern.

Fourth: wait for second-order citations. Other content producers reference your data. LLMs train on their content. Your original data now exists in hundreds of documents in the training corpus, not just one.

Why does this work? Kevin Indig showed LLM citation is probabilistic — the same query produces different citations across runs. Increasing your presence across multiple independent documents raises your probability mass across that distribution.

What I haven't proven: whether the lag between publishing and LLM training cutoffs makes this impractical at short time horizons. That's in the weaknesses section. I flag my own unknowns."

---

## SECTION 6 — Who I Would Not Recommend Following [10:00–11:15]

`[SCREEN: PLAYBOOK.md — scroll to 'Who I Would NOT Recommend' section]`

`[SAY:]`
"Julian Goldie. And I want to be specific about the reasoning, because it's not a personality critique — it's a structural one.

His content optimises for the wrong metric. Articles per hour of human input is a production efficiency metric. The research consistently shows that what gets cited, what drives sustainable revenue, and what survives algorithm updates is content quality and uniqueness. Those are inversely related to production velocity at scale.

The second problem is no longitudinal data. Julian does not publish 12-month or 24-month outcome data from his automation workflows — traffic trajectories, revenue figures, ranking stability. The practitioners who do — Income School, Gael Breton, Matt Diggity — consistently show that production methodology alone doesn't predict long-term outcomes. Without that data, his approach is unvalidated at the time horizon that matters most.

He is genuinely useful for one thing: tool integration tutorials. If you want to know how to connect Zapier to your CMS, his channel is the fastest way to learn it. The mistake is treating him as a strategic source.

I also flag Koray Tuğberk GÜBÜR — not to remove him from the roster, he's the most intellectually rigorous researcher in the corpus — but with a condition. His methodology requires Python-scripted entity mapping and real technical infrastructure. Most practitioners who follow him build 'topical maps' in spreadsheets and call it semantic SEO. Follow him only if you can actually execute what he teaches."

---

## SECTION 7 — Applying This to 100Hires in 2 Weeks [11:15–13:30]

`[SCREEN: Open 100hires.com in browser]`

`[SAY:]`
"100Hires is an AI-powered ATS for small and medium businesses. The product does candidate ranking, multi-channel outreach, automated follow-ups, job board distribution, resume parsing. The marketing challenge is specific: help HR managers and founders at SMBs find this product when they're searching for solutions to real hiring problems.

Here's exactly what I would do in two weeks, applying this playbook."

`[SCREEN: Keep 100hires.com visible, or switch to a notes file]`

`[SAY:]`
"**Week 1 — Map and build the proprietary data asset.**

Day 1 and 2: Run an AI keyword clustering pass on the entire hiring/ATS keyword space. Not for volume — for intent clusters. Separate the informational queries — 'what is an ATS', 'how does resume parsing work' — from the commercial clusters — 'best ATS for small business', 'ATS with Indeed integration', 'hiring software under 100 dollars a month'. The playbook is clear: commercial clusters first.

Day 3: Conduct one 15-minute interview with a 100Hires sales rep or customer success person. The goal is to extract the three objections that come up on every call and the edge cases that differentiate customers who get results from those who don't. That's proprietary data — it does not exist anywhere on the internet.

Day 4 and 5: Write two focused articles — 500 to 1,500 words each — targeting the highest-priority commercial clusters. Use the heading structure rules from the playbook: question-format H2s, 20 to 39 characters. Every major claim supported by a number or a named source. Strong intro that answers the query in the first 100 words."

`[PAUSE]`

`[SAY:]`
"**Week 2 — Distribute and seed the cite-chain.**

Publish both articles. Then take the most surprising specific finding from the sales interview — one insight that HR managers don't know — and publish it in three places: a LinkedIn post under a 100Hires team member's name, a comment thread in an HR community on Reddit or a Slack group, and a short paragraph in an outreach email sequence.

The goal is to get that insight into multiple independent documents so it enters LLM training data as a signal associated with 100Hires.

Measure week over week: GSC impressions by query, AIO appearances for target queries, and — critically — whether the articles generate any demo requests. Not traffic. Pipeline.

By the end of two weeks: two published articles with clean citation architecture, one proprietary data asset from internal knowledge, and the beginning of a cite-chain seeded across three channels."

`[SCREEN: Switch back to face / Loom camera only]`

`[SAY:]`
"That's the playbook applied. Not in theory — in a specific sequence with specific outputs and a specific metric.

The research is at github.com/thanhdinhmkt/AI-Powered-SEO-Content-Production. The playbook is in PLAYBOOK.md. Happy to defend any of these decisions in a live session.

Thanks for your time."

---

## TIMING REFERENCE

| Section | Target Time | Buffer |
|---------|-------------|--------|
| Intro | 0:00–0:45 | 45s |
| Repo structure | 0:45–2:30 | 1m 45s |
| AI tools workflow | 2:30–4:30 | 2m |
| Sources → Playbook | 4:30–7:00 | 2m 30s |
| Expert disagreement | 7:00–8:30 | 1m 30s |
| Original idea | 8:30–10:00 | 1m 30s |
| Who not to follow | 10:00–11:15 | 1m 15s |
| 100Hires application | 11:15–13:30 | 2m 15s |
| **Total** | **~13:30** | **within 10–15min ✅** |

---

## PRE-RECORDING CHECKLIST

**Browser tabs to have open (in order):**
1. `https://github.com/thanhdinhmkt/AI-Powered-SEO-Content-Production` (repo home)
2. `/research/linkedin-posts/kevin-indig/posts.md` (on GitHub)
3. `/research/linkedin-posts/nick-jordan/posts.md` (on GitHub)
4. `/research/other/aleyda-solis/blog-articles.md` (on GitHub)
5. `PLAYBOOK.md` (on GitHub)
6. `https://100hires.com`

**Code editor:** Have the repo cloned locally and open in Cursor or VS Code, with `scripts/fetch_transcripts.py` visible.

**Things to avoid:**
- Do not read the script verbatim — speak the ideas, not the sentences
- Do not say "um" more than once per section — pause instead
- Do not apologise for the transcript gap — explain it confidently (403 from cloud environments is a real technical constraint, not a gap in effort)
- Do not rush Section 7 — this is what the recruiter actually cares about most

**Tone calibration:**
- Sections 1–2: technical, calm, showing competence
- Section 3: engaged, specific — "here's exactly where this came from"
- Section 4: confident, willing to take a side
- Section 5: intellectually alive — this is your idea, show some energy
- Section 6: direct, not apologetic
- Section 7: practical, grounded — "here's what I would actually do"
