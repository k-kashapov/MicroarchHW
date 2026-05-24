volatile int flag = 0x2132456;
volatile int storage[3] = {0, 1, 2};

extern "C" {

__attribute__((noinline)) int randomFunc() {
    int a = flag;
    char b = (flag >> 4) & 0xFD;

    if (b > 89) {
        storage[2] = -1;
    } else {
        storage[0] = a * 83;
    }

    return storage[0] + storage[1] + storage[2];
}

}
