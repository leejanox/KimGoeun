#include <stdio.h>
//stdio.h에서 가져다 쓰겠다. 
int main() //매개변수 자리에 void 생략 가능(매개변수가 없다.) 
{
	int i,j,k =0;
	
	for(k=0; k<5; k++)
	
	{
		for(j=1; j<9; j++)
		{	
			for(i=1+3*k; i<=3+3*k; i++)
			{
				printf("%d * %d= %d\t", i,j, i*j);
				if(i%3==0) printf("\n");
			}
		}
		printf("\n");
	}
	
	return 0;
}
