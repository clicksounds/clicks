import os
import json

def collect_files(base_dir):
    result = {}
    for pack_type in ['Meme', 'Useful']:
        type_dir = os.path.join(base_dir, '..', '..', pack_type)
        if not os.path.isdir(type_dir):
            continue
        for pack in os.listdir(type_dir):
            pack_dir = os.path.join(type_dir, pack)
            if not os.path.isdir(pack_dir):
                continue
            clicks_dir = os.path.join(pack_dir, 'Clicks')
            releases_dir = os.path.join(pack_dir, 'Releases')
            clicks = sorted(os.listdir(clicks_dir)) if os.path.isdir(clicks_dir) else []
            releases = sorted(os.listdir(releases_dir)) if os.path.isdir(releases_dir) else []
            result[pack] = {"c": clicks, "r": releases}
    return result

if __name__ == "__main__":
    base = os.path.dirname(__file__)
    obj = {"e": collect_files(base)}
    with open(os.path.join(base, "all_files.json"), "w") as f:
        json.dump(obj, f, indent=2)