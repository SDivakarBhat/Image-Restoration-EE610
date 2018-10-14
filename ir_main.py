# ---------------------------------------------------------------#
# __name__ = "Image_Restoration_EE610_Assignment_2"
# __author__ = "S Divakar Bhat"
# __version__ = "1.0"
# __email__ = "sdivakarbhat@iitb.ac.in"
# __status__ = "Development"
# ---------------------------------------------------------------#

# main.py contains the code for initializing and running the code for GUI
import sys
# PyQt4 libraries are used for GUI
from PyQt4.QtGui import *
from PyQt4.QtCore import *
# OpenCV2 library is used for reading/ writing of images and color space
# conversion only
import cv2
# All array operations are performed using numpy library
import numpy as np
# Matplotlib library is used for histogram plots
import  matplotlib.pyplot as plt

# The GUI structure definition is provided in ImageRestoration.py
from ImageRestoration import *
# Image Restoration logic is defined in Restoration_funcs.py
import Restoration_funcs as Rf

# class ImageEditorClass implements the GUI main window class
class ImageRestorationClass(QMainWindow):

    # stores a copy of original image for use in Undo All functionality
	originalImage = [0]
    # stores the current image being displayed/ processed
	currentImage = [0]
    # stores the previous image for use in Undo operation
	previousImage = [0]

	kernel = [0]
	imageBlur = [0]
    # stores a copy of image being blurred
