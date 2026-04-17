import urllib.request
import json

def search_loras(query):
    url = f"https://huggingface.co/api/models?search={query}&filter=text-to-image,lora"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"\nSearching for '{query}':")
            for m in data[:3]:
                print(f"- {m['id']}")
    except:
        print(f"Failed to fetch {query}")

search_loras("tarot")
search_loras("vintage")
search_loras("stained glass")
search_loras("pencil art")
search_loras("ink")
search_loras("engraving")
search_loras("illustration")
