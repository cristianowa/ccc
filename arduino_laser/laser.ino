int laserPin = 3;
void setup()
{
}
void loop()
{
    /* top value is 170 3V3/5V = 0.66 => 255*0.66 ~= 170 */
     
   analogWrite(laserPin,168); 
   delay(200);
   analogWrite(laserPin,0); 
   delay(200);
}
