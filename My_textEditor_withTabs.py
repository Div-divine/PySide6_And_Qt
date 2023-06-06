<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>991</width>
    <height>783</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>-10</x>
      <y>0</y>
      <width>991</width>
      <height>721</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="currentIndex">
     <number>1</number>
    </property>
    <property name="tabsClosable">
     <bool>true</bool>
    </property>
    <widget class="QWidget" name="tab1">
     <attribute name="title">
      <string>Tab 1</string>
     </attribute>
     <widget class="QTextEdit" name="textEdit">
      <property name="geometry">
       <rect>
        <x>13</x>
        <y>0</y>
        <width>971</width>
        <height>691</height>
       </rect>
      </property>
     </widget>
    </widget>
    <widget class="QWidget" name="tab2">
     <attribute name="title">
      <string>Tab 2</string>
     </attribute>
     <widget class="QTextEdit" name="textEdit_2">
      <property name="geometry">
       <rect>
        <x>13</x>
        <y>0</y>
        <width>971</width>
        <height>691</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>0</y>
      <width>21</width>
      <height>24</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string>+</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>720</y>
      <width>75</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>CheckBox</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>991</width>
     <height>22</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuFile">
    <property name="title">
     <string>File</string>
    </property>
    <addaction name="actionOpen"/>
    <addaction name="actionSave"/>
    <addaction name="actionSava_As"/>
    <addaction name="actionNew"/>
    <addaction name="actionExit"/>
   </widget>
   <widget class="QMenu" name="menuEdit">
    <property name="title">
     <string>Edit</string>
    </property>
    <addaction name="actionView"/>
   </widget>
   <widget class="QMenu" name="menuView">
    <property name="title">
     <string>View</string>
    </property>
    <addaction name="actionZoom_Out"/>
    <addaction name="actionZoom_In"/>
   </widget>
   <widget class="QMenu" name="menuAdvanced">
    <property name="title">
     <string>Advanced</string>
    </property>
    <addaction name="actionAuto_Save"/>
   </widget>
   <addaction name="menuFile"/>
   <addaction name="menuEdit"/>
   <addaction name="menuView"/>
   <addaction name="menuAdvanced"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionOpen">
   <property name="text">
    <string>Open</string>
   </property>
  </action>
  <action name="actionSave">
   <property name="text">
    <string>Save</string>
   </property>
  </action>
  <action name="actionSava_As">
   <property name="text">
    <string>Sava As</string>
   </property>
  </action>
  <action name="actionNew">
   <property name="text">
    <string>New</string>
   </property>
  </action>
  <action name="actionExit">
   <property name="text">
    <string>Exit</string>
   </property>
  </action>
  <action name="actionView">
   <property name="text">
    <string>Find</string>
   </property>
  </action>
  <action name="actionZoom_Out">
   <property name="text">
    <string>Zoom Out</string>
   </property>
  </action>
  <action name="actionZoom_In">
   <property name="text">
    <string>Zoom In</string>
   </property>
  </action>
  <action name="actionAuto_Save">
   <property name="text">
    <string>Auto Save</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
