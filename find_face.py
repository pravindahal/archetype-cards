import urllib.request
import json
import urllib.parse
def search_loras(query):
    encoded = urllib.parse.quote(query)
    url = f"https://huggingface.co/api/models?search={encoded}&filter=text-to-image,lora"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"\nSearching for '{query}':")
            for m in data[:5]:
                print(f"- {m['id']}")
    except:
        pass
search_loras("detailer")
