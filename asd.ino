int a[] = {2,3,4,5,6,7,8};

int c[7][7] ={// Arduino
            {0,0,0,1,0,0,0}, 
            {1,1,1,1,0,1,0},
            {1,0,0,0,0,1,0},
            {1,1,0,0,0,1,1},
            {1,1,1,1,0,0,1},
            {1,1,0,1,0,1,0},
            {1,1,0,0,0,1,0},
            
            };

int uno[3][7] = {
  			{1,1,0,0,0,1,1},
            {1,1,0,1,0,1,0},
            {1,1,0,0,0,1,0},


			};


int led = 7;
int sw = 13;

void setup() {
  Serial.begin(9600);
  for(int i=0; i<led; i++) {
    pinMode(a[i],OUTPUT);
  }
  pinMode(sw , INPUT_PULLUP);
}

void loop () {
  if(Serial.available() >0) {
  char r = Serial.read();
  Serial.println(r);	  
  switch(r) {
   case 'A': 
    for(int i=0; i<7; i++) {
    	for(int j=0; j<led; j++) {
     	 digitalWrite(a[j] , c[i][j]);
    }
    delay(500);
    for(int k=0; k<led; k++) {
    	digitalWrite(a[k] , HIGH);
      }
    
  
    }break;
    
    case 'U' :
    for(int i=0; i<3; i++) {
    	for(int j=0; j<led; j++) {
     	 digitalWrite(a[j] , uno[i][j]);
    }
    delay(500);
    for(int k=0; k<led; k++) {
    	digitalWrite(a[k] , HIGH);
    }
       
    }break;
    
    
  

  }

}
}