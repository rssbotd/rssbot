# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "ecf492148f16c199a1529e31b7ae05c3",
    "clients": "00bdef52e0c1fe4a021a3da410dde98c",
    "command": "4849f20c1f890fdf0bd45905c24b7b07",
    "configs": "35fd868784ef7d8e33a9452e8660cc9d",
    "defines": "590087c271ee1f2885f778873eee5f7e",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "fetcher": "91cae8ef0e2a27c588cad6ad14e7174b",
    "loggers": "f6682f08b96a3e92b4aea34b2d80bcf0",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "objects": "c892a3d53b73bbdf2b85c2adf105d6e8",
    "package": "7e9535636da7b77009aa4ac66873e4c7",
    "parsers": "178864f8cde7b2465b490451aa06d9d6",
    "persist": "6e20851959d851c200142a41bf30353b",
    "require": "8468b2c606e90d1f33816f059ddafbdc",
    "runtime": "dd793ef4f39ca1709b93da142bd94d94",
    "threads": "857daae5bab1bca7e29b7de2fc6d9f83",
    "utility": "81b74a3365bdf92fca7c72f11baa8d1b"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "c7816bb51a83be76bcccf5bc514f367b",
    "irc": "d77258369b0c92e8e38980a5c0fb10e7",
    "opm": "e691361b8fda0596cb67cdd9af36c1a8",
    "rss": "5d3fa3491f76c09da7bace106d9e2e41",
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
