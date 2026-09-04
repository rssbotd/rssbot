# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "3c57d8c0f74e3e0e8d8ab341c634e24c",
    "brokers": "91bfac1f11cab7c6ddaf348e7689799a",
    "clients": "70bf3b44b10aadf53f7321584081867f",
    "command": "a17fc464c120fb316616730e4b9715e3",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "971eb8aec3c713f5b4615fdd26210293",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "fetcher": "253e40532e58696a518eacdad7765ca6",
    "hashing": "949c285088499ba4c715835c98e1c6ee",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1b1d7d46d5f1253d905f6a13de075ce9",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "d5f2fe82a55ff7f59ff3f844aba9c8e2",
    "package": "79fd8aea7d70b050baadf470eb9e72e7",
    "parsers": "de88da518e5ca1b61346cb327eb538e2",
    "persist": "364fe8518cc88367cffa81b654beb141",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "1fc8ec4be675b93c9da78a1379b81551",
    "runtime": "392efb2258ce991b733b7ca67e4bbb3a",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "utility": "7bfc5e8741007048fac03878ee0b2181",
    "watcher": "2522617f0b55035e5c84ff1f116a730b"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "fbe18cb6b71d98e458eb8a5aed30b2c3",
    "opm": "315fc36048012dfa55980735c5e6eeca",
    "rss": "cf9dfdc6b481319b7fac8e8671d037a2",
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
