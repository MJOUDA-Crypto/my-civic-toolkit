import yaml
import requests

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    print("[*] Loaded config:")
    print(config)

    # Example action: Fetch a website
    if 'test_url' in config:
        try:
            r = requests.get(config['test_url'])
            print(f"[+] Fetched {config['test_url']} - Status: {r.status_code}")
        except Exception as e:
            print(f"[!] Error fetching URL: {e}")

if __name__ == "__main__":
    main()
