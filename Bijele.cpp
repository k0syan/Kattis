#include <iostream>
#include <vector>
using namespace std;

int main () {
  vector<int> required = {1, 1, 2, 2, 2, 8};
  
  for (int i = 0; i < 6; ++i) {
    int tmp;
    cin >> tmp;
    required[i] -= tmp;
  }
  
  for (int i = 0; i < 6; ++i) {
    cout << required[i] << " ";
  }
  
  cout << endl;

  return 0;
}
