# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "5b5863528613b640aa6058f13033b192",
    "brokers": "91bfac1f11cab7c6ddaf348e7689799a",
    "clients": "e9a7f01148ea04f9b95c25962ac95fec",
    "command": "a17fc464c120fb316616730e4b9715e3",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "f7f0efdc031c2ea8ede39d61d30f05f0",
    "encoder": "749faec2870ee53b1bbe11a340a3f947",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "locater": "31182ab15204be63245f8912d316cdf0",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "1b1d7d46d5f1253d905f6a13de075ce9",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "8c22ec85f2b9b76362b1ccca62f640e9",
    "package": "1317c1bad74b244a6b82d562dc4a1eb9",
    "parsers": "583be581d4c62b2d17191220b31849e7",
    "persist": "fbd1e186f85a6119c6e1b8921e01e152",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "5dcb987227c5bb45faab57563967ebd1",
    "runners": "a780799c6655373a79d6409049af3d16",
    "runtime": "8146da7afa08cc6376f8c98203ce83f9",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "utility": "7bfc5e8741007048fac03878ee0b2181",
    "watcher": "e2139a354aaa17545d7d80e24dfd07d7"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "4db4f174d6e358349eaf72aa4e62eb88",
    "rss": "435891821e19982dbfc95204b204caf9",
    "srv": "928c1092265eb21e38d985ad06625ece",
    "thr": "aa9d092137049239127bbf5b85599018",
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
