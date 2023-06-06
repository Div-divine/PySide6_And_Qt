from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QComboBox, QMessageBox, QVBoxLayout
from PySide6.QtUiTools import loadUiType
from PySide6.QtGui import Qt
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl
import googletrans
import textblob
import pyttsx3
import gtts

Ui_MainWindow , QMainWindow = loadUiType("translation_App.ui")

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")
        self.TranslateButton = self.findChild(QPushButton, "pushButton")
        self.ClearButton = self.findChild(QPushButton, "pushButton_2")
        self.TextToSpeechButton = self.findChild(QPushButton, "pushButton_3")
        self.FemaleVoiceButton = self.findChild(QPushButton, "pushButton_4")
        self.COmboBox1 = self.findChild(QComboBox, "comboBox")
        self.COmboBox2 = self.findChild(QComboBox, "comboBox_2")

        
        self.TextToSpeechButton.clicked.connect(self.speak)
        self.TextToSpeechButton.clicked.connect(self.female)

        self.TranslateButton.clicked.connect(self.Translate)
        self.ClearButton.clicked.connect(self.Clear)

        self.lineEdit.setAlignment(Qt.Alignment(Qt.AlignTop | Qt.AlignLeft))
        self.lineEdit2.setAlignment(Qt.Alignment(Qt.AlignTop | Qt.AlignLeft))

        self.languages = googletrans.LANGUAGES
        #print(self.languages)  
        self.language_list = list(self.languages.values())  
        #print(self.language_list)   

        self.COmboBox1.addItems(self.language_list)

        self.COmboBox2.addItems(self.language_list)

        self.COmboBox1.setCurrentText("english")
        self.COmboBox2.setCurrentText("igbo")



        # layout = QVBoxLayout(self)
        # self.video_widget = QVideoWidget()
        # layout.addWidget(self.video_widget)

        # self.media_player = QMediaPlayer()
        # self.media_player.setVideoOutput(self.video_widget)


        # video_url = QUrl.fromLocalFile(r"C:\Users\divin\Downloads\Test.mp4")
        

        # # Start playing the video
        # self.media_player.play()

    
    def Clear(self):
        self.lineEdit.setText("")
        self.lineEdit2.setText("")
        self.COmboBox1.setCurrentText("english")
        self.COmboBox2.setCurrentText("igbo")


    def Translate(self):
        try:
            # Get Original language Key
            for key, value in self.languages.items():
                if value == self.COmboBox1.currentText() :
                    from_language = key

            # Get tranlated language key

            for key, value in self.languages.items():
                if value == self.COmboBox2.currentText() :
                    to_language = key


            #self.lineEdit.setText(from_language)
            #self.lineEdit2.setText(to_language)        
        

            # Let's turn the original text into a textblob, this enables us to translate our text
            words = textblob.TextBlob(self.lineEdit.text())

            # Translate words

            words = words.translate(from_lang= from_language, to=to_language )

            # Output to second textEdit

            self.lineEdit2.setText(str(words))

             # Initialize the speech engine
            # engine = pyttsx3.init()

            # # Pass words into the engine to speak 

            # engine.say(words)

            # # Run the engine
            # engine.runAndWait()

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))

    def speak(self): 

        try:
            # Get Original language Key
            for key, value in self.languages.items():
                if value == self.COmboBox1.currentText() :
                    from_language = key

            # Get tranlated language key

            for key, value in self.languages.items():
                if value == self.COmboBox2.currentText() :
                    to_language = key


            #self.lineEdit.setText(from_language)
            #self.lineEdit2.setText(to_language)        
        

            # Let's turn the original text into a textblob, this enables us to translate our text
            words = textblob.TextBlob(self.lineEdit.text())

            # Translate words

            words = words.translate(from_lang= from_language, to=to_language )

            # Output to second textEdit

            #self.lineEdit2.setText(str(words))

             # Initialize the speech engine
            engine = pyttsx3.init()
            # Adjust  the speech rate
            engine.setProperty('rate', 150) 

            # Pass words into the engine to speak 

            engine.say(words)

            # Run the engine
            engine.runAndWait()

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))     

    def female(self): 

        try:
            # Get Original language Key
            for key, value in self.languages.items():
                if value == self.COmboBox1.currentText() :
                    from_language = key

            # Get tranlated language key

            for key, value in self.languages.items():
                if value == self.COmboBox2.currentText() :
                    to_language = key


            #self.lineEdit.setText(from_language)
            #self.lineEdit2.setText(to_language)        
        

            # Let's turn the original text into a textblob, this enables us to translate our text
            words = textblob.TextBlob(self.lineEdit.text())

            # Translate words

            words = words.translate(from_lang= from_language, to=to_language )

            # Output to second textEdit

            #self.lineEdit2.setText(str(words))

             # Initialize the speech engine
            engine = pyttsx3.init()


            # Get the available voices
            voices = engine.getProperty('voices')

            # Loop through the voices to find a female voice
            female_voice = None

            for voice in voices:
                if 'female' in voice.name.lower():
                    female_voice = voice
                    break

            # Set the voice to the found female voice
            if female_voice:
                engine.setProperty('voice', female_voice.id)
            else:
                print("Female voice not found. Using default voice.")
            # Adjust  the speech rate

            engine.setProperty('rate', 150) 

            # Pass words into the engine to speak 

            engine.say(words)

            # Run the engine
            engine.runAndWait()

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))                

                   

           
        


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = App()

    window.show()
    app.exec()        