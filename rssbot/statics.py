# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "356bcfca9f6e3aacdd4343e995c5a5ee",
    "brokers": "411602e99c15c7c26d56879651c8e284",
    "buffers": "afc9e5fbbe9ba9dd08e952347aba8b46",
    "clients": "a1223377e8b7eb76a0916dbddc12fd84",
    "command": "8252c22e22d446e0fcec5cb3325161dd",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "4a9e85332d0152dae276744663c86f9c",
    "display": "cbf591509cfdde428059c93738203942",
    "encoder": "7c7f68bbcdc0bd9955c0acf70a9b4d7c",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "loggers": "575e865d11c848de2a53c185a3fb0afc",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1607117dee79ef31d01e1561b6ade069",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "cf9917590377ac8e2cf792eeab0d3d95",
    "package": "1317c1bad74b244a6b82d562dc4a1eb9",
    "parsers": "cc9923d5e2e0aab885247a530ac0970c",
    "persist": "49e11f383821f99816f40c5bf2e304d6",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "258d6a2a356c4c23cb5ce6faa40efa86",
    "runtime": "480cd39a86a5edd94214fbf9a0ac5251",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "973787cf63dccce61d10b16722c08355"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "1a3a2176350a03d2ede9564b8b9ee13f",
    "rss": "6563d2f2f6be561bf96a820ebf3eb82e",
    "tbl": "fea88e7cacbd51ab6977bd4936ff1ee1",
    "thr": "70f24fd3b5aebbed3685a6a4aeeba0d1",
    "upt": "4e8110d1b93254cd6555a619b2b78ccc"
}


NAMES = {
    "atr": "rss",
    "cfg": "cfg",
    "dpl": "rss",
    "exp": "rss",
    "fnd": "fnd",
    "imp": "rss",
    "nme": "rss",
    "pwd": "irc",
    "rem": "rss",
    "res": "rss",
    "rss": "rss",
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
