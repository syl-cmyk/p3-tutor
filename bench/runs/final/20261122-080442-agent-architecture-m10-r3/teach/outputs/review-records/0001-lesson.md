# Review record: lesson 0001, context and memory (O3, 10 minutes)

Two review passes ran. The second ended with `Verdict: revise`; I stopped because two passes is the limit.

## Pass 1 (verdict: revise)
- Tokens per page clashed with the manual's size. Fixed the rule of thumb later (see pass 2).
- First-call size differed between Part 1 (about 1,010) and the booking trace (2,000). Fixed: the trace now says the booking prompt is longer and has a third tool.
- Caching ignored in the 8,800 count. Fixed: "before any caching discount".
- Meta hedges ("my own reasoning", "same source") and the "Recap" lines. Removed; the "same source" became a real link.
- Misconceptions without examples. Added a training example and the 3D printer chunk "PLA speed: 60 mm/s" for wrong-machine retrieval.
- "Your turn" steps did not map to items (a) to (c). Relabelled; the given step is now explicit.
- Dead script. Removed.
- Memory defined as only notes. Now covers notes and retrieval as two kinds of memory.
- Too long. Shortened all four captions and removed a filler sentence.
- Not changed: definitions come before the example in Parts 3 and 4, and part titles stay as the plan has them. The plan fixed both, and the titles are used word for word.

## Pass 2 (verdict: revise)
- Token-per-page figure is uncited. Fixed: now only "750 tokens is about a page and a half", from the three-quarters-of-a-word rule.
- "Starts before the window is full" is not in the source. Reworded to "grows as the text grows".
- The 200,000-token tip contradicted the retrieval example. Fixed: it now says the assistant has many manuals and pays per step, so retrieval is the safer default.
- Figure 4 label awkward. Fixed.
- Item (c) ambiguous. The solution now says why it is not notes.
- Not changed, with reasons: the length estimate of about 2,080 words (1.39 times the request, inside the 1.5 limit) is only partly trimmed, because the SVG text and worked examples carry the learner's preferred real-text traces. The "Context between steps" and "Context budgeting" titles stay as the plan's titles.
