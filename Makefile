%.py: %.ui
	pyside-uic $< > $@

coolapp.py: gui/mainwindow.py gui/randomdialog.py

run: coolapp.py
	python coolapp.py
