# bulk-stock

An application to manage bulk stock in stores


## State

This is very early stage of development repository to test
some technologies and deep into idea arround
[avracadabra](https://www.avracadabra.fr/)

## Ideas

I've more tha one ideas, in order to keep focus
I'll try to split them in 3 parts:

* **bulk stock management system**
  : This is about managing stock in stores that receive
  customers.

* **provider stock management**
  : This is about provider stock managment and how to
  make easy the communication with stores.

* **jar traceability**
  : This is about customer jar traceability.

At the begining I'll focus on store managment. before deep into
expected features lets talk about used technologies.

## Frameworks and source code

Those are very personnal choices about what I know and what
I want to know a bit more so:

* **The backend** will be done using [Anyblok](https://github.com/AnyBlok/AnyBlok)
and [AWB: Anyblok Warehouse management system Base](https://github.com/AnyBlok/anyblok_wms_base)

Anyblok is a quite recent framework that I (Pierre Verkest) trust and contribute, so I'm not
very fair about that choice, but it use a lot of prooved famous python librairy likes
SqlAlchemy, pyramid...

* **Frontend** will be develop using [ELM](https://elm-lang.org/) a functionnal language
that I've test a little bit and looks like very promising as long term maintenance.


# Credits

This [AnyBlok][anyblok] package was created with
[audreyr/cookiecutter][cookiecutter] and the
[AnyBlok/cookiecutter-anyblok-project][cookiecutter-anyblok] project template.


# License

[Mozilla Public License Version 2.0](http://mozilla.org/MPL/2.0/)


# Authors

* Pierre Verkest <pierreverkest84@gmail.com>


[anyblok]: https://github.com/AnyBlok/AnyBlok

[cookiecutter-anyblok]: https://github.com/Anyblok/cookiecutter-anyblok-project
[cookiecutter]: https://github.com/audreyr/cookiecutter
