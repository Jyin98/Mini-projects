//gcd.c

#include <stdio.h>
#include <stdlib.h>

int euclid(int, int);

int main(int argc, char ** argv){

	//terminate program if less than one number
	if(argc<2){
		exit(0);
	}
	
	//initialize array of int and convert from args to values
	int numbers[argc-1];
	for(int i=1; i<argc; i++){
		//invalid characters would return 0 and cause divide by zero error
		numbers[i-1] = atoi(argv[i]);		
	}
	
	//perform the gcd
	int a = numbers[0];
	int gcd = a;
	
	for(int i=1; i<argc-1; i++){
		gcd = euclid(gcd, numbers[i]);
	}
	
	if(gcd!=-1){
		printf("%d\n",gcd);
	} else {
		printf("Divide by zero error.\n");
	}
	
	return 0;
}