#    imageBlur = [0]
    # stores a copy of image being sharpened
 #   imageSharpen = [0]

    # stores current image height and width
	imageWidth = 0
	imageHeight = 0
	PSNR = 0
	SSIM = 0
	PSNR1 = 0
	SSIM1 = 0
    # initializes an object of ImageRestorationClass from Restoration_funcs.py
	imageLib = Rf.ImageRestorationClass()

    # stores code of current operation
	currentOperationCode = -1

    # ------------------------------#
    # Blur => 0   #
    # Full Inverse => 1             #
    # Truncated Inverse => 2        #
    # Wiener => 3                   #
    # Constrained Least Square => 4 #
  
    # ------------------------------#

    # GUI initialization
	def __init__(self, parent=None):
		super(ImageRestorationClass, self).__init__()
		QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

        # Assigning functions to be called on all button clicked events 

	
		self.ui.pushButton.clicked.connect(lambda: self.open_image())
		self.ui.pushButton_3.clicked.connect(lambda: self.save_image())
		self.ui.pushButton_2.clicked.connect(lambda: self.Blur())
		self.ui.pushButton_4.clicked.connect(lambda: self.full_inv())
		self.ui.pushButton_5.clicked.connect(lambda: self.truncated_inv())
		self.ui.pushButton_6.clicked.connect(lambda: self.wiener())
		self.ui.pushButton_7.clicked.connect(lambda: self.cls())
		self.ui.pushButton_8.clicked.connect(lambda: self.open_kernel())
		self.ui.pushButton_9.clicked.connect(lambda: self.undo())
		self.ui.pushButton_10.clicked.connect(lambda: self.undoAll())
		self.ui.pushButton_12.clicked.connect(lambda: self.view_kernel())

       
        # initiaize and input dialog box gui for input of gamma value
		self.newDialog = InputDialogGuiClass(self)

    # called when Open button is clicked
	def open_image(self):
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        #self.set_default_slider()

        # open a new Open Image dialog box and capture path of file selected
		open_image_window = QFileDialog()
		image_path = QFileDialog.getOpenFileName\
		(open_image_window, 'Open Image', '/')

        # check if image path is not null or empty
		if image_path:
            # initialize class variables
			self.currentImage = [0]
			self.currentOperationCode = -1

            # read image at selected path to a numpy ndarray object as color image
			self.currentImage = cv2.imread(image_path, 1)
            # convert the image read to HSV format from default BGR format
			#self.currentImage = cv2.cvtColor(self.currentImage, cv2.COLOR_BGR2RGB)

            # set image specific class variables based on current image
			self.imageWidth = self.currentImage.shape[1]
			self.imageHeight = self.currentImage.shape[0]

			self.originalImage = self.currentImage.copy()
			self.previousImage = self.currentImage.copy()

            # displayImage converts current image from ndarry format to
            # pixmap and assigns it to image display label
			self.displayImage()
            # enable_options enable all buttons and sliders in the window.
            # Only Open button is enabled on start
			self.enable_options()

    # called when Open button is clicked
	def open_kernel(self):
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        #self.set_default_slider()

        # open a new Open Image dialog box and capture path of file selected
		open_image_window = QFileDialog()
		image_path = QFileDialog.getOpenFileName(open_image_window, 'Open Image', '/')

        # check if image path is not null or empty
		if image_path:
            # initialize class variables
			self.kernel = [0]
			self.currentOperationCode = -1

            # read image at selected path to a numpy ndarray object as color image
			self.kernel = cv2.imread(image_path, 0)
            # convert the image read to HSV format from default BGR format
            #self.kernel = cv2.cvtColor(self.currentImage, )

            # set image specific class variables based on current image
			self.imageWidth = self.currentImage.shape[1]
			self.imageHeight = self.currentImage.shape[0]

            #self.kernel = self.currentImage.copy()
            #self.previousImage = self.currentImage.copy()

            # displayImage converts current image from ndarry format to
            # pixmap and assigns it to image display label
            #self.displayImage()
            # enable_options enable all buttons and sliders in the window.
            # Only Open button is enabled on start
		self.enable_options()

    # called when Save button is clicked
	def save_image(self):
        # configure the save image dialog box to use .jpg extension for image if
        # not provided in file name
		dialog = QFileDialog()
		dialog.setDefaultSuffix('jpg')
		dialog.setAcceptMode(QFileDialog.AcceptSave)

        # open the save dialog box and wait until user clicks 'Save'
        # button in the dialog box
		if dialog.exec_() == QDialog.Accepted:
            # select the first path in the selected files list as image save
            # location
			save_image_filename = dialog.selectedFiles()[0]
            # write current image to the file path selected by user
			cv2.imwrite(save_image_filename,self.currentImage)
    # called when Histogram Equalization button is clicked
	def Blur(self):
        # updatePreviousImage function updates the previous image class variable
        #  with current image
		self.updatePreviousImage()
        # update current operation code class variable
		self.currentOperationCode = 0
        # set_default_slider function resets blur and sharpen sliders to initial
        #  position
      #  self.set_default_slider()
		
        # update V channel of the current image with histogram equallized matrix
		self.currentImage = self.imageLib.Blur(self.originalImage, self.kernel)
		self.blurImage = self.currentImage
		self.PSNR1 = self.imageLib.psnr(self.originalImage, self.currentImage)
		self.PSNR = self.imageLib.psnr(self.originalImage, self.blurImage)
		self.ui.label_5.setText(str(self.PSNR))
		self.ui.label_9.setText(str(self.PSNR1))
		self.SSIM1 = self.imageLib.ssim(self.originalImage, self.currentImage)
		self.SSIM = self.imageLib.ssim(self.originalImage, self.blurImage)
		self.ui.label_6.setText(str(self.SSIM))
		self.ui.label_12.setText(str(self.SSIM1))
        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
		self.displayImage_1()

	def full_inv(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
		self.updatePreviousImage()
        # update current operation code class variable
		self.currentOperationCode = 1
        # set_default_slider function resets blur and sharpen sliders to
        # initial position
       # self.set_default_slider()

        # open gamma input dialog box and wait for dialog box to exit
     
		self.currentImage = self.imageLib.full_inv(self.blurImage, self.kernel)
		self.PSNR1 = self.imageLib.psnr(self.originalImage, self.currentImage)
		self.PSNR = self.imageLib.psnr(self.originalImage, self.blurImage)
		self.ui.label_5.setText(str(self.PSNR))
		self.ui.label_9.setText(str(self.PSNR1))
		self.SSIM1 = self.imageLib.ssim(self.originalImage, self.currentImage)
		self.SSIM = self.imageLib.ssim(self.originalImage, self.blurImage)
		self.ui.label_6.setText(str(self.SSIM))
		self.ui.label_12.setText(str(self.SSIM1))
        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
		self.displayImage_1()

	def truncated_inv(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
		self.updatePreviousImage()
        # update current operation code class variable
		self.currentOperationCode = 2
        # set_default_slider function resets blur and sharpen sliders to
        # initial position	
        #self.set_default_slider()

	 # open d0 input dialog box and wait for dialog box to exit
		if self.newDialog.exec() == 0:
            # read gamma value from gamma input dialog box class
			d0 = self.newDialog.gamma
            # reset the value of gamma in gamma input dialog box to 1
			self.newDialog.gammaInput.setText('10.00')
			self.newDialog.gamma = 10.0
            # perform gamma correction for positive gamma values
            # gamma range is restricted to 0 to 10 in the gamma input
            # dialog box
			if d0 > 0:
				self.currentImage = self.imageLib.truncated_inv(self.blurImage, self.kernel, d0)
				self.PSNR1 = self.imageLib.psnr(self.originalImage, self.currentImage)
				self.PSNR = self.imageLib.psnr(self.originalImage, self.blurImage)
				self.ui.label_5.setText(str(self.PSNR))
				self.ui.label_9.setText(str(self.PSNR1))
				self.SSIM1 = self.imageLib.ssim(self.originalImage, self.currentImage)
				self.SSIM = self.imageLib.ssim(self.originalImage, self.blurImage)
				self.ui.label_6.setText(str(self.SSIM))
				self.ui.label_12.setText(str(self.SSIM1))
        # displayImage converts current image from ndarry format to
        # pixmap and assigns it to image display label
		self.displayImage_1()

	def wiener(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
		self.updatePreviousImage()
        # update current operation code class variable
		self.currentOperationCode = 3
        # set_default_slider function resets blur and sharpen sliders to
        # initial position
        #self.set_default_slider()
		if self.newDialog.exec() == 0:
            # read gamma value from gamma input dialog box class
			lambd = self.newDialog.gamma
            # reset the value of gamma in gamma input dialog box to 1
			self.newDialog.gammaInput.setText('0.05')
			self.newDialog.gamma = 0.05
            # perform gamma correction for positive gamma values
            # gamma range is restricted to 0 to 10 in the gamma input
            # dialog box
		if lambd > 0:
        # update current image with wiener restored image
			self.ui.pushButton_9.setEnabled(True)
			self.currentImage = self.imageLib.wiener(self.blurImage, self.kernel, lambd)
			self.PSNR1 = self.imageLib.psnr(self.originalImage, self.currentImage)
			self.PSNR = self.imageLib.psnr(self.originalImage, self.blurImage)
			self.ui.label_5.setText(str(self.PSNR))
			self.ui.label_9.setText(str(self.PSNR1))
			self.SSIM1 = self.imageLib.ssim(self.originalImage, self.currentImage)
			self.SSIM = self.imageLib.ssim(self.originalImage, self.blurImage)
			self.ui.label_6.setText(str(self.SSIM))
			self.ui.label_12.setText(str(self.SSIM1))
        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
		self.displayImage_1()

	def cls(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
		self.updatePreviousImage()

        # disconnect, initialize and reconnect the sharpen slider value
        # changed event
        # this is to avoid calling of sharpen function when sharpen slider
        # value is reset
        #self.ui.sharpenExtendInputSlider.valueChanged.disconnect()
        #self.ui.sharpenExtendInputSlider.setValue(0)
        #self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda:
         #                                                     self.sharpen())
        #self.ui.sharpenValueLabel.setText('0')

        # read current blur value from slider and compute blur window size as
        # (2 * slider value + 1)
        #blur_value = int(np.floor(self.ui.blurExtendInputSlider.value()))
        #blur_window_size = (blur_value * 2) + 1

        # if the operation being performed currently is blur, use initial image
        # passed to blur function
        # else set current image as initial image for blur
        #if self.currentOperationCode == 4:
         #   self.currentImage = self.imageBlur.copy()
        #else:
         #   self.imageBlur = self.currentImage.copy()
		if self.newDialog.exec() == 0:
            # read gamma value from gamma input dialog box class
			gamma = self.newDialog.gamma
            # reset the value of gamma in gamma input dialog box to 1
			self.newDialog.gammaInput.setText('0.00001')
			self.newDialog.gamma = 0.00001
            # perform gamma correction for positive gamma values
            # gamma range is restricted to 0 to 10 in the gamma input
            # dialog box
           
		if gamma > 0:
            # enable undo button
			self.ui.pushButton_9.setEnabled(True)
            # update V channel of the current image with blurred V matrix
			self.currentImage = self.imageLib.cls(self.blurImage, self.kernel, gamma)
			self.PSNR1 = self.imageLib.psnr(self.originalImage, self.currentImage)
			self.PSNR = self.imageLib.psnr(self.originalImage, self.blurImage)
			self.ui.label_5.setText(str(self.PSNR))
			self.ui.label_9.setText(str(self.PSNR1))
			self.SSIM1 = self.imageLib.ssim(self.originalImage, self.currentImage)
			self.SSIM = self.imageLib.ssim(self.originalImage, self.blurImage)
			self.ui.label_6.setText(str(self.SSIM))
			self.ui.label_12.setText(str(self.SSIM1))
        # update current operation code class variable
		self.currentOperationCode = 4

        #self.ui.blurValueLabel.setText(str(blur_value))
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
		self.displayImage_1()


	def undo(self):
		self.ui.pushButton_9.setEnabled(False)
		self.currentImage = self.previousImage.copy()
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
		self.displayImage_1()

	def undoAll(self):
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        #self.set_default_slider()
		self.currentImage = self.originalImage.copy()
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
		self.displayImage__1()
		self.ui.pushButton_10.setEnabled(False)

	def view_kernel(self):
        # count the no of values corresponding to each value in the V channel of
        # image matrix give a minimum length of 256 to the counting to ensure all 256 pixel
        # values are covered or pixel values not available in image are set to zero
		ker = self.kernel
        # start a new figure to show histogram - assign title and axes label
		plt.subplot(111),plt.imshow(ker)
		plt.title('Kernel'), plt.xticks([]), plt.yticks([])
		plt.show()


    # displayImage converts current image from ndarry format to pixmap and
    # assigns it to image display label
	def displayImage(self):
        # set display size to size of the image display label
		display_size = self.ui.label_3.size()
        # copy current image to temporary variable for processing pixmap
		image = np.array(self.currentImage.copy())
		zero = np.array([0])

        # display image if image is not [0] array
		if not np.array_equal(image, zero):
            # convert HSV image to RGB format for display in label
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # ndarray cannot be directly converted to QPixmap format required
            # by image display label
            # so ndarray is first converted to QImage and then QImage to QPixmap
            # convert image ndarray to QImage format
			qImage = QImage(image, self.imageWidth, self.imageHeight,
	                            self.imageWidth * 3, QImage.Format_RGB888)

            # convert QImage to QPixmap for loading in image display label
			pixmap = QPixmap()
			QPixmap.convertFromImage(pixmap, qImage)
			pixmap = pixmap.scaled(display_size, Qt.KeepAspectRatio,
                                   Qt.SmoothTransformation)
            # set pixmap to image display label in GUI
		self.ui.label_3.setPixmap(pixmap)


	def displayImage_1(self):
        # set display size to size of the image display label
		display_size = self.ui.label_4.size()
        # copy current image to temporary variable for processing pixmap
		image = np.array(self.currentImage.copy())
		zero = np.array([0])

        # display image if image is not [0] array
		if not np.array_equal(image, zero):
            # convert HSV image to RGB format for display in label
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # ndarray cannot be directly converted to QPixmap format required
            # by image display label
            # so ndarray is first converted to QImage and then QImage to QPixmap
            # convert image ndarray to QImage format
			qImage = QImage(image, self.imageWidth, self.imageHeight,
				self.imageWidth * 3, QImage.Format_RGB888)

            # convert QImage to QPixmap for loading in image display label
			pixmap = QPixmap()
			QPixmap.convertFromImage(pixmap, qImage)
			pixmap = pixmap.scaled(display_size, Qt.KeepAspectRatio,
				Qt.SmoothTransformation)
            # set pixmap to image display label in GUI
		self.ui.label_4.setPixmap(pixmap)
    # enable_options enable all buttons and sliders in the window. Only
    # Open button is enabled on start
    # Undo button remains disabled until an operation is performed
	def enable_options(self):
		self.ui.pushButton_2.setEnabled(True)
		self.ui.pushButton_4.setEnabled(True)
		self.ui.pushButton_5.setEnabled(True)
		self.ui.pushButton_6.setEnabled(True)
		self.ui.pushButton_7.setEnabled(True)

		self.ui.pushButton_3.setEnabled(True)
		self.ui.pushButton_10.setEnabled(True)
		self.ui.pushButton_9.setEnabled(False)

		self.ui.pushButton_12.setEnabled(True)
        
    # set_default_slider function resets blur and sharpen sliders to initial
    # position

	def updatePreviousImage(self):
		self.previousImage = self.currentImage.copy()

# initialize the ImageEditorClass and run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ImageRestorationClass()
    myapp.showMaximized()
    sys.exit(app.exec_())

