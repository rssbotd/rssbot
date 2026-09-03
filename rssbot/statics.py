# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "3c57d8c0f74e3e0e8d8ab341c634e24c",
    "brokers": "4d751219f294ccc6cbe7644f4cc202d0",
    "clients": "70bf3b44b10aadf53f7321584081867f",
    "command": "a17fc464c120fb316616730e4b9715e3",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "a547587db7f3da2ab165471f7af559e4",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "fetcher": "28ddbe8c25382246008d4823f008a804",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1b1d7d46d5f1253d905f6a13de075ce9",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "af547abcc9342045ee16836549906098",
    "package": "1317c1bad74b244a6b82d562dc4a1eb9",
    "parsers": "de88da518e5ca1b61346cb327eb538e2",
    "persist": "364fe8518cc88367cffa81b654beb141",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "5dcb987227c5bb45faab57563967ebd1",
    "runtime": "8146da7afa08cc6376f8c98203ce83f9",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "utility": "7bfc5e8741007048fac03878ee0b2181",
    "watcher": "bc1f50786775de68bc07d2fedcd96908"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "21afb18b8db1dcf325bfbf95fd8989eb",
    "opm": "315fc36048012dfa55980735c5e6eeca",
    "rss": "ab0f7005f2e4b550b8d641800b417b1d",
    "srv": "928c1092265eb21e38d985ad06625ece",
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
