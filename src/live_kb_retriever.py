import requests
import json
import os

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def fetch_wikipedia_results(query, top_k=5):
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'utf8': '',
        'format': 'json',
        'srlimit': top_k
    }
    response = requests.get(WIKI_API_URL, params=params)
    if response.status_code != 200:
        print(f"Error fetching results for: {query}")
        return []
    data = response.json()
    return [item['title'] for item in data.get('query', {}).get('search', [])]

def get_page_content(title):
    params = {
        'action': 'query',
        'prop': 'extracts',
        'titles': title,
        'format': 'json',
        'exintro': True,
        'explaintext': True,
    }
    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()
    pages = data.get('query', {}).get('pages', {})
    return next(iter(pages.values())).get('extract', '')


def retrieve_and_store(conversations_path, output_dir, top_k=5):
    with open(conversations_path, 'r') as file:
        raw_data = file.read().strip().split("\n")
        conversations = [json.loads(line) for line in raw_data if line.strip()]




    os.makedirs(output_dir, exist_ok=True)

    for i, convo in enumerate(conversations if isinstance(conversations, list) else [conversations]):
        conv_id = f"conv_{i:03}"
        last_utterance = convo['post']['title']

        titles = fetch_wikipedia_results(last_utterance, top_k=top_k)
        docs = [{"title": title, "content": get_page_content(title)} for title in titles]

        output_path = os.path.join(output_dir, f"{conv_id}.json")
        with open(output_path, 'w') as out_file:
            json.dump({"utterance": last_utterance, "retrieved": docs}, out_file, indent=2)
        print(f"✅ Saved retrievals for {conv_id}")

if __name__ == "__main__":
    retrieve_and_store("data/sample_conversations.json", "retrieved_results")
