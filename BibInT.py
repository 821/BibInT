import sys,re,os,bibtexparser
from pybtex.database.input.bibtex import Parser; from pybtex.database.output.bibtex import Writer
from PyQt4.QtGui import *; from PyQt4.QtCore import *
# user
folder = 'E:\\Reference\\'
defalt = 'defalt' # new bibtex entries will be stored here
# bibtex format
reftypes = ['book', 'article', 'booklet', 'conference', 'inbook', 'incollection', 'inproceedings', 'manual', 'mastersthesis', 'misc', 'phdthesis', 'proceedings', 'techreport', 'unpublished']
fields = ['ID', 'author', 'title', 'journal', 'year', 'publisher', 'booktitle', 'editor', 'chapter', 'pages', 'institution', 'school', 'address', 'crossref', 'edition', 'howpublished', 'keywords', 'month', 'number', 'organization', 'series', 'type', 'volume', 'note', 'file']
global IDEdit, authoredit, titleedit, journaledit, yearedit, publisheredit, booktitleedit, editoredit, chapteredit, pagesedit, institutionedit, schooledit, addressedit, crossrefedit, editionedit, howpublishededit, keywordsedit, monthedit, numberedit, organizationedit, seriesedit, typeedit, volumeedit, noteedit, fileEdit

# open bibtex files and load to list
def init():
	listWidget.clear()
	alldo(add2List, allref)
def readbib(content, bibfilename): # read bibtex content and save into allref
	bibdata = bibtexparser.loads(content).entries
	for entry in bibdata:
		entry['file'] = bibfilename
		allref.append(entry)
def add2List(entry):
	lItem = QListWidgetItem(entry['ID'] + '`' + entry['file'])
	lItem.setFont(QFont('serif', 16))
	listWidget.addItem(lItem)
# list to ref
def tobib(entryinlist):
	db = bibtexparser.bibdatabase.BibDatabase()
	db.entries = []
	db.entries.append(entryinlist)
	writer = bibtexparser.bwriter.BibTexWriter()
	return writer.write(db)
def clearfields():
	for field in fields:
		exec(field + "Edit.clear()", globals())
def View():
	crRef = listWidget.currentItem().text()
	for ref in allref:
		refSplit = crRef.split('`')
		if refSplit[0] == ref['ID'] and refSplit[1] == ref['file'] :
			clearfields()
			for key in ref.keys():
				if key == 'ENTRYTYPE':
					typeBox.setCurrentIndex(reftypes.index(ref['ENTRYTYPE']))
				else:
					exec(key + "Edit.setText('" + ref[key] + "')")
			textEdit.setText(tobib(ref)) # view in textedit
# list and entries to files
def writetofiles():
	init()
	for bac in os.listdir(folder):
		if os.path.splitext(bac)[-1][1:] == 'bac':
			os.remove(folder + bac)
	for ref in allref:
		if os.path.exists(folder + ref['file'] + '.bib'):
			os.rename(folder + ref['file'] + '.bib', folder + ref['file'] + '.bac')
	for ref in allref:
		with open(folder + ref['file'] + '.bib', 'a', encoding = 'utf-8') as reffile:
			reffile.write(tobib(ref))
def edits2dict():
	got = {}
	got['ENTRYTYPE'] = typeBox.currentText()
	for field in fields:
		exec("text = " + field + "Edit.text()", globals())
		if text:
			exec("got['" + field + "'] = text")
		elif field == 'file':
			got['file'] = defalt
	return got
def Add():
	allref.append(edits2dict())
	writetofiles()
def Add2():
	bibdata = bibtexparser.loads(textEdit.document().toPlainText()).entries
	for entry in bibdata:
		allref.append(entry)
	writetofiles()

# from Note-
def alldo(func, list):
	for v in list:
		func(v)
class Widget(QWidget):
	def __init__(self, parent=None):
		super (Widget, self).__init__(parent)
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor.fromRgb(0, 30, 60))
		self.setPalette(p)
		self.setGeometry(1, 60, screen.width(), screen.height()-85)
		self.setWindowTitle('Note-')
		self.setWindowIcon(QIcon('BibTeX.png'))
		self.sysTrayIcon = QSystemTrayIcon(self)
		self.sysTrayIcon.setIcon(QIcon('BibTeX.png'))
		self.connect(self.sysTrayIcon, SIGNAL('activated(QSystemTrayIcon::ActivationReason)'), self.activate)
		self.sysTrayIcon.setVisible(True)
	def changeEvent(self, event):
		if self.isMinimized():
			self.hide()
	def activate(self, reason):
		if reason == 1 or reason == 2:
			self.show(); self.setWindowState(Qt.WindowActive)
# function buttons
def funcButt(var):
	button = QPushButton(var[0])
	button.clicked.connect(var[1])
	button.setFont(font)
	var[2].addWidget(button)

# type
def types(rtype):
	exec("typeBox.addItem('" + rtype + "')")
# user inputs
def inputs(field):
	exec(field + "Edit = QLineEdit()", globals())
	exec(field + "Edit.setPalette(pal)", globals())
	exec(field + "Edit.setFont(font)", globals())
	def paste():
		exec(field + "Edit.clear()", globals())
		exec(field + "Edit.paste()", globals()) # function: paste from clipboard
	entButton = QPushButton(field)
	entButton.setFixedWidth(200)
	entButton.setFont(font)
	entButton.clicked.connect(paste)
	Layout = QHBoxLayout()
	exec("Layout.addWidget(" + field + "Edit)")
	Layout.addWidget(entButton)
	rLayout.addLayout(Layout)

def Edit():
	pass
def Edit2():
	pass

allref = []
for bibfile in os.listdir(folder):
	if os.path.splitext(bibfile)[-1][1:] == 'bib':
		with open(folder + bibfile, 'r', encoding='utf-8') as bibopen:
			readbib(bibopen.read(), os.path.splitext(bibfile)[0])
app = QApplication(sys.argv)
screen = QDesktopWidget().screenGeometry()
pal = QPalette()
bgc = QColor(0, 0, 0)
pal.setColor(QPalette.Base, bgc)
textc = QColor(255, 255, 255)
pal.setColor(QPalette.Text, textc)
font = QFont()
font.setPointSize(screen.height() // 62)

widget = Widget()
fullLayout, midLayout, rLayout, buttonLayout = QHBoxLayout(), QVBoxLayout(), QVBoxLayout(), QHBoxLayout()

listWidget = QListWidget()
listWidget.setFixedWidth(200)
listWidget.setPalette(pal)
alldo(add2List, allref)
widget.connect(listWidget, SIGNAL('itemClicked(QListWidgetItem *)'), View)

textEdit = QTextEdit()
textEdit.setPalette(pal)
textEdit.setFont(font)
textEdit.setFixedWidth(screen.width() / 4)
midLayout.addWidget(textEdit)
alldo(funcButt, [('Add', Add2, midLayout), ('Edit', Edit2, midLayout), ('Clear', lambda: textEdit.setText(''), midLayout)])

typeBox = QComboBox()
typeBox.setFont(font)
alldo(types, reftypes)
rLayout.addWidget(typeBox)
alldo(inputs, fields)
alldo(funcButt, [('Add', Add, buttonLayout), ('Edit', Edit, buttonLayout), ('Clear', clearfields, buttonLayout)])
rLayout.addLayout(buttonLayout)

fullLayout.addWidget(listWidget)
fullLayout.addLayout(midLayout)
fullLayout.addLayout(rLayout)
widget.setLayout(fullLayout)
widget.show()
app.exec_()