
#include <iostream>

#include "pkg/hello.h"
using namespace std;

int main() {
  say(const_cast<char*>("hello world"));
  cout << "here" << endl;
  int x;
}
