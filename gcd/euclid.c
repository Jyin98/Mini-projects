//euclid.c

#include <stdio.h>

int euclid(int a, int b){
	int divd = 0;
	int d = 0;
	int r = -1;
	int q = 0;
	int result = -1;
	
	//initialize
	if(a>b){
		divd = a;
		d = b;
	} else {
		divd = b;
		d = a;
	}
	
	//guard against divide by zero
	if(d==0){
		r = 0;
	}
	
	//perform euclid algorithm
	while(r!=0){
		result = d;
		q = divd/d;
		r = divd%d;
		if(r!=0){
			divd = d;
			d = r;
		}
	}
	
	if(result<0){
		result = -result;
	}
	
	return result;

}
