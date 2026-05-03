---
title: freertos
url: https://skills.sh/mohitmishra786/low-level-dev-skills/freertos
---

# freertos

skills/mohitmishra786/low-level-dev-skills/freertos
freertos
Installation
$ npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill freertos
SKILL.md
FreeRTOS
Purpose

Guide agents through FreeRTOS application development: task creation and priorities, inter-task communication with queues and semaphores, stack overflow detection, configASSERT, and FreeRTOS-aware debugging with GDB and OpenOCD.

Triggers
"How do I create a FreeRTOS task?"
"How do I pass data between FreeRTOS tasks?"
"My FreeRTOS task is crashing — how do I detect stack overflow?"
"How do I use FreeRTOS mutexes?"
"How do I debug FreeRTOS tasks with GDB?"
"How do I configure FreeRTOSConfig.h?"
Workflow
1. Task creation and priorities
#include "FreeRTOS.h"
#include "task.h"

// Task function signature
void vMyTask(void *pvParameters) {
    const char *name = (const char *)pvParameters;
    for (;;) {
        // Task body — must never return
        printf("Task %s running\n", name);
        vTaskDelay(pdMS_TO_TICKS(500));  // yield for 500ms
    }
}

int main(void) {
    // xTaskCreate(function, name, stack_depth_words, param, priority, handle)
    TaskHandle_t xHandle = NULL;
    xTaskCreate(vMyTask, "MyTask",
                configMINIMAL_STACK_SIZE + 128,  // words, not bytes!
                (void *)"sensor",
                tskIDLE_PRIORITY + 2,            // higher = more urgent
                &xHandle);

    vTaskStartScheduler();  // never returns if heap is sufficient
    for (;;);               // should never reach here
}


Priority guidelines:

tskIDLE_PRIORITY (0) — idle task, never block here
ISR-deferred tasks — highest priority to service interrupts quickly
Avoid priorities above configMAX_PRIORITIES - 1
2. Queues — inter-task data passing
#include "queue.h"

typedef struct { uint32_t sensor_id; float value; } SensorReading_t;

QueueHandle_t xSensorQueue;

void vProducerTask(void *pvParam) {
    SensorReading_t reading;
    for (;;) {
        reading.sensor_id = 1;
        reading.value = read_adc();
        // Send; block max 10ms if queue full
        xQueueSend(xSensorQueue, &reading, pdMS_TO_TICKS(10));
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

void vConsumerTask(void *pvParam) {
    SensorReading_t reading;
    for (;;) {
        // Block forever until item available
        if (xQueueReceive(xSensorQueue, &reading, portMAX_DELAY) == pdTRUE) {
            process(reading.value);
        }
    }
}

// Create before starting scheduler
xSensorQueue = xQueueCreate(10, sizeof(SensorReading_t));


From ISR: use xQueueSendFromISR() and pass &xHigherPriorityTaskWoken.

3. Semaphores and mutexes
#include "semphr.h"

// Binary semaphore — signaling (ISR→task)
SemaphoreHandle_t xSem = xSemaphoreCreateBinary();

void UART_ISR(void) {
    BaseType_t xWoken = pdFALSE;
    xSemaphoreGiveFromISR(xSem, &xWoken);
    portYIELD_FROM_ISR(xWoken);
}

void vUartTask(void *p) {
    for (;;) {
        xSemaphoreTake(xSem, portMAX_DELAY);
        // process received data
    }
}

// Mutex — mutual exclusion (NOT from ISR)
SemaphoreHandle_t xMutex = xSemaphoreCreateMutex();

void vCriticalSection(void) {
    if (xSemaphoreTake(xMutex, pdMS_TO_TICKS(100)) == pdTRUE) {
        // protected access
        shared_resource++;
        xSemaphoreGive(xMutex);
    }
}

// Recursive mutex (same task can take multiple times)
SemaphoreHandle_t xRecursive = xSemaphoreCreateRecursiveMutex();
xSemaphoreTakeRecursive(xRecursive, portMAX_DELAY);
xSemaphoreGiveRecursive(xRecursive);


Use mutex (not binary semaphore) for shared resources to get priority inheritance.

4. Stack overflow detection
// FreeRTOSConfig.h
#define configCHECK_FOR_STACK_OVERFLOW  2  // Method 2 (pattern + watermark)
#define configUSE_MALLOC_FAILED_HOOK    1

// Implement the hook (called when overflow detected)
void vApplicationStackOverflowHook(TaskHandle_t xTask, char *pcTaskName) {
    // Log the offending task name, then halt
    configASSERT(0);  // triggers assertion failure
}

void vApplicationMallocFailedHook(void) {
    configASSERT(0);
}


Check watermarks at runtime:

// Returns minimum ever free stack words
UBaseType_t uxHighWaterMark = uxTaskGetStackHighWaterMark(xHandle);
printf("Stack headroom: %lu words\n", uxHighWaterMark);
// Rule of thumb: keep headroom > 20 words

5. Essential FreeRTOSConfig.h settings
// FreeRTOSConfig.h — adapt to your MCU
#define configCPU_CLOCK_HZ              (SystemCoreClock)
#define configTICK_RATE_HZ              1000          // 1ms tick
#define configMAX_PRIORITIES            8
#define configMINIMAL_STACK_SIZE        128           // words
#define configTOTAL_HEAP_SIZE           (16 * 1024)  // bytes
#define configMAX_TASK_NAME_LEN         16

// Debug / safety
#define configUSE_TRACE_FACILITY        1
#define configUSE_STATS_FORMATTING_FUNCTIONS  1
#define configCHECK_FOR_STACK_OVERFLOW  2
#define configUSE_MALLOC_FAILED_HOOK    1
#define configASSERT(x) if((x)==0) { taskDISABLE_INTERRUPTS(); for(;;); }

// Features
#define configUSE_MUTEXES               1
#define configUSE_RECURSIVE_MUTEXES     1
#define configUSE_COUNTING_SEMAPHORES   1
#define configUSE_TIMERS                1
#define configTIMER_TASK_STACK_DEPTH    (configMINIMAL_STACK_SIZE * 2)

6. GDB debugging with OpenOCD
# Connect GDB with FreeRTOS thread awareness
# OpenOCD provides FreeRTOS-aware RTOS plugin

# openocd.cfg addition
# source [find rtos/FreeRTOS.cfg]  # auto-loads with most targets

# GDB session
(gdb) info threads          # lists all FreeRTOS tasks
(gdb) thread 3              # switch to task 3
(gdb) bt                    # backtrace of that task's stack
(gdb) frame 2               # inspect specific frame

# Print task list from GDB (if trace facility enabled)
(gdb) call vTaskList(buf)
(gdb) printf "%s\n", buf


For OpenOCD setup details, see skills/embedded/openocd-jtag. For FreeRTOSConfig.h reference, see references/freertos-config.md.

Related skills
Use skills/embedded/openocd-jtag for GDB/OpenOCD remote debugging setup
Use skills/embedded/linker-scripts for placing FreeRTOS heap in specific RAM regions
Use skills/debuggers/gdb for general GDB session management
Use skills/embedded/zephyr for an alternative RTOS with built-in device management
Weekly Installs
89
Repository
mohitmishra786/…v-skills
GitHub Stars
80
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass