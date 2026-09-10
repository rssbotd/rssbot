# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "33ce47d91d23e2f08ea3c88ba729c8cf",
    "brokers": "7b538e39c4cbf771cfc7aa7af9ee6b0b",
    "clients": "76dbf2500f53dd1f2d0dbc50c9edf35b",
    "command": "ffcc1f6594f913efef6628294b9de515",
    "configs": "a76957a9575874a43e19d348e61ac6f6",
    "defines": "f6da40af2240d015d28ce6224bbbe664",
    "encoder": "92d40ef5ae50cafba6cc88b0e260b012",
    "engines": "6e08062628b324ff8ead4aaacdcadb32",
    "fetcher": "350fdb8ddc37c23fbad9685bc8f5a0fe",
    "loggers": "bff3f83a7436a45814853a34ca069251",
    "looping": "6a8f6f3369dc6b4980d68087941857d2",
    "message": "a4095faea9fabfeb87f9abe05da599f1",
    "objects": "7b4de5cab301c4bb56c153a4854e09a3",
    "package": "8c57813abd9552cf860750dbaab39ad7",
    "parsers": "bbb1a0183c61bd9fea612ec00eedeb33",
    "persist": "dd76d5cc15d3c16372ea34e51fa4a1f7",
    "pooling": "f20a7782598016fc262275511df1d557",
    "repeats": "c103268a6570558d1d53e2d2161d804c",
    "require": "bc38ac96f2f7a6d338df77c860839989",
    "runtime": "873afa8f2caccd62ec29d56cc4d31a39",
    "threads": "bf204b132a637089383f407e58b553db",
    "utility": "7736fb6aa8e951c0630531f1aa2d596c",
    "watcher": "fd271e485857938561742702fcf12356"
}


MODULES = {
    "cfg": "a47404e23ba563ebc0c3ac7a99fb8b77",
    "fnd": "c7816bb51a83be76bcccf5bc514f367b",
    "irc": "d77258369b0c92e8e38980a5c0fb10e7",
    "opm": "e691361b8fda0596cb67cdd9af36c1a8",
    "rss": "457846ad534eff3f38e93249f269cced",
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
