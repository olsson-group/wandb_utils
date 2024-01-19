from argparse import ArgumentParser

import wandb
import concurrent


def main(args):
    api = wandb.Api(overrides={"project": args.project})
    project = api.project(args.project)

    tasks = []
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)

    for artifact_type in project.artifacts_types():  # pylint: disable=too-many-nested-blocks
        for artifact_collection in artifact_type.collections():
            artifacts = api.artifacts(artifact_type.type, artifact_collection.name)
            for artifact in artifacts:
                if artifact_type.type == "model":
                    executor.submit(delete, artifact, args.dry_run)

    executor.shutdown(wait=True)


def delete(artifact, dry_run):
    if len(artifact.aliases) > 0:
        print(f"KEEPING {artifact.name}")
    else:
        print(f"DELETING {artifact.name}")
        if not dry_run:
            artifact.delete()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--dry_run", action="store_true")

    main(parser.parse_args())
