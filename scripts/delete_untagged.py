from argparse import ArgumentParser

import wandb


def main(args):

    """
    deletes all models that do not have a tag attached

    by default this means wandb will delete all but the "latest" or "best" models

    set dry_run == False to delete...
    """

    api = wandb.Api(overrides={"project": args.project})
    project = api.project(args.project)

    for artifact_type in project.artifacts_types():
        collections = artifact_type.collections()
        for artifact_collection in artifact_type.collections():
            artifacts = api.artifacts(artifact_type.type, artifact_collection.name)
            for artifact in artifacts:
                if artifact_type.type == "model":
                    if len(artifact.aliases) > 0:
                        print(f"KEEPING {artifact.name}")
                    else:
                        print(f"DELETING {artifact.name}")
                        if not args.dry_run:
                            artifact.delete()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--dry_run", action="store_true")

    # parser.add_argument('arg')
    # parser.add_argument('--kwarg')

    main(parser.parse_args())
