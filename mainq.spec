# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mainq.py'],
             pathex=['D:\\M1\\CVision\\shop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mainq',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mainq')






























































        ################   APPEL A LA FONCTION ####################

        self.ajouter.clicked.connect(self.open_img)
        self.rotateAll.clicked.connect(self.rotation)
        self.contour.clicked.connect(self.contourIm)
        self.trait2.mousePressEvent = self.niveauxGris
        self.trait3.mousePressEvent = self.binarisation
        self.trait4.mousePressEvent = self.binarisation_invesrion
        self.rotateLeft.clicked.connect(self.egalisationHist)
        self.pushButton.clicked.connect(self.flou)
        self.zoom_moins.clicked.connect(self.zoom_min)
        self.zoom_plus.clicked.connect(self.zoom_max)

        #BOOLEAN SHOW ET HIDE FILTRAGE CONTENU
        self.label_5.setHidden(True)
        self.median_filter.setHidden(True)
        self.filtrage_bilateral.setHidden(True)
        self.filtrage_gauss.setHidden(True)

        self.label_6.setHidden(True)
        self.fd1.setHidden(True)
        self.fd2.setHidden(True)
        self.fd3.setHidden(True)

        ###########################################

        self.filtrer.clicked.connect(self.filtrages)
        
        self.fd1.clicked.connect(self.filtrage_dir1)
        self.fd2.clicked.connect(self.filtrage_dir2)
        self.fd3.clicked.connect(self.filtrage_dir2)

        self.pushButton.clicked.connect(self.filtre_flou)

        self.median_filter.clicked.connect(self.flou_median)
        self.filtrage_bilateral.clicked.connect(self.flou_bilaterals)
        self.filtrage_gauss.clicked.connect(self.flou_gausss)


        self.Red.valueChanged.connect(self.opacitey)
        self.Green.valueChanged.connect(self.gauss_slide)
        self.Bleu.valueChanged.connect(self.echelle)
        self.erosion.valueChanged.connect(self.eroder)
        

        self.pushButton_2.clicked.connect(self.showSliderCanny)
        self.horizontalSlider.valueChanged.connect(self.Canny)
        self.max.valueChanged.connect(self.Canny)

        self.filename = None
        self.tmp = None
        self.opacite = 0
        self.flou = 0

   ###################################################################################################################################################
   ###################################################################################################################################################
   ###################################################################################################################################################
   ###################################################################################################################################################
    
    #Début ouverture image
    def open_img(self):
        fname, filter = QFileDialog.getOpenFileName()
        if fname:
            self.loadImage(fname)
        else:
            print("Invalid Image")

    def loadImage(self, fname):
        self.image = cv2.imread(fname)
        self.tmp = self.image
        self.displayImage()

    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8

        if len(self.image.shape) == 3:
            if(self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        
        thresh = 144
        max_val = 255
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)

        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img2 = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_Indexed8)
        
        
        ret, binaire_inversion = cv2.threshold(frame, thresh, max_val, cv2.THRESH_BINARY_INV) 
        img3 = QImage(binaire_inversion, binaire_inversion.shape[1], binaire_inversion.shape[0], binaire_inversion.strides[0], QImage.Format_Indexed8)

        ret, binaire = cv2.threshold(frame, thresh, max_val, cv2.THRESH_BINARY)
        img4 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        
        img = img.rgbSwapped()  
        img2 = img2.rgbSwapped() 
        img4 = img4.rgbSwapped()     
        if window == 1:  
            #image à l'origine    
            self.trait1.setScaledContents(True)
            self.trait1.setPixmap(QPixmap.fromImage(img))
            self.trait1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            
            #image traité en gris 
            self.trait2.setScaledContents(True)
            self.trait2.setPixmap(QPixmap.fromImage(img2))
            self.trait2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            #Binarisation Inversion
            self.trait3.setScaledContents(True)
            self.trait3.setPixmap(QPixmap.fromImage(img3))
            self.trait3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            #image traité Binarisation
            self.trait4.setScaledContents(True)
            self.trait4.setPixmap(QPixmap.fromImage(img4))
            self.trait4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            
            #image image traité
            self.import_image.setPixmap(QPixmap.fromImage(img))
            self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        if window == 2:
            
            self.import_image.setPixmap(QPixmap.fromImage(img))
            self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Rouge.setText("OPACI")
        self.label_2.setText("GAUSS")
        self.label_3.setText("ECHEL")
        self.erosion_2.setText("DE")
        self.min.setHidden(True)
        self.max.setHidden(True)
        self.horizontalSlider.setHidden(True)
        self.label_10.setHidden(True)
      
   
   ###################################################################################################################################################


    #Début rotation image 
    def rotation(self):
        rows, cols, steps = self.image.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1) 
        self.image = cv2.warpAffine(self.image, M, (cols, rows))
        self.displayImage(2)

   ####################################################################################################################################################
    
    #NIVEAUX DE GRIS ON CLICK LABEL TRAIT1
    def niveauxGris(self,image):
        self.image = self.tmp
        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img2 = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_Indexed8)
        #self.import_image.setScaledContents(True)
        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

   #################################################################################################################################################### 


    #BINARISATION
    def binarisation(self,image):
        self.image = self.tmp
        sary=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        #thresh à expliqué
        thresh = 145
        max_val = 255
        ret, binaire = cv2.threshold(sary, thresh, max_val, cv2.THRESH_BINARY_INV)
        img2 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        #self.import_image.setScaledContents(True)
        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


  #################################################################################################################################################### 

      #INVESRSION DE BINARISATION
    def binarisation_invesrion(self,image):
        self.image = self.tmp
        sary=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        #thresh à expliqué
        thresh = 145
        max_val = 255
        ret, binaire = cv2.threshold(sary, thresh, max_val, cv2.THRESH_BINARY)
        img2 = QImage(binaire, binaire.shape[1], binaire.shape[0], binaire.strides[0], QImage.Format_Indexed8)
        #self.import_image.setScaledContents(True)
        self.import_image.setPixmap(QPixmap.fromImage(img2))
        self.import_image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

  #################################################################################################################################################### 

    #egalisation d'histograme
    def egalisationHist(self):
        self.image = self.tmp
        sary_traite = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        R, G, B = cv2.split(sary_traite)
        sortie_1_R = cv2.equalizeHist(R)
        sortie_1_G = cv2.equalizeHist(G)
        sortie_1_B = cv2.equalizeHist(B)

        
        self.image = cv2.merge((sortie_1_B,sortie_1_G, sortie_1_R))
        
        
        plt.hist(sortie_1_R.ravel(),1000,[0,390])
        plt.hist(sortie_1_G.ravel(),1000,[0,390])
        plt.hist(sortie_1_B.ravel(),1000,[0,390])
        plt.show()
        self.displayImage(2)

  #################################################################################################################################################### 

    #CONTOURS D'IMAGES
    def contourIm(self):
            self.image = self.tmp

            

            thresh = 140
            max_val = 255
            lower = np.array([60,60,60])
            higher = np.array([250,250,250])
            image_traitement = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            ret, mask =  cv2.threshold(image_traitement, thresh, max_val, cv2.THRESH_BINARY_INV)
            cont, contour = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            self.image = cv2.drawContours(self.image,cont,-1,(0,0,255),2)
            self.displayImage(2)
            
 #################################################################################################################################################### 
    
    #FLOU D'IMAGES    
    def flou(self):
        self.image = self.tmp
        self.image = cv2.blur(self.image, (5, 5))
        self.displayImage(2)

