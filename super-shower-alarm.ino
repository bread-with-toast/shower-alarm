int buzzerPin = 3;
int varResPin = A0;
int led = 4;
int thermistor = A2;

void setup() {
    Serial.begin(9600);
    
    pinMode(buzzerPin, OUTPUT);
    pinMode(varResPin, INPUT);
    pinMode(thermistor, INPUT);
    pinMode(led, OUTPUT);

    randomSeed(analogRead(A1));
}

int alarm() {
    for (int i=1;i<=3;i++) {
        digitalWrite(led, HIGH);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
        analogWrite(buzzerPin, random(25, 255));
        delay(1000);
    }

    digitalWrite(buzzerPin, LOW);
    digitalWrite(led, LOW);
    delay(500);
}

void loop() {
    /* 
    Max Value: ~1024
    1024 * 585.9375 = 600,000ms 
    600,000ms = 10 minutes
    10 minutes is the maximum time before the buzzer goes off for 30 seconds
    */
    Serial.print("It is currently ~");
    Serial.print(analogRead(thermistor) / 22);
    Serial.print(" degrees Celsius. ");

    Serial.print("The time till the alarm goes off is: ");
    Serial.print((analogRead(varResPin) * 585.9375) / 1000);
    Serial.print(" seconds ");

    Serial.print("or ");
    Serial.print((analogRead(varResPin) * 585.9375) / 60000);
    Serial.println(" minutes.");
    
    delay(analogRead(varResPin) * 585.9375);
    alarm();
}
