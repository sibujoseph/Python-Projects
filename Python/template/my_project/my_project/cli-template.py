import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="My Project - A Production-Ready Python App"
    )
    parser.add_argument("-c", "--config", type=str, help="Path to config file (JSON)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    return parser.parse_args()
