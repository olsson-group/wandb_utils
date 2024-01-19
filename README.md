Install by 

    git clone https://github.com/olsson-group/wandb_utils.git
    cd wandb_utils
    running pip install -e . 

Run

    python scripts/delet_untagged.py {project_name}


To delete all untagged models in {project_name}.

By default wandb tags the "latest" or "best" models.

Run 

    python scripts/delet_untagged.py {project_name} --dry_run

for a dry run to see which models will be kept/deleted
