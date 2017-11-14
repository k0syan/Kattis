#include <iostream>
using namespace std;

int main() {
  int x, n;
  cin >> x;
  cin >> n;
  int left = 0;
  for (int i = 0; i < n; ++i) {
    int tmp;
    cin >> tmp;
    left += x;
    left -= tmp;
  }
  
  cout << left + x << endl;
  

  return 0;
}
