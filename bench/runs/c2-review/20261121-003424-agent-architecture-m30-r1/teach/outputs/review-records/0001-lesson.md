# Review record: lesson 0001, context and memory in an agent

Two review passes ran; the second ended with `Verdict: revise`, so the limit of two passes stopped the loop. I fixed every factual and example finding from pass 2 before writing the final file, but did not run a third review.

## Pass 1 (verdict: revise)
- Memory tool cited to the wrong page: now cited to the context-management announcement.
- "Removes old results that can be fetched again" attributed to the feature: reworded as the lesson's own advice.
- "Their BM25 method": now "BM25 keyword matching", explained as a standard method.
- Prompt caching missing from cost story: added a paragraph with a link.
- Wasted-token arithmetic was 12,000 but the example gives 15,000: recomputed (4.5 cents, 45 dollars).
- Figure 1 bars not to scale: redrawn.
- Section 1 opener was a transition: rewritten to give its point.
- Misconceptions lacked cases: added a Monday/Wednesday case, a "bigger window" cost case and a real search exchange.
- Narrated sources ("Anthropic puts...", "describes..."): reworded to say the idea, then cite.
- No hint before answers: added a hint to "Your turn".
- Window size and overflow missing: added a docs-backed size and a trace where call 3 would not fit.
- Too short (~23 min): added a summarize-and-restart case, an E-204 case, a design-choices list, a recap and a Dev trace.
- Real-world why only at the top: added to the summary.
- Quiz 0002 referenced but absent: written.

## Pass 2 (verdict: revise)
Fixed:
- Caching link now points to the prompt caching docs.
- "1 to 1.5%" changed to percentage points.
- The 6,000-token window example now names call 3, not call 4.
- "About 3,700" changed to 3,650 and noted as excluding fixed text.
- Manual page size made consistent (70 pages of 3,000 tokens).
- Dev trace now saves a stable, dated preference, not a booking.
- Calendar check rewritten with a clear scenario; weak feedback on two options improved.

Not changed, by choice:
- Some paragraphs run to four sentences, and the example-before-idea order is only partly met; the lesson is long because the learner asked for 30 minutes.
- The retrieval part is still dense; BM25 and the percentages were kept short but not moved out.
- The 35% figure is described as "failed retrievals" without defining the measure (top-20 failure).
- The Go further link to anthropic.com/news/context-management redirects but works.
