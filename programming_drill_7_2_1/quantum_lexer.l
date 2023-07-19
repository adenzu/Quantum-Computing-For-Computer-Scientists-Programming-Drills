%{
%}

INT [1-9]+[0-9]*

%%
INITIALIZE {printf("INIT");} 
SELECT {printf("SLCT");}
APPLY {printf("APLY");}
CONCAT {printf("CNCT");}
TENSOR {printf("TNSR");}
INVERSE {printf("NVRS");}
MEASURE {printf("MESR");}

R{INT}? {printf("QREG");}
S{INT}? {printf("VRBL");}
U{INT}? {printf("OPRT");}
RES {printf("RES");}

H {printf("HDMR");}
R"_("{INT}/{INT}")" {printf("ROTT");}
I"_"{INT} {printf("IDNT");}
CNOT {printf("CNOT");}

0 |
{INT} {printf("INT");}
"["[01]+"]" {printf("BITARR");}
%%

int yywrap(){}
int main(int argc, char** argv) {
    yylex();
    return 0;
}