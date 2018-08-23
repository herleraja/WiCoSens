#!/usr/bin/env python
"""
Modified the animation example code, "strip_chart_demo.py" to plot
data collected from serial port.
"""
import matplotlib

#matplotlib.use('TkAgg')

import serial
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import colorsys


# -- Scope() ------------------------------------------------------------
class Scope(object):
	def __init__(self, ax, maxt=2, dt=0.02):
		self.ax = ax
		self.dt = dt
		self.maxt = maxt

		self.line_hR5,self.line_sR5,self.line_vR5, self.tdata_R5, self.ydata_hR5,self.ydata_sR5, self.ydata_vR5 =self.createAX(self.ax[0,0])

		self.line_hR4, self.line_sR4, self.line_vR4, self.tdata_R4, self.ydata_hR4,self.ydata_sR4, self.ydata_vR4 = self.createAX(self.ax[0, 1])



	def createAX(self, ax):

		tdata = [0]  # x data
		ydata_h = [0]  # y data for line 1 (h)
		ydata_s = [0]  # y data for line 2 (s)
		ydata_v = [0]  # y data for line 3 (v)

		line_h = Line2D(tdata, ydata_h, color='r', label='h')  # red
		line_s = Line2D(tdata, ydata_s, color='b', label='s')  # blue
		line_v = Line2D(tdata, ydata_v, color='g', label='v')  # green

		ax.add_line(line_h)
		ax.add_line(line_s)
		ax.add_line(line_v)
		ax.set_xlabel('Time(s)', fontsize=10)
		ax.set_ylabel('Color(h, s, v)', fontsize=10)
		ax.set_title('Color (h, s, v) plotting')
		ax.legend(loc='upper left', fontsize=9)
		ax.grid(True)

		return line_h, line_s, line_v, tdata,ydata_h,ydata_s,ydata_v

	def updateSubPlot(self, line_h, line_s, line_v, tdata,ydata_h,ydata_s,ydata_v, r, g,b,c):
		lastt = tdata[-1]
		if lastt > tdata[0] + self.maxt:  # reset the arrays
			tdata = [tdata[-1]]
			ydata_h = [ydata_h[-1]]
			ydata_s = [ydata_s[-1]]
			ydata_v = [ydata_v[-1]]
			# self.ydata_mg = [self.ydata_mg[-1]]
			ax.set_xlim(tdata[0], tdata[0] + self.maxt)
			ax.set_ylim([0, 1])
			ax.figure.canvas.draw()

		t = tdata[-1] + self.dt
		# h = float(values[1])
		# s = float(values[2])
		# v = float(values[3])

		h, s, v = rgb2hsv(float(r), float(g), float(b), float(c))
		# mg = np.sqrt(gx ** 2 + gy ** 2 + gz ** 2)
		tdata.append(t)
		ydata_h.append(h)
		ydata_s.append(s)
		ydata_v.append(v)
		# self.ydata_mg.append(mg)

		line_h.set_data(tdata, ydata_h)
		line_s.set_data(tdata, ydata_s)
		line_v.set_data(tdata, ydata_v)

		return line_h,line_s,line_v

	def update(self, values):

		lastt = self.tdata_R5[-1]

		if lastt > self.tdata_R5[0] + self.maxt:  # reset the arrays
			self.tdata_R5 = [self.tdata_R5[-1]]
			self.ydata_hR5 = [self.ydata_hR5[-1]]
			self.ydata_sR5 = [self.ydata_sR5[-1]]
			self.ydata_vR5 = [self.ydata_vR5[-1]]

			self.ax[0,0].set_xlim(self.tdata_R5[0], self.tdata_R5[0] + self.maxt)
			self.ax[0,0].set_ylim([0, 1])
			self.ax[0,0].figure.canvas.draw()

		t = self.tdata_R5[-1] + self.dt

		h, s, v = rgb2hsv(float(values[6]),float(values[7]),float(values[8]),float(values[9]))

		self.tdata_R5.append(t)
		self.ydata_hR5.append(h)
		self.ydata_sR5.append(s)
		self.ydata_vR5.append(v)

		self.line_hR5.set_data(self.tdata_R5, self.ydata_hR5)
		self.line_sR5.set_data(self.tdata_R5, self.ydata_sR5)
		self.line_vR5.set_data(self.tdata_R5, self.ydata_vR5)

		lastt = self.tdata_R4[-1]

		if lastt > self.tdata_R4[0] + self.maxt:  # reset the arrays

			self.tdata_R4 = [self.tdata_R4[-1]]
			self.ydata_hR4 = [self.ydata_hR4[-1]]
			self.ydata_sR4 = [self.ydata_sR4[-1]]
			self.ydata_vR4 = [self.ydata_vR4[-1]]

			self.ax[0,1].set_xlim(self.tdata_R4[0], self.tdata_R4[0] + self.maxt)
			self.ax[0,1].set_ylim([0, 1])
			self.ax[0,1].figure.canvas.draw()

		t = self.tdata_R4[-1] + self.dt

		h, s, v = rgb2hsv(float(values[10]), float(values[11]), float(values[12]),float(values[13]))

		self.tdata_R4.append(t)
		self.ydata_hR4.append(h)
		self.ydata_sR4.append(s)
		self.ydata_vR4.append(v)

		self.line_hR4.set_data(self.tdata_R4, self.ydata_hR4)
		self.line_sR4.set_data(self.tdata_R4, self.ydata_sR4)
		self.line_vR4.set_data(self.tdata_R4, self.ydata_vR4)


		return self.line_hR5, self.line_sR5, self.line_vR5,self.line_hR4, self.line_sR4, self.line_vR4  #, self.line_mg


def rgb2hsv(r, g, b, c):
	if c!=0:
		r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

	hsv = colorsys.rgb_to_hsv(r, g, b)

	return hsv[0] ,hsv[1],hsv[2]

# -- initSerialPort() ---------------------------------------------------
def initSerialPort():
	sh = serial.Serial("COM3" , 115200, timeout=None)
	sh.isOpen()

	for i in range(5):  # -- discard the first 5 lines
		aline = sh.readline().decode('utf-8').rstrip()
		print(aline)

	return sh


# -- serial data feeder ------------------------------------------------
def serialfeeder():
	aline = sh.readline().decode('utf-8').rstrip()
	values = aline.split(',')
	yield values


# ----------------------------------------------------------------------
fig, ax = plt.subplots(2,2)


sh = initSerialPort();

scope = Scope(ax)
try:
    ani = animation.FuncAnimation(fig, scope.update, serialfeeder, interval=10, blit=True)
except KeyboardInterrupt:
    print('nnKeyboard exception received. Exiting.')
    plt.close()
    sh.close()
    exit()

plt.show()