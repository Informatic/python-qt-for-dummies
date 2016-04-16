Python & Qt for Dummies™
========================
This is a tiny guide on Qt desktop application development using Python. It
turns out this pair is a great option for quick multiplatform apps.

I've successfuly made application in a Linux environment in a single night
that worked straight away on Windows machines after bundling it with cx_Freeze.
That's quite nice. :^)

PyQt4 vs PySide
---------------
So there are two most popular bindings - PyQt4 and PySide. PyQt is developed by 
[Riverbank Computing](https://www.riverbankcomputing.com/) and licensed under
mixed GPLv3 (for non-commercial use) and Riverbank Commercial License (which
costs 350 GBP for a single developer), while PySide is project by Qt community
licensed under LGPL, thus cheaper and more interesting choice for small-scale
commercial projects. Both APIs are mostly identical with little differences,
for best support when releasing application to be run from sources it's best to
use some wrapper [like QtVariant provided here.](https://askubuntu.com/a/141641)

Building
--------
User interface can be conveniently designed in QtCreator, and then tool like
`pyside-uic` (or `pyuic4 for PyQt4 bindings) can be used to generate plain
python classes from that. These classes can then be extended to contain
additional slots ("event handlers") and all your logic code.

This repository contains GNU Make `Makefile` which can automatically detect
changes in `.ui` files and rebuild python classes when needed. Just use `make
run` to do that and run an application.

Documentation
-------------
PySide (as well as PyQt with slight differences) is direct binding from Qt
libraries thus official Qt documentation applies just fine. (If something is not
in QtGui module, just look for it in QtCore)
More docs can be found here: https://wiki.qt.io/PySideDocumentation

Notes
-----
This guide definitely has to be updated to account for Qt5 some day.
