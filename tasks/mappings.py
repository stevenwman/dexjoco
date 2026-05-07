from importlib import import_module


TASK_SPECS = (
    {
        "task_id": "water_plant",
        "display_name": "Water Plant",
        "aliases": ("water plant",),
        "target": ("tasks.water_plant.config", "TaskConfig"),
    },
    {
        "task_id": "fold_glasses",
        "display_name": "Fold Glasses",
        "aliases": ("fold glasses", "glass_fold"),
        "target": ("tasks.fold_glasses.config", "TaskConfig"),
    },
    {
        "task_id": "click_mouse",
        "display_name": "Click Mouse",
        "aliases": ("click mouse", "monitor_mousepad"),
        "target": ("tasks.click_mouse.config", "TaskConfig"),
    },
    {
        "task_id": "pinch_tongs",
        "display_name": "Pinch Tongs",
        "aliases": ("pinch tongs", "table_tongs"),
        "target": ("tasks.pinch_tongs.config", "TaskConfig"),
    },
    {
        "task_id": "pick_bucket",
        "display_name": "Pick Bucket",
        "aliases": ("pick bucket", "bucket_pick"),
        "target": ("tasks.pick_bucket.config", "TaskConfig"),
    },
    {
        "task_id": "hammer_nail",
        "display_name": "Hammer Nail",
        "aliases": ("hammer nail",),
        "target": ("tasks.hammer_nail.config", "TaskConfig"),
    },
    {
        "task_id": "bimanual_microwave_cook",
        "display_name": "Bimanual Microwave Cook",
        "aliases": ("bimanual microwave cook", "microwave_cook"),
        "target": ("tasks.bimanual_microwave_cook.config", "TaskConfig"),
    },
    {
        "task_id": "bimanual_unlock_ipad",
        "display_name": "Bimanual Unlock iPad",
        "aliases": ("bimanual unlock ipad", "ipad_unlock"),
        "target": ("tasks.bimanual_unlock_ipad.config", "TaskConfig"),
    },
    {
        "task_id": "bimanual_hanoi",
        "display_name": "Bimanual Hanoi",
        "aliases": ("bimanual hanoi", "hanoi"),
        "target": ("tasks.bimanual_hanoi.config", "TaskConfig"),
    },
    {
        "task_id": "bimanual_assembly",
        "display_name": "Bimanual Assembly",
        "aliases": ("bimanual assembly", "assembly"),
        "target": ("tasks.bimanual_assembly.config", "TaskConfig"),
    },
    {
        "task_id": "bimanual_photograph",
        "display_name": "Bimanual Photograph",
        "aliases": ("bimanual photograph", "photograph"),
        "target": ("tasks.bimanual_photograph.config", "TaskConfig"),
    },
)


TASK_CONFIGS = {spec["task_id"]: spec["target"] for spec in TASK_SPECS}
TASK_DISPLAY_NAMES = {spec["task_id"]: spec["display_name"] for spec in TASK_SPECS}
TASK_ALIASES = {}

for spec in TASK_SPECS:
    task_id = spec["task_id"]
    alias_names = {task_id, spec["display_name"], *spec["aliases"]}
    for alias in alias_names:
        TASK_ALIASES[alias.casefold()] = task_id


def resolve_task_name(task_name):
    task_id = TASK_ALIASES.get(task_name.casefold())
    if task_id is None:
        raise KeyError(task_name)
    return task_id


def get_task_display_name(task_name):
    return TASK_DISPLAY_NAMES[resolve_task_name(task_name)]


def list_supported_task_names():
    return tuple(spec["display_name"] for spec in TASK_SPECS)


class LazyConfigMapping(dict):
    def __contains__(self, key):
        try:
            key = resolve_task_name(key)
        except (AttributeError, KeyError):
            return False
        return super().__contains__(key)

    def __getitem__(self, key):
        task_id = resolve_task_name(key)
        module_name, class_name = super().__getitem__(task_id)
        module = import_module(module_name)
        return getattr(module, class_name)


CONFIG_MAPPING = LazyConfigMapping(TASK_CONFIGS)
