# Rokoko Bridge

This directory contains the external Rokoko Studio bridge. These scripts run on
another PC that hosts Rokoko Studio, listen to the local Rokoko UDP stream,
canonicalize hand keypoints, and forward them to the remote Dexjoco machine.

## Role In The Full Pipeline

For teleoperation with hand retargeting, the expected flow is:

1. Rokoko Studio on the bridge PC publishes hand keypoints to `127.0.0.1:14044`
2. The scripts in this directory receive those packets on that same PC
3. Raw canonicalized keypoints are forwarded to the Linux Dexjoco machine:
   - right hand -> UDP `5013`
   - left hand -> UDP `5015`
4. `teleoperation/GeoRT/geort/mocap/rokoko_retarget_send_right.py` on Linux
   reads `5013` and publishes retargeted joints to `5014`
5. `teleoperation/GeoRT/geort/mocap/rokoko_retarget_send_left.py` on Linux
   reads `5015` and publishes retargeted joints to `5016`
6. `tasks/sim_teleop.py` consumes `5014` and `5016`

## Dependencies

These scripts use:

- `numpy`
- `lz4` if Rokoko Studio sends compressed UDP packets

Install `lz4` on the bridge PC if needed:

```bash
pip install lz4
```

## Forward One Hand

Right hand to the Linux machine:

```bash
python teleoperation/rokoko/rokoko_mocap.py \
  --hand right \
  --target-ip <linux_ip>
```

Left hand to the Linux machine:

```bash
python teleoperation/rokoko/rokoko_mocap.py \
  --hand left \
  --target-ip <linux_ip>
```

You can override the local Rokoko bind address if needed:

```bash
python teleoperation/rokoko/rokoko_mocap.py \
  --listen-ip 127.0.0.1 \
  --listen-port 14044 \
  --target-ip <linux_ip>
```

## Forward Both Hands

```bash
python teleoperation/rokoko/rokoko_mocap_bimanual.py \
  --target-ip <linux_ip>
```

By default this sends:

- left hand to `5015`
- right hand to `5013`

## Record Canonicalized Keypoints To NPY

These recordings are intended for GeoRT retarget model training. The saved
`.npy` arrays contain canonicalized `(T, 21, 3)` hand keypoints that can be
used as the human-motion side of a GeoRT training dataset.

Right hand:

```bash
python teleoperation/rokoko/collect_mocap_data.py \
  --hand right \
  --output-dir ./data
```

Left hand:

```bash
python teleoperation/rokoko/collect_mocap_data.py \
  --hand left \
  --output-dir ./data
```

## Notes

- These scripts are part of the main Dexjoco repository, but they are meant to
  run on the separate PC that hosts Rokoko Studio.


