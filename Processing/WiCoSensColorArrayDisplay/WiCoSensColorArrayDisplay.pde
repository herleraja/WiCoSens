
// Example by Tom Igoe

import processing.serial.*;
import java.awt.Color.*;

int lf = 10;    // Linefeed in ASCII
String myString = null;
Serial myPort;  // The serial port

float rect_w = 75;
float rect_h = 200;
float rect_w_text = 600;
float rect_h_text = 220;
float rect_text_x = 340;
float rect_text_y = 200;
float text_x = 600;
float text_y = 280;
float rect_curve = 10; // corner radius

void setup() {
  size(900, 200);
  noStroke();
  background(255);
  // List all the available serial ports
  printArray(Serial.list());
  // Open the port you are using at the rate you want:
  myPort = new Serial(this, Serial.list()[0], 9600);
  myPort.clear();
  // Throw out the first reading, in case we started reading 
  // in the middle of a string from the sender.
  myString = myPort.readStringUntil(lf);
  myString = null;
}

float floatRangeConvert(float value) {
  float  returnValue = map(value, 0, 1, 0, 255);
  return returnValue;
}

void draw() {

  while (myPort.available() > 0) {
    myString = myPort.readStringUntil(lf);
    if (myString != null) {
      println(myString);

      String[]  myStringArray = myString.split(",");
      if (myStringArray.length==52) {


        fill(floatRangeConvert(float(myStringArray[48])/float(myStringArray[51])), floatRangeConvert(float(myStringArray[49])/float(myStringArray[51])), floatRangeConvert(float(myStringArray[50])/float(myStringArray[51])));
        rect(0, 0, rect_w, rect_h, rect_curve); 

        fill(floatRangeConvert(float(myStringArray[44])/float(myStringArray[47])), floatRangeConvert(float(myStringArray[45])/float(myStringArray[47])), floatRangeConvert(float(myStringArray[46])/float(myStringArray[47])));
        rect(1*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[40])/float(myStringArray[43])), floatRangeConvert(float(myStringArray[41])/float(myStringArray[43])), floatRangeConvert(float(myStringArray[42])/float(myStringArray[43])));
        rect(2*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[36])/float(myStringArray[39])), floatRangeConvert(float(myStringArray[37])/float(myStringArray[39])), floatRangeConvert(float(myStringArray[38])/float(myStringArray[39])));
        rect(3*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[32])/float(myStringArray[35])), floatRangeConvert(float(myStringArray[33])/float(myStringArray[35])), floatRangeConvert(float(myStringArray[34])/float(myStringArray[35])));
        rect(4*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[28])/float(myStringArray[31])), floatRangeConvert(float(myStringArray[30])/float(myStringArray[31])), floatRangeConvert(float(myStringArray[31])/float(myStringArray[31])));
        rect(5*rect_w, 0, rect_w, rect_h, rect_curve); //  middle sensor

        fill(floatRangeConvert(float(myStringArray[24])/float(myStringArray[27])), floatRangeConvert(float(myStringArray[25])/float(myStringArray[27])), floatRangeConvert(float(myStringArray[26])/float(myStringArray[27])));
        rect(6*rect_w, 0, rect_w, rect_h, rect_curve); //  

        fill(floatRangeConvert(float(myStringArray[20])/float(myStringArray[23])), floatRangeConvert(float(myStringArray[21])/float(myStringArray[23])), floatRangeConvert(float(myStringArray[22])/float(myStringArray[23])));
        rect(7*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[16])/float(myStringArray[19])), floatRangeConvert(float(myStringArray[17])/float(myStringArray[19])), floatRangeConvert(float(myStringArray[18])/float(myStringArray[19])));
        rect(8*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[12])/float(myStringArray[15])), floatRangeConvert(float(myStringArray[13])/float(myStringArray[15])), floatRangeConvert(float(myStringArray[14])/float(myStringArray[15])));
        rect(9*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[8])/float(myStringArray[11])), floatRangeConvert(float(myStringArray[9])/float(myStringArray[11])), floatRangeConvert(float(myStringArray[10])/float(myStringArray[11])));
        rect(10*rect_w, 0, rect_w, rect_h, rect_curve); // 

        fill(floatRangeConvert(float(myStringArray[4])/float(myStringArray[7])), floatRangeConvert(float(myStringArray[5])/float(myStringArray[7])), floatRangeConvert(float(myStringArray[6])/float(myStringArray[7])));
        rect(11*rect_w, 0, rect_w, rect_h, rect_curve); // 


        /*
    float[] hsb = java.awt.Color.RGBtoHSB(int(float(myStringArray[6])*255/float(myStringArray[9])), int(float(myStringArray[7])*255/float(myStringArray[9])), int(float(myStringArray[8])*255/float(myStringArray[9])), null);
         
         float hue = hsb[0]; 
         float saturation = hsb[1];
         float brightness = hsb[2];
         
         if(brightness >0.4 & brightness <0.98  ) {
         if(saturation > 0.05){
         // int past_time = millis();
         // println(past_time-first_time);
         if(hue > 0 & hue < 0.02){
         fill(0, 102, 153);
         text("Red", text_x, text_y);
         }
         else if(hue >= 0.1 & hue < 0.17){
         fill(0, 102, 153);
         text("Yellow", text_x, text_y);
         }
         else if(hue >= 0.022 & hue < 0.036){
         fill(0, 102, 153);
         text("Orange", text_x, text_y);
         }
         else if(hue >= 0.7 & hue < 0.8){
         fill(0, 102, 153);
         text("Violet", text_x, text_y);
         }
         else if(hue >= 0.45 & hue < 0.55){
         fill(0, 102, 153);
         text("Light-Blue", text_x, text_y);
         }
         else if(hue >= 0.57 & hue < 0.66){
         fill(0, 102, 153);
         text("Dark-Blue", text_x, text_y);
         }
         else if(hue >= 0.24 & hue < 0.3){
         fill(0, 102, 153);
         text("Light-Green", text_x, text_y);
         }
         else if(hue >= 0.3 & hue < 0.4){
         fill(0, 102, 153);
         text("Dark-Green", text_x, text_y);
         }
         }  
         }
         else {
         fill(0, 102, 153);
         text(" ", 550, 280);
         }
         
         
         fill(float(myStringArray[6])*255/float(myStringArray[9]), float(myStringArray[7])*255/float(myStringArray[9]), float(myStringArray[8])*255/float(myStringArray[9]));
         rect(0, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[10])*255/float(myStringArray[13]), float(myStringArray[11])*255/float(myStringArray[13]), float(myStringArray[12])*255/float(myStringArray[13]));
         rect(rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[14])*255/float(myStringArray[15]), float(myStringArray[15])*255/float(myStringArray[15]), float(myStringArray[16])*255/float(myStringArray[15]));
         rect(2*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[16])*255/float(myStringArray[19]), float(myStringArray[17])*255/float(myStringArray[19]), float(myStringArray[18])*255/float(myStringArray[19]));
         rect(3*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[20])*255/float(myStringArray[23]), float(myStringArray[21])*255/float(myStringArray[23]), float(myStringArray[22])*255/float(myStringArray[23]));
         rect(4*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[24])*255/float(myStringArray[27]), float(myStringArray[25])*255/float(myStringArray[27]), float(myStringArray[26])*255/float(myStringArray[27]));
         rect(5*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[28])*255/float(myStringArray[31]), float(myStringArray[30])*255/float(myStringArray[31]), float(myStringArray[31])*255/float(myStringArray[31]));
         rect(6*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[32])*255/float(myStringArray[35]), float(myStringArray[33])*255/float(myStringArray[35]), float(myStringArray[34])*255/float(myStringArray[35]));
         rect(7*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[36])*255/float(myStringArray[39]), float(myStringArray[37])*255/float(myStringArray[39]), float(myStringArray[38])*255/float(myStringArray[39]));
         rect(8*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[42])*255/float(myStringArray[45]), float(myStringArray[43])*255/float(myStringArray[45]), float(myStringArray[44])*255/float(myStringArray[45]));
         rect(9*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[46])*255/float(myStringArray[49]), float(myStringArray[47])*255/float(myStringArray[49]), float(myStringArray[48])*255/float(myStringArray[49]));
         rect(10*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[50])*255/float(myStringArray[53]), float(myStringArray[51])*255/float(myStringArray[53]), float(myStringArray[52])*255/float(myStringArray[53]));
         rect(11*rect_w, 0, rect_w, rect_h, rect_curve); 
         
         
         OR
         
         fill(floatRangeConvert(float(myStringArray[6])/float(myStringArray[9])), floatRangeConvert(float(myStringArray[7])/float(myStringArray[9])), floatRangeConvert(float(myStringArray[8])/float(myStringArray[9])));
         rect(0, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[10])/float(myStringArray[13])), floatRangeConvert(float(myStringArray[11])/float(myStringArray[13])), floatRangeConvert(float(myStringArray[12])/float(myStringArray[13])));
         rect(rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[14])/float(myStringArray[15])),floatRangeConvert(float(myStringArray[15])/float(myStringArray[15])), floatRangeConvert(float(myStringArray[16])/float(myStringArray[15])));
         rect(2*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[16])/float(myStringArray[19])), floatRangeConvert(float(myStringArray[17])/float(myStringArray[19])), floatRangeConvert(float(myStringArray[18])/float(myStringArray[19])));
         rect(3*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[20])/float(myStringArray[23])), floatRangeConvert(float(myStringArray[21])/float(myStringArray[23])), floatRangeConvert(float(myStringArray[22])/float(myStringArray[23])));
         rect(4*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[24])/float(myStringArray[27])), floatRangeConvert(float(myStringArray[25])/float(myStringArray[27])), floatRangeConvert(float(myStringArray[26])/float(myStringArray[27])));
         rect(5*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[28])/float(myStringArray[31])), floatRangeConvert(float(myStringArray[30])/float(myStringArray[31])), floatRangeConvert(float(myStringArray[31])/float(myStringArray[31])));
         rect(6*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[32])/float(myStringArray[35])), floatRangeConvert(float(myStringArray[33])/float(myStringArray[35])), floatRangeConvert(float(myStringArray[34])/float(myStringArray[35])));
         rect(7*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[36])/float(myStringArray[39])), floatRangeConvert(float(myStringArray[37])/float(myStringArray[39])), floatRangeConvert(float(myStringArray[38])/float(myStringArray[39])));
         rect(8*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[42])/float(myStringArray[45])), floatRangeConvert(float(myStringArray[43])/float(myStringArray[45])), floatRangeConvert(float(myStringArray[44])/float(myStringArray[45])));
         rect(9*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[46])/float(myStringArray[49])), floatRangeConvert(float(myStringArray[47])/float(myStringArray[49])), floatRangeConvert(float(myStringArray[48])/float(myStringArray[49])));
         rect(10*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(floatRangeConvert(float(myStringArray[50])/float(myStringArray[53])), floatRangeConvert(float(myStringArray[51])/float(myStringArray[53])), floatRangeConvert(float(myStringArray[52])/float(myStringArray[53])));
         rect(11*rect_w, 0, rect_w, rect_h, rect_curve); 
         
         
         
         OR
         
         
         fill(float(myStringArray[6]), float(myStringArray[7]), float(myStringArray[8]));
         rect(0, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[10]), float(myStringArray[11]), float(myStringArray[12]));
         rect(rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[14]), float(myStringArray[15]), float(myStringArray[16]));
         rect(2*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[16]), float(myStringArray[17]), float(myStringArray[18]));
         rect(3*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[20]), float(myStringArray[21]), float(myStringArray[22]));
         rect(4*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[24]), float(myStringArray[25]), float(myStringArray[26]));
         rect(5*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[28]), float(myStringArray[30]), float(myStringArray[31]));
         rect(6*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[32]), float(myStringArray[33]), float(myStringArray[34]));
         rect(7*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[36]), float(myStringArray[37]), float(myStringArray[38]));
         rect(8*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[42]), float(myStringArray[43]), float(myStringArray[44]));
         rect(9*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[46]), float(myStringArray[47]), float(myStringArray[48]));
         rect(10*rect_w, 0, rect_w, rect_h, rect_curve); // 
         
         fill(float(myStringArray[50]), float(myStringArray[51]), float(myStringArray[52]));
         rect(11*rect_w, 0, rect_w, rect_h, rect_curve);
         
         */
      }
    }
  }
}// Examp
