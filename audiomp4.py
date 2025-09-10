import os
import json

folders = {
    "Saison1": "music/Saison 1",
    "Saison2": "music/Saison 2"
}

extensions = [".mp3", ".flac"]

tracks = {}

for saison, folder in folders.items():
    if os.path.exists(folder):
        saison_tracks = {}
        for file in os.listdir(folder):
            name, ext = os.path.splitext(file)
            if ext.lower() in extensions:
                if name not in saison_tracks:
                    saison_tracks[name] = {"title": name, "files": []}
                saison_tracks[name]["files"].append(os.path.join(folder, file).replace("\\", "/"))
        tracks[saison] = list(saison_tracks.values())
    else:
        print(f"Dossier introuvable : {folder}")

with open("tracks.json", "w", encoding="utf-8") as f:
    json.dump(tracks, f, indent=4, ensure_ascii=False)

print("✅ tracks.json généré")