#################################################################################################################################################### 

    #Zoom moins 
    def zoom_min(self):
        self.image = cv2.resize(self.image, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)                          

####################################################################################################################################################               

    #Zoom plus 
    def zoom_max(self):
        self.image = cv2.resize(self.image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)             

####################################################################################################################################################               

     #Appel à tous les fonctions de filtrages
    def filtrages(self):
        self.label_6.setHidden(False)    
        self.fd1.setHidden(False)
        self.fd2.setHidden(False)
        self.fd3.setHidden(False)

####################################################################################################################################################

####################################################################################################################################################

    #Filtrage directionnel X1 
    def filtrage_dir1(self):
        self.image = self.tmp
        kernel = np.ones((3, 3), np.float32) / 9
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Filtrage directionnel X2
    def filtrage_dir2(self):
        self.image = self.tmp
        kernel = np.ones((4, 4), np.float32) / 9
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Filtrage directionnel X3
    def filtrage_dir3(self):
        self.image = self.tmp
        kernel = np.ones((5, 5), np.float32) / 9
        self.image = cv2.filter2D(self.image, -1, kernel)
        self.displayImage(2)

####################################################################################################################################################

    #Appel fonction de filtrage flou
    def filtre_flou(self):
        self.label_5.setHidden(False)    
        self.median_filter.setHidden(False)
        self.filtrage_bilateral.setHidden(False)
        self.filtrage_gauss.setHidden(False)

####################################################################################################################################################        

    #FLou median
    def flou_median(self):
        self.image = self.tmp
        self.image = cv2.medianBlur(self.image,5)
        self.displayImage(2)

####################################################################################################################################################

    # filtrage Flou bilateral 
    def flou_bilaterals(self):
        self.image = self.tmp
        self.image = cv2.bilateralFilter(self.image,9,75,75)
        self.displayImage(2)

####################################################################################################################################################

    # Filtrage FLou de gauss
    def flou_gausss(self):
        self.image = self.tmp
        self.image = cv2.GaussianBlur(self.image,(5,5),0)
        self.displayImage(2)

####################################################################################################################################################

    #REGLAGE D'OPACITE SLIDER
    def opacitey(self, gamma):
        self.image = self.tmp
        gamma = gamma*0.1
        invGamma = 1.0 /gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

        self.image = cv2.LUT(self.image, table)
        self.displayImage(2)


####################################################################################################################################################

    #REGLE SLIDER GAUSS    
    def gauss_slide(self, g):
        self.image = self.tmp
        self.image = cv2.GaussianBlur(self.image, (5, 5), g)
        self.displayImage(2)


####################################################################################################################################################

    #REGLAGE ECHELLE
    def echelle(self , c):
        self.image = self.tmp
        self.image = cv2.resize(self.image, None, fx=c, fy=c, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)

####################################################################################################################################################

    #DE (Dilatation erision)
    def eroder(self , iter):
        self.image = self.tmp
        if iter > 0 :
            kernel = np.ones((4, 7), np.uint8)
            self.image = cv2.erode(self.tmp, kernel, iterations=iter)
        else :
            kernel = np.ones((2, 6), np.uint8)
            self.image = cv2.dilate(self.image, kernel, iterations=iter*-1)
        self.displayImage(2)


####################################################################################################################################################



    def showSliderCanny(self):
        self.min.setHidden(False)
        self.max.setHidden(False)
        self.horizontalSlider.setHidden(False)            
        self.max.setHidden(False)
        self.label_10.setHidden(False)
        self.horizontalSlider.setHidden(False)



    def Canny(self):
        self.image = self.tmp
        can = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.Canny(can, self.horizontalSlider.value(), self.max.value())
        self.displayImage(2)      

    
  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())