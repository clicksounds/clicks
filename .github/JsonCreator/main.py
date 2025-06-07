import os
import traceback
import shutil
import json
import time

jsonshit = {
    "everything": [],
    "meme": [],
    "useful": []
}

with open('all_files.json', 'r') as f:
    filecrap = json.load(f)

def rename_files():
    folder_path = shutil.copytree("Update", "Output")
    shutil.rmtree("Update")
    for root, dirs, files in os.walk(folder_path):
        for i, file in enumerate(files, start=1):
            name = root.split("/")[2]
            memeUseful = root.split("/")[1]
            filename, file_extension = os.path.splitext(file)
            if file == "pack.json":
                pack = {}
                with open(os.path.join(root, "pack.json"), "r") as fileh:
                    lines = fileh.readlines()
                    pack = json.loads('\n'.join(lines))
                pack["click-files"] = filecrap["e"][name]["c"]
                pack["release-files"] = filecrap["e"][name]["r"]
                for thing in pack["authors"]:
                    if "type" not in thing:
                        thing["type"] = "Main"
                with open(os.path.join(root, "pack.json"), "w") as fileh:
                    fileh.write(json.dumps(pack) + '\n')
                with open(os.path.join("../../info", pack["id"] + ".json"), "w") as fileh:
                    fileh.write(json.dumps(pack) + '\n')
                jsonshit["everything"].append(pack)
                if pack["type"] == "Meme":
                    jsonshit["meme"].append(pack)
                elif pack["type"] == "Useful":
                    jsonshit["useful"].append(pack)

if __name__ == "__main__":
    if os.path.exists("Output"):
        shutil.rmtree("Output")
    os.mkdir("Update")
    shutil.copytree("../../Meme", "Update/Meme")
    shutil.copytree("../../Useful", "Update/Useful")

    rename_files()

    jsonshitall = jsonshit["everything"]
    jsonshitall2 = jsonshit["meme"]
    jsonshitall3 = jsonshit["useful"]

    shutil.rmtree("../../Meme")
    shutil.rmtree("../../Useful")
    shutil.copytree("Output/Meme", "../../Meme")
    shutil.copytree("Output/Useful", "../../Useful")

    with open("../../list.json", "w") as file:
        file.write(json.dumps(jsonshitall) + '\n')
    with open("../../meme.json", "w") as file:
        file.write(json.dumps(jsonshitall2) + '\n')
    with open("../../useful.json", "w") as file:
        file.write(json.dumps(jsonshitall3) + '\n')

    shutil.rmtree("Output")
    print("Files renamed, converted, and original files removed successfully!")
