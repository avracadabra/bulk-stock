[![Build Status](https://travis-ci.org/avracadabra/bulk-stock.svg?branch=master)](https://travis-ci.org/avracadabra/bulk-stock)
[![Coverage Status](https://coveralls.io/repos/github/avracadabra/bulk-stock/badge.svg?branch=master)](https://coveralls.io/github/avracadabra/bulk-stock?branch=master)

# bulk-stock

An application to manage bulk stock in stores.

This repo will contains Dockerfile to publish images on docker hub. and
integration test to make sure all pieces are working together.

## State

This is very early stage of development repository to test
some technologies and deep into idea around
[avracadabra](https://www.avracadabra.fr/)

## Ideas

I've more than one ideas, in order to keep focus
I'll try to split them in 3 parts:

- **bulk stock management system**
  : This is about managing stock in stores that receive
  customers.

- **provider stock management**
  : This is about provider stock management and how to
  make easy the communication with stores.

- **jar traceability**
  : This is about customer jar traceability.

At the beginning I'll focus on store management. before deep into
expected features lets talk about used technologies.

## Frameworks and source code

Those are very personal choices about what I know and what
I want to deep into so:

- **The Warehouse Management System (WMS) Service** will be done using
  [Anyblok](https://github.com/AnyBlok/AnyBlok) and [AWB: Anyblok Warehouse
  management system Base](https://github.com/AnyBlok/anyblok_wms_base)

  Anyblok is a quite recent framework that I (Pierre Verkest) trust and
  contribute, so I'm not very fair about that choice, but it use a lot of
  famous python library likes SqlAlchemy, pyramid...

- **Proxy Service** this service will serve data to clients through
  GraphQL using [tartiflette.io](https://tartiflette.io/) based on
  [aiohttp](https://aiohttp.readthedocs.io/en/stable/). It will aggregate and
  cache some data from different services (WMS: Warehouse Management System,
  PIM: Product Information Management, ...) before send them to the end user.

- **Frontend** will be develop using [ELM](https://elm-lang.org/) a functional
  language that I've test a little bit and looks like very promising as long
  term maintenance.

# Credits

This [AnyBlok][anyblok] package was created with
[audreyr/cookiecutter][cookiecutter] and the
[AnyBlok/cookiecutter-anyblok-project][cookiecutter-anyblok] project template.

# License

[Mozilla Public License Version 2.0](http://mozilla.org/MPL/2.0/)

# Authors

- Pierre Verkest <pierreverkest84@gmail.com>

[anyblok]: https://github.com/AnyBlok/AnyBlok
[cookiecutter-anyblok]: https://github.com/Anyblok/cookiecutter-anyblok-project
[cookiecutter]: https://github.com/audreyr/cookiecutter
