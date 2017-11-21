#include <iostream>
#include <vector>
using namespace std;

int main() {
  int count;
  cin >> count;
  vector<int> numbers;
  
  for (int i = 0; i < count; ++i) {
    int tmp;
    cin >> tmp;
    numbers.push_back(tmp);
  }
  
  for (int i = 0; i < count; ++i) {
    if (numbers[i] % 2 == 0) {
      cout << numbers[i] << " is even" << endl;
    } else {
      cout << numbers[i] << " is odd" << endl;
    }
  }

  return 0;
}
