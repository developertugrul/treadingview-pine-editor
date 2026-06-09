import os, glob

path = r'C:\Users\tugrul\Desktop\Claude\BORSA\tradingview\v1\**\*.pine'
files = glob.glob(path, recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('shape.star', 'shape.diamond')
    content = content.replace('\n         plot(', '\nplot(')
    content = content.replace('\n                options=[', '\n               options=[')
    content = content.replace('\n                group=grp_panel)', '\n               group=grp_panel)')
    
    content = content.replace('\n                math.abs', '\n               math.abs')
    content = content.replace('\n                genel_asagi  ? "▼ AŞAĞI TREND"  :', '\n               genel_asagi  ? "▼ AŞAĞI TREND"  :')
    content = content.replace('\n                st_yukari    ? "↗ ST Yükseliş"   :', '\n               st_yukari    ? "↗ ST Yükseliş"   :')
    content = content.replace('\n                "~ Kararsız"', '\n               "~ Kararsız"')
    
    content = content.replace('\n                st_yukari    ? "↗ ZAYIF YUKARI"  :', '\n               st_yukari    ? "↗ ZAYIF YUKARI"  :')
    content = content.replace('\n                st_asagi     ? "↘ ZAYIF AŞAĞI"  :', '\n               st_asagi     ? "↘ ZAYIF AŞAĞI"  :')
    content = content.replace('\n                "~ KARARSIZ"', '\n               "~ KARARSIZ"')
    
    content = content.replace('\n                genel_asagi  ? C_BEAR :', '\n               genel_asagi  ? C_BEAR :')
    content = content.replace('\n                C_NEUT', '\n               C_NEUT')
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed', file)
