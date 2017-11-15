#include <iostream>
using namespace std;

int main () {
  int answer = 0;
  int count;
  
  cin >> count;
  
  for (int i = 0; i < count; ++i) {
    int tmp;
    cin >> tmp;
    if (tmp < 0) {
      ++answer;
    }
  }
  
  cout << answer << endl;

  return 0;
}
