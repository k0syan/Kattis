#include <iostream>
#include <vector>
using namespace std;

int main() {
  int count;
  cin >> count;
  
  int answer = 0;
  
  vector<int> numbers;
  
  for (int i = 0; i < count; ++i) {
    int tmp;
    cin >> tmp;
    
    int pow = 0;
    int p = 1;
    pow = tmp % 10;
    tmp /= 10;
    
    for (int j = 0; j < pow; ++j) {
      p *= tmp;
    }
    
    answer += p;
  }
  
  cout << answer << endl;

  return 0;
}
