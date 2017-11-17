#include <iostream>
#include <math.h>

using namespace std;

int main () {

  float area;
  cin >> area;
  float length;
  
  float side = sqrt(area);
  length = 4 * side;
  
  cout << length << endl;
  
  return 0;
}
