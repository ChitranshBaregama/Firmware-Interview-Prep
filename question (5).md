# Debugging — UART RX Stuck Low

## Problem
A UART receiver repeatedly reads framing errors / unexpected `0x7F`, and the RX line appears low while idle.

Create a systematic hardware + firmware diagnosis plan. Include idle polarity, pin mux, pull configuration, voltage levels, ground reference, baud mismatch, inversion, contention and oscilloscope/logic-analyzer checks.

