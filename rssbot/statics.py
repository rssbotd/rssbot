# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "2f5776e0bd8b986bb70fcff0a5698e8b",
    "brokers": "0174b643bbb4da359340e371bececf64",
    "clients": "c32842e0c6de42b360942024989361e0",
    "command": "c427c52ef8e362605c816f7d06853d96",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "b2dafb00013406f520cd73a25beb22c2",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "fetcher": "4f8c4966d9322b7cc90f37173a174a68",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1b1d7d46d5f1253d905f6a13de075ce9",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "5908114744b95d3cfda9b61722b1e8ec",
    "package": "1317c1bad74b244a6b82d562dc4a1eb9",
    "parsers": "de88da518e5ca1b61346cb327eb538e2",
    "persist": "f590b6a6f033103040fcabded23e0dae",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "5dcb987227c5bb45faab57563967ebd1",
    "runtime": "8146da7afa08cc6376f8c98203ce83f9",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "utility": "7bfc5e8741007048fac03878ee0b2181",
    "watcher": "20f9fe59f70b4c5774e55bc6919feafb"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "4db4f174d6e358349eaf72aa4e62eb88",
    "opm": "315fc36048012dfa55980735c5e6eeca",
    "rss": "42f9e0ab9b2a0a14a3f996b6399b66a2",
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
