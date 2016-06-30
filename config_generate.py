#!/usr/bin/env python
# -*- coding: utf8 -*-

from jinja2 import Template


template = Template('''{
    "prefix": "s{{ no }}_",
    "taskdb": "mongodb+taskdb://localhost/pyspider_taskdb",
    "projectdb": "mongodb+projectdb://localhost/pyspider_projectdb",
    "resultdb": "mongodb+resultdb://localhost/pyspider_resultdb",
    "amqp_url": "amqp://guest:guest@localhost/pyspider_host",
    "webui": {
        "port": {{ 6000 + no }}
    },
    "phantomjs": {
        "port": {{ 7000 + no }}
    },
    "scheduler": {
        "xmlrpc_port": {{ 8000 + no }}
    }
}''')

no = int(raw_input('Pls input number of pyspider: '))
config = template.render(no=no)

fn = 'config_%s.json' % no
with open(fn, 'w') as fh:
    fh.write(config)

print config
print '==='
print 'config already saved to %s, use ./run.py -c %s to start.' % (fn, fn)
