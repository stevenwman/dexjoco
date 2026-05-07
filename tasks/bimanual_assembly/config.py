from tasks.config import TaskConfigBase
from tasks.sim_teleop import (
    BimanualTeleopConfig,
    DualArmViveHandTeleopWrapper,
)
from dexjoco_sim.envs.panda_bimanual_assembly_env import PandaBimanualAssemblyGymEnv
from tasks.obs_adapters import DexjocoObsAdapter


class TaskConfig(TaskConfigBase):
    proprio_keys = ["tcp_pose", "gripper_pose", "socket_ori_pose", "peg_ori_pose", "table_delta_height"]
    teleop = BimanualTeleopConfig(pose_scale=1.5)

    def get_environment(self, fake_env=False, render_mode="human", randomize=False, **kwargs):
        env = PandaBimanualAssemblyGymEnv(render_mode=render_mode, randomize=randomize, hz=30, **kwargs)
        if not fake_env:
            env = DualArmViveHandTeleopWrapper(env, self.teleop)
        env = DexjocoObsAdapter(env, proprio_keys=self.proprio_keys)
        return env

    def process_demos(self, demo):
        return demo
