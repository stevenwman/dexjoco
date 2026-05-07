# Simulation Demo Collection Walkthrough

This repository is now trimmed around simulated teleoperation data collection.
Optional UDP teleoperation providers are documented in
[`teleop_udp_protocol.md`](teleop_udp_protocol.md).
The main supported workflow is:

1. choose one of the kept simulation tasks
2. run `scripts/record_demos_zarr.py`
3. teleoperate in MuJoCo and save successful episodes as Zarr demos

The kept tasks are:

- `Water Plant` (`water_plant`)
- `Fold Glasses` (`fold_glasses`)
- `Click Mouse` (`click_mouse`)
- `Pinch Tongs` (`pinch_tongs`)
- `Pick Bucket` (`pick_bucket`)
- `Hammer Nail` (`hammer_nail`)
- `Bimanual Microwave Cook` (`bimanual_microwave_cook`)
- `Bimanual Unlock iPad` (`bimanual_unlock_ipad`)
- `Bimanual Hanoi` (`bimanual_hanoi`)
- `Bimanual Assembly` (`bimanual_assembly`)
- `Bimanual Photograph` (`bimanual_photograph`)

## Environment

Use the `dexjoco` conda environment:

```bash
conda run -n dexjoco python scripts/record_demos_zarr.py --exp_name=water_plant
```

If you prefer to enter the environment first:

```bash
conda activate dexjoco
cd scripts
python record_demos_zarr.py --exp_name=water_plant
```

## Recommended command

From the repository root:

```bash
conda run -n dexjoco python scripts/record_demos_zarr.py \
  --exp_name=water_plant \
  --successes_needed=20 \
  --randomize=True
```

Useful flags:

- `--exp_name`: one of the kept task names above
- `--successes_needed`: stop automatically after this many successful demos
- `--randomize=True`: keep simulation domain randomization enabled during collection
- `--render_mode=human`: open the MuJoCo viewer for teleoperation
- `--show_sim_cameras=True`: show the OpenCV camera grid window
- `--out_dir=PATH`: choose where the collected demos are written

## During collection

- successful episodes are saved automatically
- failed episodes are discarded automatically
- press `R` in the viewer loop to drop the current trajectory and reset
- teleop wrappers keep the current end-effector pose when you are not actively intervening

Each successful demo is written to its own directory:

```text
<out_dir>/<exp_name>_demo_<index>_<timestamp>/
  replay.zarr/
  videos/
```

## Notes

- The task configs under `tasks/*/config.py` are intentionally minimal and centered on simulated teleoperation capture.
- Domain randomization is preserved through the `randomize` argument in each task environment.
- Legacy reward-classifier training, policy-training launch scripts, and real-robot deployment helpers have been removed from this trimmed setup.
