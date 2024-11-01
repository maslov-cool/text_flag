import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>750</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>750</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>750</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>821</width>
      <height>231</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout_2">
     <item row="0" column="0">
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>Цвет № 1</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_1">
         <property name="text">
          <string>Синий</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_1</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_2">
         <property name="text">
          <string>Красный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_1</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_3">
         <property name="text">
          <string>Зелёный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_1</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
     <item row="0" column="1">
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>Цвет № 2</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_4">
         <property name="text">
          <string>Синий</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_2</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_5">
         <property name="text">
          <string>Красный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_2</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_6">
         <property name="text">
          <string>Зелёный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_2</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
     <item row="0" column="2">
      <layout class="QVBoxLayout" name="verticalLayout_3">
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>Цвет № 3</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_7">
         <property name="text">
          <string>Синий</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_3</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_8">
         <property name="text">
          <string>Красный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_3</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="radioButton_9">
         <property name="text">
          <string>Зелёный</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">color_group_3</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>250</y>
      <width>141</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>221</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>750</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="color_group_1"/>
  <buttongroup name="color_group_2"/>
  <buttongroup name="color_group_3"/>
 </buttongroups>
</ui>
'''


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.setWindowTitle('Текстовый флаг')

        self.make_flag.clicked.connect(self.action)

    def action(self):
        self.result.setText('Цвета: ' + self.color_group_1.checkedButton().text() + ', ' +
                            self.color_group_2.checkedButton().text() + ' и ' +
                            self.color_group_3.checkedButton().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
