# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "4465f93752a9a1e8e31f7c9d8140bebe",
    "brokers": "bf614fd92d3268216c853bbb08a57b03",
    "clients": "b413a171a471d34bf6316745e1706726",
    "command": "f32195caf74094d583d25393c09a8954",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "defines": "e075ed3a2f56a4181d870961c25d8b61",
    "encoder": "7c7f68bbcdc0bd9955c0acf70a9b4d7c",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "loggers": "0c0da171831c7b05d0cf369159a90409",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "428bff45813633055e71003d71ec4053",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "c3b42bbc567da30b4018000951c2cd7b",
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
    "irc": "65221a112c5356a3bf2b8e3bf65c8236",
    "rss": "e73119088cbcfa5453e8fa0c90909345",
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
