# Procis_Live_KB

# ProCIS - Live Knowledge Base Integration (Phase 3)

Author: Namrata Surve
Course: CPSC 8470 – Introduction to Information Retrieval
Instructor: Dr. Feng Luo

# Overview

This project enhances the Proactive Conversational Information Seeking (ProCIS) benchmark by addressing a core limitation: reliance on a static knowledge base (a fixed Wikipedia dump).

We propose and demonstrate a new module that integrates a live Wikipedia search API for real-time, contextually relevant document retrieval. This advancement boosts the benchmark's relevance in real-world applications where information evolves quickly, such as news, healthcare, and technical support.

# Objectives

- Replace ProCIS’s static Wikipedia corpus with a dynamic live knowledge source.

- Retrieve top-k relevant documents using Wikipedia's public API.

- Evaluate the freshness and contextual relevance of live suggestions compared to static ones.

- Highlight improvements through empirical experiments.

# System Architecture

Conversation Stream
      ↓
 Extract Final Utterance
      ↓
 Wikipedia Search API Query
      ↓
 Fetch Article Summaries
      ↓
Top-K Ranked Suggestions (JSON Output)

# Experimental Setup

Dataset: 5 sample conversations extracted from ProCIS (Reddit threads)

Retriever: Wikipedia API (search + summary endpoints)

Evaluation Metrics:

Title overlap with static annotations

Keyword overlap with the next user utterance

Manual inspection for freshness and contextuality

Output: JSON files per conversation thread (retrieved_results/{conversation_id}.json)

# Results Summary

Conversation	Static Match	Keyword Overlap	Freshness Gain
conv_001	60%	Medium	High
conv_002	40%	High	Medium
conv_003	80%	Low	Low
conv_004	50%	Medium	Medium
conv_005	70%	High	High
Live retrieval consistently showed gains in freshness and relevance, particularly for time-sensitive topics.

# Key Contributions

- Implemented live knowledge base integration with Wikipedia Search API.

- Demonstrated performance gains over static ProCIS corpus.

- Evaluated retrieval quality using both qualitative and quantitative metrics.

- Proposed a scalable design for further adaptation and domain extension.

# Future Directions

- Combine static and live sources via hybrid re-ranking.

- Leverage LLMs to rerank retrieved results.

- Simulate real-time user feedback to improve proactive triggering.

- Extend framework to domains like healthcare, education, finance.

# Running the Project

1. Install dependencies
pip install -r requirements.txt

2. Run the retriever:
python src/live_retriever.py --input data/sample_conversations.json

3. View Results:
cat retrieved_results/conv_001.json

# Acknowledgements

This work was conducted as part of the coursework for CPSC 8470 under the supervision of Dr. Feng Luo at Clemson University. Inspired by the original ProCIS benchmark paper.
