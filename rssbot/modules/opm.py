# This file is placed in the Public Domain.
# pylint: disable=C,W0105


"OPML"


import _thread


from ..object  import Object


"defines"


importlock = _thread.allocate_lock()
skipped    = []


TEMPLATE = """<opml version="1.0">
    <head>
        <title>OPML</title>
    </head>
    <body>
        <outline title="opml" text="rss feeds">"""


"parser"


class OPMLParser:

    @staticmethod
    def getnames(line):
        return [x.split('="')[0]  for x in line.split()]

    @staticmethod
    def getvalue(line, attr):
        lne = ''
        index1 = line.find(f'{attr}="')
        if index1 == -1:
            return lne
        index1 += len(attr) + 2
        index2 = line.find('"', index1)
        if index2 == -1:
            index2 = line.find('/>', index1)
        if index2 == -1:
            return lne
        lne = line[index1:index2]
        if 'CDATA' in lne:
            lne = lne.replace('![CDATA[', '')
            lne = lne.replace(']]', '')
            #lne = lne[1:-1]
        return lne

    @staticmethod
    def getattrs(line, token):
        index = 0
        result = []
        stop = False
        while not stop:
            index1 = line.find(f'<{token} ', index)
            if index1 == -1:
                return result
            index1 += len(token) + 2
            index2 = line.find('/>', index1)
            if index2 == -1:
                return result
            result.append(line[index1:index2])
            index = index2
        return result

    @staticmethod
    def parse(txt, toke="outline", itemz=None):
        if itemz is None:
            itemz = ",".join(OPMLParser.getnames(txt))
        result = []
        for attrz in OPMLParser.getattrs(txt, toke):
            if not attrz:
                continue
            obj = Object()
            for itm in spl(itemz):
                if itm == "link":
                    itm = "href"
                val = OPMLParser.getvalue(attrz, itm)
                if not val:
                    continue
                if itm == "href":
                    itm = "link"
                setattr(obj, itm, val.strip())
            result.append(obj)
        return result


def spl(txt):
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]
