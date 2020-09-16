# connio

![Pypi version][pypi]

A python concurrency agnostic communication library.

Pass a URL to the single point API function `connio.connection_for_url()`
and it will return a communication object with a common generic API.

Helpful when handling with instrumentation which work over serial line or TCP
(and in future USB) with simple REQ-REP communication protocols (example:
[SCPI](https://en.m.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments)).

The request for a communication object is forwarded to the corresponding
[serialio][serialio] or [sockio][sockio] libraries depending on the
URL you give.

Written in asyncio with support for different concurrency models:

* asyncio
* classic blocking API
* future based API
* python 2 compatible blocking API (for those pour souls stuck with python 2)



## Installation

From within your favorite python environment:

```console
pip install connio
```

## Usage

```python
import asyncio
from connio import connection_for_url

async def main():

    # A local async serial line
    sl = connection_for_url("serial:///dev/ttyS0", parity="E")
    print(await sl.write_readline(b"*IDN?\n"))

    # An async serial line over telnet server
    sl = connection_for_url("rfc2217://moxa.acme.org:7890", parity="E")
    print(await sl.write_readline(b"*IDN?\n"))

    # An async TCP connection
    tcp = connection_for_url("tcp://gepace.acme.org:5025")
    print(await tcp.write_readline(b"*IDN?\n"))

    # An sync TCP connection
    tcp = connection_for_url("tcp://gepace.acme.org:5025", concurrency="sync")
    print(tcp.write_readline(b"*IDN?\n"))

asyncio.run(main())
```

[pypi]: https://img.shields.io/pypi/pyversions/connio.svg
[serialio]: https://github.com/tiagocoutinho/serialio
[sockio]: https://github.com/tiagocoutinho/sockio