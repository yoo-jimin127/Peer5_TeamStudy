// 백준 2290 - LCD Test

#include <iostream>
#include <string>
using namespace std;

int s = 0; // s : 크기 ( 1 <= s && s <= 10 )
string n = ""; // n : 모니터에 나타내야 할 수 ( 0 <= n && n <= 9,999,999,999)

// 숫자 출력 조건 : 가로 = s + 2 / 세로 = 2s + 3
// 0~9까지의 7개 dash로 이루어진 배열
int printArr[10][7] = {
    {1, 1, 1, 0, 1, 1, 1}, //0
    {0, 0, 1, 0, 0, 1, 0}, //1
    {1, 0, 1, 1, 1, 0, 1}, //2
    {1, 0, 1, 1, 0, 1, 1}, //3
    {0, 1, 1, 1, 0, 1, 0}, //4
    {1, 1, 0, 1, 0, 1, 1}, //5
    {1, 1, 0, 1, 1, 1, 1}, //6
    {1, 0, 1, 0, 0, 1, 0}, //7
    {1, 1, 1, 1, 1, 1, 1}, //8
    {1, 1, 1, 1, 0, 1, 1} //9
};

void printLCD(char c, int idx) {
    
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> s >> n; // s, n 입력

}