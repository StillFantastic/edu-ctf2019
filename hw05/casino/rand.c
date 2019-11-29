#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main() {
  srand(1480288863);
  for (int i = 0; i < 6; i++) {
    printf("%d ", rand() % 100);
  } 

  printf("\n");
  return 0;
}
