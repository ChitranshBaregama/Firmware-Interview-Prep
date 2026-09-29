from pathlib import Path
import argparse, shutil

p=argparse.ArgumentParser()
p.add_argument("id")
p.add_argument("slug")
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
dst=root/"questions"/f"{a.id}_{a.slug}"
dst.mkdir(parents=True, exist_ok=False)
for f in (root/"templates").iterdir():
    shutil.copy2(f, dst/f.name)
print(dst)
