# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "f3c643e9961eeb669ebc66ad6a80788e",
    "brokers": "7578f0f6f1074b91416117aabb9518c6",
    "buffers": "98af2b1a25fa257b140bd72a92f668fc",
    "caching": "1ff3b6f5773a6aa40ad3bfdf7001e38e",
    "clients": "d71f1d82dd9d9338fa7836e1da05fd24",
    "command": "4849f20c1f890fdf0bd45905c24b7b07",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "console": "3d67b69459252297257c6e566545ab53",
    "daemons": "b8d2b2bd4628fbf2912e1730b19b0f21",
    "defines": "a43229eaa77471fbf4d7395b43a17ec6",
    "display": "a8cf92bac0c6a872936461fa0b4e58d2",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "16dbb2e124d80440ff4f10d071e4bc28",
    "fetcher": "8ef9ab283dbbdbdcd0d17c21b784048e",
    "handler": "c5218de9f2a98d783e2f138d55f66f46",
    "kernels": "a3d1c4ddcca62e1daf608d21cd682cca",
    "locater": "fee2c1a80c3aa3cebc1e1454e4c416ff",
    "loggers": "5c1468e57a6c3c940495b8adf3fa71e4",
    "looping": "21c34bf932571c26079c298ce4f8f30a",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "ca481638f42109f208147adcefffa995",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "options": "2ecdd873312adbf52a564c3774a171b8",
    "outputs": "72bcccec2f96a719381082509bacdb1d",
    "package": "aaad3c63e6f3848758a5844c9011d5bf",
    "parsers": "24dfafaa37a9706b4bc7f997a8dfb371",
    "persist": "9b2e2cff7ba31efe444732576bc2857c",
    "pooling": "d1bf5fbaaf6a528259096c5493aba25b",
    "repeats": "b947b7bf88faa29fbbb0a489b9f01f6c",
    "require": "8468b2c606e90d1f33816f059ddafbdc",
    "runners": "dbd7c456d1481cf1f4ed9977d6fbabc2",
    "runtime": "c4c7865fd72d1340992e393c50cf3564",
    "screens": "f1f3111ca89d439e89ba0eae5ba10503",
    "scripts": "2ecdd873312adbf52a564c3774a171b8",
    "service": "2ecdd873312adbf52a564c3774a171b8",
    "sources": "e854b03dcfb33d64773412ae97b178ff",
    "threads": "35e18554a62c22f035453301730b6102",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "db92b8fb4fa5e624e150148efa3ad755",
    "watcher": "caa0450481ffcdb4748fe58ae9447638",
    "workdir": "8ecfa6e7d2274c12b4509197da57c755"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "c7816bb51a83be76bcccf5bc514f367b",
    "irc": "d77258369b0c92e8e38980a5c0fb10e7",
    "opm": "e691361b8fda0596cb67cdd9af36c1a8",
    "rss": "9033cdcfda66892aac1db1cd14e32b76",
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
