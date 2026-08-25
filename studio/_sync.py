#!/usr/bin/env python3
"""Re-embed _template.html into the generator page (studio/index.html).

The generator has no server behind it and must also work when opened from
file://, so it can't fetch the template at runtime; it carries a copy inside a
<script type="text/plain"> block instead. Run this after editing _template.html so the two stay in sync:

    python3 studio/_sync.py
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
tpl = io.open(os.path.join(HERE, '_template.html'), encoding='utf-8').read()
gen_path = os.path.join(HERE, 'index.html')
gen = io.open(gen_path, encoding='utf-8').read()

pattern = re.compile(
    r'(<script type="text/plain" id="templateSource">\n)(.*?)(\n</script>)',
    re.DOTALL)
if not pattern.search(gen):
    sys.exit('marker block not found in studio/index.html')

new = pattern.sub(lambda m: m.group(1) + tpl.rstrip('\n') + m.group(3), gen)
io.open(gen_path, 'w', encoding='utf-8').write(new)
print('embedded %d chars of _template.html into studio/index.html' % len(tpl))
