import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import serial
import colorsys
from datetime import datetime


#tyle.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# -- initSerialPort() ---------------------------------------------------
def initSerialPort():
	sh = serial.Serial("COM3" , 115200, timeout=None)
	sh.isOpen()

	for i in range(5):  # -- discard the first 5 lines
		aline = sh.readline().decode('utf-8').rstrip()
		print(aline)

	return sh

sh = initSerialPort();

# -- serial data feeder ------------------------------------------------
def serialfeeder():
	aline = sh.readline().decode('utf-8').rstrip()
	values = aline.split(',')
	return values


def rgb2hsv(r, g, b, c):
	r, g, b = r / c, g / c, b / c  # Normalising the rgb data by dividing by clear bit

	hsv = colorsys.rgb_to_hsv(r, g, b)

	return hsv[0] ,hsv[1],hsv[2]

t = []
h = []
s = []
v = []

def animate(i):
	values = serialfeeder()

	h_n, s_n, v_n = rgb2hsv(float(values[6]), float(values[7]), float(values[8]), float(values[9]))

	t.append(str(datetime.now().time()))
	h.append(h_n)
	s.append(s_n)
	v.append(v_n)

	ax1.clear()

	ax1.plot(t, h)
	ax1.plot(t, s)
	ax1.plot(t, v)

	ax2.clear()
	ax2.plot(t, h)
	ax2.plot(t, s)
	ax2.plot(t, v)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()




