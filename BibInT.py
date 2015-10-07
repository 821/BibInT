import sys,re,os
from PyQt4.QtGui import *; from PyQt4.QtWebKit import QWebView,QWebPage; from PyQt4.QtCore import *
# user
folder = 'E:/Reference'
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
		self.setGeometry(0, 70, screen.width(), screen.height()-100)
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

# user inputs
global CommandStr, AuthorStr, TitleStr, JournalStr, YearStr, PublisherStr, BooktitleStr, EditorStr, ChapterStr, PagesStr, InstitutionStr, SchoolStr, AddressStr, CrossrefStr, EditionStr, HowpublishedStr, KeywordsStr, MonthStr, NumberStr, OrganizationStr, SeriesStr, TypeStr, VolumeStr, NoteStr, CommandEdit, AuthorEdit, TitleEdit, JournalEdit, YearEdit, PublisherEdit, BooktitleEdit, EditorEdit, ChapterEdit, PagesEdit, InstitutionEdit, SchoolEdit, AddressEdit, CrossrefEdit, EditionEdit, HowpublishedEdit, KeywordsEdit, MonthEdit, NumberEdit, OrganizationEdit, SeriesEdit, TypeEdit, VolumeEdit, NoteEdit
def inputs(field):
	exec(field + "Edit = QLineEdit()", globals())
	exec(field + "Edit.setPalette(pal)", globals())
	exec(field + "Edit.setFont(font)", globals())
	def paste():
		exec(field + "Edit.paste()", globals())
		exec(field + "Str = " + field + "Edit.text()", globals())
	entButton = QPushButton(field)
	entButton.setFixedWidth(200)
	entButton.setFont(font)
	entButton.clicked.connect(paste)
	Layout = QHBoxLayout()
	exec("Layout.addWidget(" + field + "Edit)")
	Layout.addWidget(entButton)
	rLayout.addLayout(Layout)

# type
def types(rtype):
	exec("typeBox.addItem('" + rtype + "')")

# function buttons
def funcButt(var):
	button = QPushButton(var[0])
	button.clicked.connect(var[1])
	button.setFont(font)
	var[2].addWidget(button)
def Add():
	pass
def Edit():
	pass
def Clear():
	pass
def Add2():
	pass
def Edit2():
	pass
def Clear2():
	pass
def init():
	pass

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
listWidget.setFixedWidth(150)
listWidget.setPalette(pal)
init()

textEdit = QTextEdit()
textEdit.setPalette(pal)
textEdit.setFont(font)
textEdit.setFixedWidth(screen.width() / 4)
midLayout.addWidget(textEdit)
alldo(funcButt, [('Add', Add2, midLayout), ('Edit', Edit2, midLayout), ('Clear', Clear2, midLayout)])

typeBox = QComboBox()
typeBox.setFont(font)
alldo(types, ['Book', 'Article', 'Booklet', 'Conference', 'Inbook', 'Incollection', 'Inproceedings', 'Manual', 'Mastersthesis', 'Misc', 'Phdthesis', 'Proceedings', 'Techreport', 'Unpublished'])
rLayout.addWidget(typeBox)
alldo(inputs, ['Command', 'Author', 'Title', 'Journal', 'Year', 'Publisher', 'Booktitle', 'Editor', 'Chapter', 'Pages', 'Institution', 'School', 'Address', 'Crossref', 'Edition', 'Howpublished', 'Keywords', 'Month', 'Number', 'Organization', 'Series', 'Type', 'Volume', 'Note'])
alldo(funcButt, [('Add', Add, buttonLayout), ('Edit', Edit, buttonLayout), ('Clear', Clear, buttonLayout)])
rLayout.addLayout(buttonLayout)

fullLayout.addWidget(listWidget)
fullLayout.addLayout(midLayout)
fullLayout.addLayout(rLayout)
widget.setLayout(fullLayout)

widget.show()
app.exec_()