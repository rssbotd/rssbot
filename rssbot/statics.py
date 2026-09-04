# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "87bd5f5e18c870e841cc716c47164171",
    "brokers": "12fa66535cefa5cbe072200cf590f362",
    "clients": "1fccf3868288dec52fae3cce4b1f565e",
    "command": "c427c52ef8e362605c816f7d06853d96",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "9b3aebaa1644eaa3fdf4bece1c6ec1c5",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "fetcher": "253e40532e58696a518eacdad7765ca6",
    "hashing": "5527c4a5383b44ece726613fc4905327",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1b1d7d46d5f1253d905f6a13de075ce9",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "d5f2fe82a55ff7f59ff3f844aba9c8e2",
    "package": "9dc3ff1e7f113122285f3f2ca58a1cf5",
    "parsers": "de88da518e5ca1b61346cb327eb538e2",
    "persist": "482dbf4f9313f2675e5aa2011a0c6fde",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "1fc8ec4be675b93c9da78a1379b81551",
    "runtime": "8f3b863a467700b2afce27485fbb5b1b",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "utility": "7bfc5e8741007048fac03878ee0b2181",
    "watcher": "c908c65db61edae0b49de52d0dfc619c"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "eml": "85f8b5204ac494656d43e1264eb339fa",
    "fie": "319404702aed6718b4f3684f540e352d",
    "flt": "ed9508361af22b8bb53048963c845331",
    "fnd": "c7816bb51a83be76bcccf5bc514f367b",
    "hlp": "72d51848600d7bad7a99874c461a7d44",
    "irc": "fbe18cb6b71d98e458eb8a5aed30b2c3",
    "log": "9b6cfa6442ad173f4bc174517f9ff349",
    "man": "920599410f7739c9503e0eea9e4e5885",
    "mdl": "c0e0e5376167f973b16f5c8572c2f046",
    "opm": "ad51933f934d29118e1e14ccf8e349ab",
    "pth": "96738e80ef191355b25843c5a369a0e6",
    "req": "bc1984d2e9de0310dc1b468f25c7ab8c",
    "rss": "916c5ad4e942510dbbdad61259e4dcbb",
    "sil": "2bc3b0ab5ff2fbc059005189d8bb4ae1",
    "slg": "e68f11973ddc2e3edeb0de0e16e9fe7a",
    "srv": "928c1092265eb21e38d985ad06625ece",
    "tdo": "2fe9711bc3a47efdf7d8f04cb7444275",
    "thr": "aa9d092137049239127bbf5b85599018",
    "tmr": "e87b0f0a9ced5066fe729fa7eba42263",
    "upt": "4e8110d1b93254cd6555a619b2b78ccc",
    "ver": "b52bce62de72c66593379d77e6a050f8",
    "wsd": "d69089e9164aa0f854a53410e9632625"
}


NAMES = {
    "atr": "rss",
    "cfg": "cfg",
    "dis": "mdl",
    "dne": "tdo",
    "dpl": "rss",
    "eml": "eml",
    "exp": "opm",
    "fie": "fie",
    "flt": "flt",
    "fnd": "fnd",
    "hlp": "hlp",
    "imp": "opm",
    "log": "log",
    "lou": "sil",
    "man": "man",
    "mbx": "eml",
    "nme": "rss",
    "now": "mdl",
    "pth": "pth",
    "pwd": "irc",
    "rem": "rss",
    "req": "req",
    "res": "rss",
    "rss": "rss",
    "sil": "sil",
    "slg": "slg",
    "srv": "srv",
    "syn": "rss",
    "tdo": "tdo",
    "thr": "thr",
    "tmr": "tmr",
    "upt": "upt",
    "ver": "ver",
    "wsd": "wsd"
}


def __dir__():
    return (
        'CORE',
        'MODULES',
        'NAMES'
    )
