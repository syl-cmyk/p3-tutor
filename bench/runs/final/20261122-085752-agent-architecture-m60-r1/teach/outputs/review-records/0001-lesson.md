# Review record: lesson 0001, context and memory (O3, 60 minutes)

Review passes run: 1. The reviewer's verdict was "fix"; I applied the fixes below and did not run a second pass, so the final file has not been re-reviewed.

## Pass 1 findings and what changed

Fixed:
- Token definition was attributed to the pricing FAQ, which does not say it: reworded as the lesson's own plain-words version.
- The 100 tokens = 75 words rule may undercount for Claude tokenizers: added a line saying newer tokenizers can produce about 30% more tokens, citing the pricing page.
- "Rounded" 500 tokens a page was not rounding: now says it is a clean-arithmetic choice and a real manual may run higher.
- Wrong feedback on the part 1 check (option 1,420): corrected to say it drops the 50-token question.
- The 1,430 was called "instructions and tools" (it also holds the question): compaction step and Figure 3 now use 1,400; the part 5 session trace says it includes Riley's first message.
- Tool descriptions omit the memory and training tools: closing "Why it matters" note says real windows run a bit above the round numbers.
- Opening lead stated the win only for the learner's project: now states it in general terms.
- "Memory means the model learned something" had no real case: added the delete-riley.md test.
- No real-world reason at the end: added a "Why it matters" line to the summary.

Not changed, with reasons:
- Last part title: kept the planner's title word for word, as the plan must be held to.
- Terms used inside worked examples before their definitions, more than one worked example in some parts, source-narrating phrases, long asides, hints on the checks, moving the token example before its definition: not reworked in this pass; they remain open for a later edit.
- Quiz overlap with checks: quiz 0002 uses different numbers and cases from every practice check, so I kept it.
