from pathlib import Path
cdir = Path('./')
for cf in cdir.glob('*.md'):
    indat = open(cf, 'r').readlines()
    with open(cf,'w') as ofp:
        for line in indat:
            if 'categories' in line:
                line = 'categories: ["halifax-2023"]\n'
            ofp.write(line)