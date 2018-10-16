# coding: utf-8

reg_dict = {
'BRST': '_("Брестская область")',
'VTBS': '_("Витебская область")',
'GMLS': '_("Гомельская область")',
'GRDN': '_("Гродненская область")',
'MNSK': '_("Минская область")',
'MGLV': '_("Могилевская область")'
}

with open('/Users/artkra/working/project/pm/static/maps/velcom_new/belarusALLRG.js', 'r') as f:
    with open('/Users/artkra/working/project/pm/static/maps/velcom_new/belarusALLRGtest.js', 'ab') as t:
        buf = f.readline()
        t.write(buf)
        buf = f.readline()
        t.write(buf)
        t.write('')
        while buf:
            if "id" in buf:
                reg = buf.split('"')[3].split('.')[0]
            if '"name"' in buf:
                buf = f.readline()
                t.write('\t\t"region":' + reg_dict[reg] + ',\n')
                t.write(buf)
            else:
                buf = f.readline()
                t.write(buf)