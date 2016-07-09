#!/usr/bin/env python

from subprocess import Popen


def concurrent_curl(data):
    ps = []
    for url, out in data:
        cmd = ['curl', '--silent', url]
        p = Popen(cmd, stdout=open(out, 'w'))
        ps.append(p)

    for p in ps:
        p.wait()
