
int left = 0;
int right = 1;
int stop = 9;
int pins[4];
int estados[4][8];

void Steps(int steps, int direction)
{

if (direction == left){
    for (int j=0;j<steps;j++){
        for (int i=0; i<8;i++){
            delay(5);
            digitalWrite(pins[0],estados[0][i]);
            digitalWrite(pins[1],estados[1][i]);
            digitalWrite(pins[2],estados[2][i]);
            digitalWrite(pins[3],estados[3][i]);
        } 
    }
}
else if (direction == right){
    for (int j=0;j<steps;j++){
        for (int i=8; i>-1;i--){
            delay(5);
            digitalWrite(pins[0],estados[0][i]);
            digitalWrite(pins[1],estados[1][i]);
            digitalWrite(pins[2],estados[2][i]);
            digitalWrite(pins[3],estados[3][i]);
        }
    }
}
else{
    digitalWrite(pins[0],0);
    digitalWrite(pins[1],0);
    digitalWrite(pins[2],0);
    digitalWrite(pins[3],0);
}
}

void setup()
{
pins[0] = 6;
pins[1] = 9;
pins[2] = 10;
pins[3] = 11;
pinMode(pins[0],OUTPUT);
pinMode(pins[1],OUTPUT);
pinMode(pins[2],OUTPUT);
pinMode(pins[3],OUTPUT);


//4 pins, 8 states
//PIN 0
int j = 0;
estados[j][0] = 0;
estados[j][1] = 0;
estados[j][2] = 0;
estados[j][3] = 0;
estados[j][4] = 0;
estados[j][5] = 1;
estados[j][6] = 1;
estados[j][7] = 1;

//PIN1
j = 1;
estados[j][0] = 0;
estados[j][1] = 0;
estados[j][2] = 0;
estados[j][3] = 1;
estados[j][4] = 1;
estados[j][5] = 1;
estados[j][6] = 0;
estados[j][7] = 0;

//PIN2
j = 2;
estados[j][0] = 0;
estados[j][1] = 1;
estados[j][2] = 1;
estados[j][3] = 1;
estados[j][4] = 0;
estados[j][5] = 0;
estados[j][6] = 0;
estados[j][7] = 0;

//PIN3
j = 3;
estados[j][0] = 1;
estados[j][1] = 1;
estados[j][2] = 0;
estados[j][3] = 0;
estados[j][4] = 0;
estados[j][5] = 0;
estados[j][6] = 0;
estados[j][7] = 1;

}

void loop()
{
    Steps(500,left);
    Steps(0,stop);
    delay(300);
    Steps(500,right);
    Steps(0,stop);
    delay(300);
}
