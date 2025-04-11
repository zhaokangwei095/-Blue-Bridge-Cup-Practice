#include <stdio.h>
#include <stdlib.h>
#include<cstdio>
using namespace std;
char a[101][101];
int ans;
int n,m;
void dfs(int x,int y){
    a[x][y]='.';
    int dx,dy;
    for(int i=-1;i<=1;i++){
        for(int j=-1;j<=1;j++){
            dx=x+i;
            dy=y+j;
            if(dx>=0&&dx<=n&&dy>=0&&dy<m&&a[dx][dy]=='W'){
                dfs(dx,dy);
            }
        }
    }
    return;
} 
int main(){
    scanf("%d%d",&n,&m);
    for(int i=0;i<=n;i++){
    	scanf("%s",a[i]);//避免换行带来问题这里直接读入字符串
    }
    for(int i=0;i<=n;i++){
        for(int j=0;j<m;j++){
            if(a[i][j]=='W'){//如果是W的话就直接开始遍历
                dfs(i,j);
                ans++;//水潭加一处
            }
        }
    }
    printf("%d",ans);
    return 0;
}

