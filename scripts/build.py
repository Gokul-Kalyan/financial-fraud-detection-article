from pathlib import Path

import yaml
from pathlib import Path


def load_config():
    """
    Load the article configuration from config/book.yml.
    Returns:
        dict: Parsed configuration.
    Raises:
        FileNotFoundError: If book.yml does not exist.
    """

    config_path = Path("config") / "book.yml"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


def validate_config(config):
    """
    Validate the required configuration fields.

    Args:
        config (dict): Parsed YAML configuration.

    Raises:
        ValueError: If any required field is missing or invalid.
    """

    required_fields = [
        "title",
        "subtitle",
        "author",
        "chapters",
    ]

    for field in required_fields:
        if field not in config:
            raise ValueError(
                f"Missing required field in book.yml: '{field}'"
            )

    if not isinstance(config["chapters"], list):
        raise ValueError("'chapters' must be a list.")

    if len(config["chapters"]) == 0:
        raise ValueError("'chapters' cannot be empty.")

def validate_chapters(config):
    """
    Validate that all chapter files listed in the configuration exist.

    Args:
        config (dict): Parsed YAML configuration.

    Raises:
        FileNotFoundError: If any chapter file does not exist.
    """

    for chapter in config["chapters"]:
        chapter_path = Path(chapter)

        if not chapter_path.exists():
            raise FileNotFoundError(
                f"Chapter file not found: {chapter_path}"
            )

def build_article(config):
    """
    Generate the final article by combining all chapters.

    Args:
        config (dict): Validated configuration.
    """

    output_path = Path("manuscript") / "FINAL_ARTICLE.md"

    with output_path.open("w", encoding="utf-8") as outfile:

        # Write article header
        outfile.write(f"# {config['title']}\n\n")
        outfile.write(f"> {config['subtitle']}\n\n")
        outfile.write(f"**Author:** {config['author']}\n\n")
        outfile.write("---\n\n")

        # Append chapters
        for chapter in config["chapters"]:
            chapter_path = Path(chapter)

            with chapter_path.open("r", encoding="utf-8") as infile:
                outfile.write(infile.read())

            outfile.write("\n\n---\n\n")

def main():
    try:
        config = load_config()

        validate_config(config)

        validate_chapters(config)

        build_article(config)

        print("=" * 50)
        print(" Article Build Successful")
        print("=" * 50)
        print(f"Title    : {config['title']}")
        print(f"Author   : {config['author']}")
        print(f"Chapters : {len(config['chapters'])}")
        print("Output   : manuscript/FINAL_ARTICLE.md")

    except Exception as error:
        print("=" * 50)
        print(" Build Failed")
        print("=" * 50)
        print(error)


if __name__ == "__main__":
    main()