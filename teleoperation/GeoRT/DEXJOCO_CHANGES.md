# Dexjoco Changes

This directory contains third-party GeoRT code plus local Dexjoco-specific
changes for non-commercial research use.

## Local Additions

- Rokoko mocap evaluation script:
  - `geort/mocap/rokoko_evaluation.py`
- Rokoko-to-UDP retargeting senders:
  - `geort/mocap/rokoko_retarget_send_right.py`
  - `geort/mocap/rokoko_retarget_send_left.py`

## Dexjoco Integration Notes

- The right-hand sender publishes retargeted joint values to UDP port `5014`.
- The left-hand sender publishes retargeted joint values to UDP port `5016`.
- Dexjoco's simulator receives these packets in `tasks/sim_teleop.py`.

GeoRT keeps its own upstream `LICENSE`. Treat this folder as a third-party
component, not Dexjoco core code.
