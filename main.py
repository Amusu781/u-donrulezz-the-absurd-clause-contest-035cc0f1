import os
import shutil

ENTRY = "By using the Service, the user grants the Company a perpetual, royalty-free licence to their dreams, including recurring ones, which may be sublicensed to the moon, its successors and assigns."

OUT = os.environ.get("MAKEFUN_OUT", "/output")
os.makedirs(OUT, exist_ok=True)
for name in os.listdir(OUT):
    path = os.path.join(OUT, name)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip()
