import os
import click
from .config import ProductionConfig, TestingConfig
from .constant import StageOption
from .ecs import ECS


Config = ProductionConfig() if os.getenv('DEPLOY_CONFIGURATION') == 'production' else TestingConfig()


@click.command()
@click.option('--stage', default='third', help='first|second(Deploy stage)')
def main(stage):
    ecs = ECS(Config)
    if stage == StageOption.FIRST.value:
        ecs.run_first_stage()
    elif stage == StageOption.SECOND.value:
        ecs.run_second_stage()
    else:
        print("Usage: python3 deploy.py --stage=first|second")


if __name__ == '__main__':
    main()
