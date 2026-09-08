# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "d2b9b0d1ff094bd5f39b3504364051bb",
    "brokers": "7578f0f6f1074b91416117aabb9518c6",
    "buffers": "98af2b1a25fa257b140bd72a92f668fc",
    "caching": "1ff3b6f5773a6aa40ad3bfdf7001e38e",
    "clients": "d71f1d82dd9d9338fa7836e1da05fd24",
    "command": "a691dab9de089c76580cd52b5ed8b30d",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "a43229eaa77471fbf4d7395b43a17ec6",
    "display": "a8cf92bac0c6a872936461fa0b4e58d2",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "01450a9aa3d2272a59652955aae52748",
    "fetcher": "8ef9ab283dbbdbdcd0d17c21b784048e",
    "handler": "60836f12d1198a32e62af32287fcd24d",
    "locater": "fee2c1a80c3aa3cebc1e1454e4c416ff",
    "loggers": "5c1468e57a6c3c940495b8adf3fa71e4",
    "looping": "21c34bf932571c26079c298ce4f8f30a",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "ca481638f42109f208147adcefffa995",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "72bcccec2f96a719381082509bacdb1d",
    "package": "aaad3c63e6f3848758a5844c9011d5bf",
    "parsers": "24dfafaa37a9706b4bc7f997a8dfb371",
    "persist": "9b2e2cff7ba31efe444732576bc2857c",
    "pooling": "d1bf5fbaaf6a528259096c5493aba25b",
    "repeats": "8cfa3e199dc33f97878b28ffa0c01c40",
    "require": "8468b2c606e90d1f33816f059ddafbdc",
    "runners": "dbd7c456d1481cf1f4ed9977d6fbabc2",
    "runtime": "2ecdd873312adbf52a564c3774a171b8",
    "screens": "12ca2d20f80e5f6d2f1c9c443c3ccf8f",
    "sources": "e854b03dcfb33d64773412ae97b178ff",
    "threads": "35e18554a62c22f035453301730b6102",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "86761f40babb844e750a51326402efc5",
    "watcher": "caa0450481ffcdb4748fe58ae9447638",
    "workdir": "8ecfa6e7d2274c12b4509197da57c755"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "c7816bb51a83be76bcccf5bc514f367b",
    "irc": "d77258369b0c92e8e38980a5c0fb10e7",
    "opm": "ad51933f934d29118e1e14ccf8e349ab",
    "rss": "cf3a9f9952a26058bfd523f370b59fbf",
    "srv": "79208bdb18f9e4429ac35d8721fd0822",
    "thr": "aa9d092137049239127bbf5b85599018",
    "upt": "4e8110d1b93254cd6555a619b2b78ccc"
}


NAMES = {
    "atr": "rss",
    "cfg": "cfg",
    "dpl": "rss",
    "exp": "opm",
    "fnd": "fnd",
    "imp": "opm",
    "nme": "rss",
    "pwd": "irc",
    "rem": "rss",
    "res": "rss",
    "rss": "rss",
    "srv": "srv",
    "syn": "rss",
    "thr": "thr",
    "upt": "upt"
}


def __dir__():
    return (
        'CORE',
        'MODULES',
        'NAMES'
    )
