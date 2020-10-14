# PCL-Button-Feedback


## OBS + Virtual-Camera-Plugin Tutorial
In diesem Abschnitt soll das Setup für eine virtuelle Kamera beschrieben werden.

1. Zunächst muss folgendes installiert werden:
    * **OBS**: https://obsproject.com/de
    * **OBS virtual-camera-plugin**: https://obsproject.com/forum/resources/obs-virtualcam.949/
        * ___Hinweis___: Bei der Installation des Plugins kann die Anzahl der virtuellen Kameras bei 1 gelassen werden.
        
            ![](readme%20images/install.PNG)
    
2. Python-Skript ([detector.py](https://github.com/felixortmann/PCL-Button-Feedback/blob/master/detector.py)) starten. 
Es muss eventuell der VideoCapture-Parameter angepasst werden, damit die
korrekte Kamera ausgewählt wird. Es sollte sich ein Fenster öffnen mit dem augmentierten Webcamstream.
3. OBS starten. Neue Quelle hinzufügen (__Quelle (rechtsklick) → Hinzufügen → Fensteraufnahme__).
Name für das Fenster auswählen oder direkt bestätigen.

    ![quelle](readme%20images/quelle.PNG)

4. Im neuen Fenster das OpenCV Fenster des Python-Skripts auswählen (Hier: __[python.exe] frame__). Bestätigen.

    ![window](readme%20images/window.PNG)

5. Obere Taskleiste: __Werkzeuge → VirtualCam__. Target Camera auf ***OBS-Camera2*** setzen. Klick auf **Start**.

    ![](readme%20images/obscam2.PNG)
    
6. Rechtsklick auf die in Schritt 3 neue Quelle/Fensteraufnahme, dann auf **Filter**.

    ![](readme%20images/filter.PNG)
    
7. Im neuen Fenster rechtsklick auf den **Effektfilter → Hinzufügen → VirtualCam**. Hier unter **Target Camera: OBS-Camera**
auswählen und starten. Das wird der Name für die Videokonferenzen sein.

    ![](readme%20images/obscam1.PNG)
    
8. Beliebiges Videokonferenzsoftware öffnen und als Webcam OBS-Camera auswählen, z.B. BBB.

    ![](readme%20images/bbb.PNG)