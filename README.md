# Firmware Interview Prep

A portable, code-first workspace for becoming interview-ready for Embedded/Firmware roles.

## Target
- 1,500 technical/coding questions
- 150 dedicated interview questions
- Code from scratch, compile, test, debug, explain, revisit
- Works locally or in GitHub Codespaces

## Curriculum
| Track | Questions |
|---|---:|
| C Fundamentals & Language Mechanics | 150 |
| Pointers, Arrays, Strings & Memory | 170 |
| Bit Manipulation & Registers | 120 |
| Data Structures & Algorithms | 180 |
| Embedded C & Defensive Firmware | 130 |
| MCU Architecture, GPIO & Interrupts | 100 |
| Timers, PWM, ADC, DMA & RTC | 90 |
| UART, SPI, I2C, CAN & Communication | 120 |
| FreeRTOS, Concurrency & Synchronization | 130 |
| Debugging, Optimization & Testing | 100 |
| Networking & Embedded Protocols | 60 |
| Security & Cryptography | 50 |
| DLMS/COSEM & Protocol Engineering | 50 |
| Embedded Linux, C++ & System Design | 50 |
| **Total** | **1500** |

## Status
- ⬜ Unseen
- 🟡 Attempted
- 🟢 Solved
- 🔵 Solved without help
- ⭐ Interview Ready
- 🔴 Revisit

## Daily Loop
1. Pick the next item from `TRACKER.md`.
2. Read the problem only.
3. Write the solution from scratch.
4. Compile with strict warnings.
5. Run tests and edge cases.
6. Debug before looking for help.
7. Write the root cause of every mistake.
8. Explain time/space complexity and embedded implications.
9. Update status and schedule weak questions for revision.

## Build
```bash
gcc -std=c11 -Wall -Wextra -Wpedantic -Wconversion -g solution.c test.c -o test
./test
```

## Codespaces
Upload this project to GitHub, then use:
**Code → Codespaces → Create codespace on main**

## Safety
Never add employer-proprietary source, credentials, production keys/certificates, or confidential project data.
