import os
import json
import csv

def estimate_overlap_and_freshness(summary, query):
    # Simple keyword overlap estimate
    query_keywords = set(query.lower().split())
    summary_keywords = set(summary.lower().split())
    overlap = len(query_keywords & summary_keywords)

    # Heuristic-based interpretation
    keyword_overlap = "High" if overlap > 5 else "Medium" if overlap > 2 else "Low"
    freshness_gain = "High" if "202" in summary else "Medium" if any(x in summary for x in ["recent", "latest", "new"]) else "Low"
    return keyword_overlap, freshness_gain

def generate_metrics(results_dir, output_csv):
    rows = []
    for filename in sorted(os.listdir(results_dir)):
        if not filename.endswith(".json"):
            continue
        path = os.path.join(results_dir, filename)
        with open(path, 'r') as f:
            data = json.load(f)
            query = data.get("utterance", "")
            retrieved_docs = data.get("retrieved", [])
            summaries = " ".join([doc["content"] for doc in retrieved_docs if "content" in doc])
            keyword_overlap, freshness = estimate_overlap_and_freshness(summaries, query)
            conv_id = filename.replace(".json", "")
            rows.append([conv_id, "N/A", keyword_overlap, freshness, "Auto-generated estimates"])

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["conversation_id", "static_match_percent", "keyword_overlap", "freshness_gain", "notes"])
        writer.writerows(rows)

    print(f"✅ Metrics saved to {output_csv}")

if __name__ == "__main__":
    generate_metrics("retrieved_results", "results/comparison_metrics.csv")
