# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "c2fc3cec7dd76782d0df43c31ac937e3",
    "clients": "236d050f9b0bfc739f2b68c934092952",
    "command": "4849f20c1f890fdf0bd45905c24b7b07",
    "configs": "35fd868784ef7d8e33a9452e8660cc9d",
    "defines": "0d452b380709139c628573f0c292fae6",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "fetcher": "91cae8ef0e2a27c588cad6ad14e7174b",
    "looping": "310c6bb6923eb6282143ac3ebf5d659e",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "objects": "c892a3d53b73bbdf2b85c2adf105d6e8",
    "package": "7e9535636da7b77009aa4ac66873e4c7",
    "parsers": "178864f8cde7b2465b490451aa06d9d6",
    "persist": "e696c599efd459cbf6374572592d1807",
    "require": "8468b2c606e90d1f33816f059ddafbdc",
    "runtime": "9a8b3baabc8b9dc2ab0855a9f275bb9b",
    "threads": "ee5f9c1f306c7e3233f3c077d47ec779",
    "utility": "9576ee8a8e47ca90afaa7d6d4db5a381"
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
