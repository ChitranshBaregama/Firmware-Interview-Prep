# Interrupts — ISR Event Handoff

## Problem
Design an ISR-to-main-loop event handoff for a bare-metal MCU.

The ISR may receive bursts of events. Avoid long ISR execution and avoid silently losing events. Discuss atomicity and overflow behavior.

