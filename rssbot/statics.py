# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "2edf1cefde5ab25d23687d22459016cd",
    "brokers": "bf614fd92d3268216c853bbb08a57b03",
    "clients": "9bd824df44ceeeaf73134e38f8177669",
    "command": "f32195caf74094d583d25393c09a8954",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "daemons": "0242599fa838682206c2d07878854a18",
    "defines": "01e3c2c92e91f3c02428ef5a03d87fcd",
    "encoder": "7c7f68bbcdc0bd9955c0acf70a9b4d7c",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "dc4c2e41f7a6cf82584e8119ee6725fa",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "b7edddf1249f1be8b9e568379479948f",
    "package": "c1fa926069d773af8863d6d29401fa6f",
    "parsers": "cc9923d5e2e0aab885247a530ac0970c",
    "persist": "49e11f383821f99816f40c5bf2e304d6",
    "repeats": "eaec4feccb68aea97288b5729d710454",
    "require": "258d6a2a356c4c23cb5ce6faa40efa86",
    "runtime": "48efb67456d45822a47be31cfd8963f0",
    "threads": "2fcb5ceb0fa336dd7208297fc23e17b0",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "370494b1ecafd52182d8ad2a1192f866"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "d63c3713611b0d9995f536471089695b",
    "irc": "3b7482f4a34c2ebb3b4179f7c8971977",
    "rss": "cc9415a8b0ecc3a53824ae8dfdca5616",
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
