#DecimalToBinary.py
#
#Description: This program will convert base ten numbers to base two.
#
#Coded by John

invalid = True;
running = True;

while(running):
    decimal = 0;
    binary = [];
    output = '';
    output2='';
    output3='';
    output4='';
    output4L=[];
    output5='';
    output5L=[];
    over=True;
    remainder = 0;
    carry =0;
    counter=0; 
    while (invalid):
        decimal = str(input("Enter a decimal (base ten) number you wish to convert: "));
        if(decimal!="x"):
            if(decimal.isnumeric()):
                carry = int(decimal);
                invalid = False;
            else:
                print("Invalid input. Please enter a number.");
        else:
            running = False;
            invalid = False;
            
    if(running==True):
        while(carry>0):
            remainder = carry%2;
            carry = int(carry/2);
            binary.append(remainder);
            counter+=1;
          
        for element in range(counter,0,-1):
            output = output+str(binary[element-1])


        for bit in range(8):
            if(bit<(8-counter)):
                output2=output2+"0"    
            else:
                output2=output2+str(binary[7-bit])
                
        for bit in range(8):
            if(bit==0):
                output3="1"
            elif(bit<(8-counter)):
                output3=output3+"0"
            else:
                output3=output3+str(binary[7-bit])        

        output4L = list(output2)
        for bit in range(8):
            if(output4L[bit]=='0'):
                output4L[bit]='1'
                output4=output4+output4L[bit]
            else:
                output4L[bit]='0'
                output4=output4+output4L[bit]

                
        print("\n----------BINARY NUMBER----------")    
        print("The decimal number",decimal,"can be represented in binary as: ",output)

        print("----------EXTRA CASES (8 bits)----------")
        if(counter<=8):
            print("The padded version of the binary number:",output2)
            print("The negative version, -",decimal,"for sign-and-magnitude is:",output3)
            print("The negative version, -",decimal,"for 1's compliment is:",output4)
        else:
            print("No information available for",counter,"bits.")
    invalid=True;
