# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_thesaurus_ui.ui'
#
# Created: Mon Feb 17 11:37:43 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import resources_rc


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogThesaurus(object):
    def setupUi(self, DialogThesaurus):
        DialogThesaurus.setObjectName(_fromUtf8("DialogThesaurus"))
        DialogThesaurus.resize(540, 468)
        DialogThesaurus.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconSite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogThesaurus.setWindowIcon(icon)
        self.gridLayout_6 = QtGui.QGridLayout(DialogThesaurus)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_29 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_first_rec = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 5, 1, 1)
        self.pushButton_next_rec = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon2)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 7, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon3)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 8, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon4)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 9, 1, 1)
        self.pushButton_save = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon5)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 0, 10, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon6)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 7, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon7)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 8, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon8)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout.addWidget(self.pushButton_sort, 1, 9, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon9)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 10, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_delete.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon10)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout.addWidget(self.pushButton_delete, 1, 2, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(DialogThesaurus)
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon11)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(DialogThesaurus)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_42 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_43 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(DialogThesaurus)
        self.label_status.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText(_fromUtf8(""))
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName(_fromUtf8("label_sort"))
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_27 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName(_fromUtf8("label_rec_corrente"))
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName(_fromUtf8("label_rec_tot"))
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.line_8 = QtGui.QFrame(DialogThesaurus)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_6.addWidget(self.line_8, 1, 0, 1, 2)
        self.comboBox_sigla = QtGui.QComboBox(DialogThesaurus)
        self.comboBox_sigla.setEnabled(False)
        self.comboBox_sigla.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sigla.setFont(font)
        self.comboBox_sigla.setMouseTracking(True)
        self.comboBox_sigla.setEditable(True)
        self.comboBox_sigla.setMaxVisibleItems(99999)
        self.comboBox_sigla.setMaxCount(2147483647)
        self.comboBox_sigla.setObjectName(_fromUtf8("comboBox_sigla"))
        self.comboBox_sigla.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_sigla, 2, 0, 2, 1)
        self.comboBox_sigla_estesa = QtGui.QComboBox(DialogThesaurus)
        self.comboBox_sigla_estesa.setEnabled(False)
        self.comboBox_sigla_estesa.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sigla_estesa.setFont(font)
        self.comboBox_sigla_estesa.setMouseTracking(True)
        self.comboBox_sigla_estesa.setEditable(True)
        self.comboBox_sigla_estesa.setMaxVisibleItems(99999)
        self.comboBox_sigla_estesa.setMaxCount(2147483647)
        self.comboBox_sigla_estesa.setObjectName(_fromUtf8("comboBox_sigla_estesa"))
        self.comboBox_sigla_estesa.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_sigla_estesa, 3, 1, 1, 1)
        self.label = QtGui.QLabel(DialogThesaurus)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(DialogThesaurus)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 4, 1, 1, 1)
        self.comboBox_tipologia_sigla = QtGui.QComboBox(DialogThesaurus)
        self.comboBox_tipologia_sigla.setEnabled(False)
        self.comboBox_tipologia_sigla.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_tipologia_sigla.setFont(font)
        self.comboBox_tipologia_sigla.setMouseTracking(True)
        self.comboBox_tipologia_sigla.setEditable(True)
        self.comboBox_tipologia_sigla.setMaxVisibleItems(99999)
        self.comboBox_tipologia_sigla.setMaxCount(2147483647)
        self.comboBox_tipologia_sigla.setObjectName(_fromUtf8("comboBox_tipologia_sigla"))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.comboBox_tipologia_sigla.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_tipologia_sigla, 5, 0, 1, 1)
        self.comboBox_nome_tabella = QtGui.QComboBox(DialogThesaurus)
        self.comboBox_nome_tabella.setEnabled(False)
        self.comboBox_nome_tabella.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_nome_tabella.setFont(font)
        self.comboBox_nome_tabella.setMouseTracking(True)
        self.comboBox_nome_tabella.setEditable(True)
        self.comboBox_nome_tabella.setMaxVisibleItems(99999)
        self.comboBox_nome_tabella.setMaxCount(2147483647)
        self.comboBox_nome_tabella.setObjectName(_fromUtf8("comboBox_nome_tabella"))
        self.comboBox_nome_tabella.addItem(_fromUtf8(""))
        self.comboBox_nome_tabella.addItem(_fromUtf8(""))
        self.comboBox_nome_tabella.addItem(_fromUtf8(""))
        self.comboBox_nome_tabella.addItem(_fromUtf8(""))
        self.comboBox_nome_tabella.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_nome_tabella, 5, 1, 1, 1)
        self.label_11 = QtGui.QLabel(DialogThesaurus)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_10 = QtGui.QLabel(DialogThesaurus)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_6.addWidget(self.label_10, 6, 1, 2, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_13 = QtGui.QLabel(DialogThesaurus)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.textEdit_descrizione_sigla = QtGui.QTextEdit(DialogThesaurus)
        self.textEdit_descrizione_sigla.setMinimumSize(QtCore.QSize(0, 20))
        self.textEdit_descrizione_sigla.setMaximumSize(QtCore.QSize(16777215, 16000000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_descrizione_sigla.setFont(font)
        self.textEdit_descrizione_sigla.setObjectName(_fromUtf8("textEdit_descrizione_sigla"))
        self.verticalLayout_3.addWidget(self.textEdit_descrizione_sigla)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 8, 0, 1, 2)

        self.retranslateUi(DialogThesaurus)
        QtCore.QMetaObject.connectSlotsByName(DialogThesaurus)

    def retranslateUi(self, DialogThesaurus):
        DialogThesaurus.setWindowTitle(QtGui.QApplication.translate("DialogThesaurus", "pyArchInit Gestione Beni culturali - Thesaurus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DialogThesaurus", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("DialogThesaurus", "Connection test", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("DialogThesaurus", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("DialogThesaurus", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("DialogThesaurus", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("DialogThesaurus", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("DialogThesaurus", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(QtGui.QApplication.translate("DialogThesaurus", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("DialogThesaurus", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(QtGui.QApplication.translate("DialogThesaurus", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sigla.setItemText(0, QtGui.QApplication.translate("DialogThesaurus", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sigla_estesa.setItemText(0, QtGui.QApplication.translate("DialogThesaurus", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogThesaurus", "Sigla", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogThesaurus", "Sigla estesa", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(0, QtGui.QApplication.translate("DialogThesaurus", "Tipologia di struttura", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(1, QtGui.QApplication.translate("DialogThesaurus", "definizione sito", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(2, QtGui.QApplication.translate("DialogThesaurus", "definizione stratigrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(3, QtGui.QApplication.translate("DialogThesaurus", "tipo di caratterizzazione", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(4, QtGui.QApplication.translate("DialogThesaurus", "tipo di us", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipologia_sigla.setItemText(5, QtGui.QApplication.translate("DialogThesaurus", "tipo reperto", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_nome_tabella.setItemText(0, QtGui.QApplication.translate("DialogThesaurus", "us_table", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_nome_tabella.setItemText(1, QtGui.QApplication.translate("DialogThesaurus", "site_table", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_nome_tabella.setItemText(2, QtGui.QApplication.translate("DialogThesaurus", "struttura_table", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_nome_tabella.setItemText(3, QtGui.QApplication.translate("DialogThesaurus", "pyunitastratigrafiche", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_nome_tabella.setItemText(4, QtGui.QApplication.translate("DialogThesaurus", "inventario_materiali_table", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DialogThesaurus", "Tipologia sigla", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DialogThesaurus", "Nome tabella", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DialogThesaurus", "Dati descrittivi", None, QtGui.QApplication.UnicodeUTF8))

