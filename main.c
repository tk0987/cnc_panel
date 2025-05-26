#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/multicore.h"
#include "py/runtime.h"
#include "py/compile.h"
#include "py/repl.h"
#include "py/parse.h"

void core1_task() {
    printf("Running script on Core 1...\n");
    pyexec_file("main1.py");  // Run Python script on core 1
}

int main() {
    stdio_init_all();
    printf("Starting Core 1...\n");
    
    multicore_launch_core1(core1_task);  // Start Core 1 script

    printf("Running script on Core 0...\n");
    pyexec_file("main2.py");  // Run Python script on core 0

    while (1) {}
}
